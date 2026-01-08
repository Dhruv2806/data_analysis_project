import pandas as pd
import random
from datetime import datetime, timedelta

def generate_sales_data(rows=500):
    products = [
        ("Coke", "Beverages", 20),
        ("Pepsi", "Beverages", 18),
        ("Water", "Beverages", 25),
        ("Milk", "Dairy", 52),
        ("Eggs", "Dairy", 6),
        ("Bread", "Bakery", 30),
        ("Biscuits", "Snacks", 15),
        ("Chips", "Snacks", 20),
    ]

    start_date = datetime(2024, 1, 1)
    data = []

    for _ in range(rows):
        product, category, price = random.choice(products)
        quantity = random.randint(1, 15)
        date = start_date + timedelta(days=random.randint(0, 120))

        data.append([date, product, category, price, quantity])

    df = pd.DataFrame(
        data,
        columns=["Date", "Product", "Category", "Price", "Quantity"]
    )

    df.to_csv("D:/cs/Data Analysis Project/Data/sales_data.csv", index=False)
    print("Sales dataset generated successfully!")

if __name__ == "__main__":
    generate_sales_data()
