import pandas as pd
from database import get_connection
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

def display_database():
    try:
        conn = get_connection()
        df = pd.read_sql("SELECT * FROM cars", conn)
        conn.close()

        if df.empty:
            print("The database is currently empty.")
        else:
            print("\n--- Current Data in Database ---")
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', 1000)
            
            print(df)
            
            print(f"\nTotal cars found: {len(df)}")
            
    except Exception as e:
        print(f"Error connecting to database: {e}")

if __name__ == "__main__":
    display_database()


    ##USE electric_cars
    ##TRUNCATE TABLE cars;