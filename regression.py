import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from database import get_connection

def train_model():
    conn = get_connection()

    df = pd.read_sql("SELECT battery_kwh, range_km, power_hp, top_speed, price_eur FROM cars", conn)
    conn.close()

    df = df.dropna()

    if len(df) < 5:
        print(f"Error: Not enough data for regression. Found {len(df)} valid rows.")
        print("Please run scraper.py first and ensure it finds prices!")
        return

    X = df.drop("price_eur", axis=1)
    y = df["price_eur"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    print(f" Success! Model Accuracy (R²): {r2_score(y_test, preds):.2f}")
    
    test_car = [[75, 450, 200, 180]]
    prediction = model.predict(test_car)
    print(f"Predicted Price: €{prediction[0]:,.2f}")

if __name__ == "__main__":
    train_model()
