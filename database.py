import mysql.connector

DB_NAME = "electric_cars"

def get_connection(init=False):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        charset="utf8mb4"
    )
    cursor = conn.cursor()

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.execute(f"USE {DB_NAME}")

    if init:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cars (
                id INT AUTO_INCREMENT PRIMARY KEY,
                brand VARCHAR(100),
                model VARCHAR(150),
                battery_kwh FLOAT,
                range_km INT,
                power_hp INT,
                acceleration_0_100 FLOAT,
                top_speed INT,
                price_eur BIGINT,
                UNIQUE (brand, model)
            )
        """)
        conn.commit()

    cursor.close()
    return conn