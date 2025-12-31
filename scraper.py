import requests
from bs4 import BeautifulSoup
import time
import random
import re
from database import get_connection

BASE_URL = "https://ev-database.org"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

session = requests.Session()
session.headers.update(HEADERS)

def parse_car_detail(car_url):
    try:
        response = session.get(car_url, timeout=15)
        if response.status_code != 200: return None
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 1. Getting Brand & Model name
        title_tag = soup.find("h1")
        if not title_tag: return None
        title = title_tag.text.strip()
        brand = title.split(" ")[0]
        model = " ".join(title.split(" ")[1:])

        # 2. Getting Battery & Range
        battery = range_km = None
        icons_section = soup.find("section", id="icons")
        if icons_section:
            for icon in icons_section.find_all("div", class_="icon"):
                text = icon.get_text(separator=" ").strip()
                if "kWh" in text:
                    m = re.search(r"(\d+\.?\d*)", text)
                    if m: battery = float(m.group(1))
                if "km" in text and "Range" in text:
                    m = re.search(r"(\d+)", text)
                    if m: range_km = int(m.group(1))

        # 3. getting Performance stats (Power, Accel, Speed)
        power_hp = acc = spd = None
        perf_section = soup.find("div", id="performance")
        if perf_section:
            for table in perf_section.find_all("table"):
                for tr in table.find_all("tr"):
                    txt = tr.get_text().lower()
                    cols = tr.find_all("td")
                    if len(cols) < 2: continue
                    val = cols[1].text.strip()
                    
                    if "power" in txt:
                        hp_m = re.search(r"\((\d+)\s*(?:ps|hp)\)", val, re.IGNORECASE)
                        if hp_m: 
                            power_hp = int(hp_m.group(1))
                        else:
                            kw_m = re.search(r"(\d+)\s*kw", val, re.IGNORECASE)
                            if kw_m: power_hp = int(int(kw_m.group(1)) * 1.341)
                    elif "acceleration" in txt:
                        acc_m = re.search(r"(\d+\.?\d*)", val)
                        if acc_m: acc = float(acc_m.group(1))
                    elif "top speed" in txt:
                        spd_m = re.search(r"(\d+)", val)
                        if spd_m: spd = int(spd_m.group(1))

        # 4. Price in Euro
        price = None
        price_sec = soup.find("div", id="pricing")
        if price_sec:
            raw_text = price_sec.get_text(strip=True)
            euro_m = re.search(r"€([\d,.]+)", raw_text)
            if euro_m:
                price = int(re.sub(r"[^\d]", "", euro_m.group(1)))

        return (brand, model, battery, range_km, power_hp, acc, spd, price)

    except Exception as e:
        print(f"Error parsing {car_url}: {e}")
        return None

def run_scraper(limit=15):
    conn = get_connection(init=True)
    cursor = conn.cursor()
    
    res = session.get(BASE_URL)
    soup = BeautifulSoup(res.text, "html.parser")
    links = [BASE_URL + a['href'] for a in soup.select("div.list-item a.title")][:limit]
    
    print(f"Starting scrape of {len(links)} cars...")
    
    for i, link in enumerate(links):
        data = parse_car_detail(link)
        if data:
            try:
                query = """INSERT INTO cars (brand, model, battery_kwh, range_km, power_hp, 
                           acceleration_0_100, top_speed, price_eur) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                           ON DUPLICATE KEY UPDATE 
                           power_hp=VALUES(power_hp), 
                           price_eur=VALUES(price_eur)"""
                cursor.execute(query, data)
                print(f"[{i+1}/{len(links)}] SUCCESSFUL SCRAPE & SAVE:")
                print(f"  > Car:        {data[0]} {data[1]}")
                print(f"  > Specs:      {data[2]}kWh | {data[3]}km Range | {data[4]}HP")
                print(f"  > Perf:       0-100 in {data[5]}s | Top Speed: {data[6]}km/h")
                print(f"  > Price:      €{data[7]:,}")
                print("-" * 40)
            except Exception as e:
                print(f"DB Error: {e}")
        
        time.sleep(random.uniform(1, 3))

    conn.commit()
    cursor.close()
    conn.close()
    print("\n Scrape complete!")



def show_raw_html_phase(url):
    print(f"\n[DEMO] Fetching Raw HTML from: {url}")
    response = session.get(url, timeout=10)
    html_preview = response.text[:500].replace('\n', ' ')
    print("-" * 30)
    print(f"RAW HTML (Preview):\n{html_preview}...")
    print("-" * 30)


if __name__ == "__main__":
    demo_url = "https://ev-database.org/car/1011/Tesla-Model-3-Standard-Range-Plus"

    while True:
        print("1. Show Phase 1: Raw HTML (The 'Before')")
        print("2. Run Full Scraper (Save to Database)")
        print("3. Exit")
        
        choice = input("\nSelect a phase to demonstrate (1-4): ")

        if choice == '1':
            show_raw_html_phase(demo_url)
        elif choice == '2':
            limit = input("How many cars to scrape? (default 5): ")
            run_scraper(limit=int(limit) if limit else 5)
        elif choice == '3':
            print("Closing program...")
            break
        else:
            print("Invalid input, try again.")