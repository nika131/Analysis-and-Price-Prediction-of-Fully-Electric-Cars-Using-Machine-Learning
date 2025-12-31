import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from database import get_connection
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

def run_visuals():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM cars", conn)
    conn.close()

    if df.empty:
        print("The database table is empty!")
        return

    print(f"Total rows found in DB: {len(df)}")
    
    df_clean = df.dropna(subset=['battery_kwh', 'range_km', 'price_eur']).copy()
    
    print(f"Rows remaining after cleaning: {len(df_clean)}")

    if len(df_clean) == 0:
        print("Error: Not enough data to plot.")
        return

    print("\n--- Summary Statistics ---")
    print(df_clean[['battery_kwh', 'range_km', 'price_eur']].describe())

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Subplot 1: Battery vs Price
    sns.regplot(
        data=df_clean, x="battery_kwh", y="price_eur", ax=ax1,
        scatter_kws={'alpha': 0.6, 'color': 'blue'},
        line_kws={'color': 'red', 'label': 'Trend Line'},
        ci=None 
    )
    ax1.set_title("Battery (kWh) vs Price (€) + Regression")
    ax1.set_xlabel("Battery (kWh)")
    ax1.set_ylabel("Price (€)")
    ax1.grid(True, linestyle='--', alpha=0.5)

    # Subplot 2: Range vs Price
    sns.regplot(
        data=df_clean, x="range_km", y="price_eur", ax=ax2,
        scatter_kws={'alpha': 0.6, 'color': 'green'},
        line_kws={'color': 'orange', 'label': 'Trend Line'},
        ci=None
    )
    ax2.set_title("Range (km) vs Price (€) + Regression")
    ax2.set_xlabel("Range (km)")
    ax2.set_ylabel("Price (€)")
    ax2.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_visuals()