import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)

    # Convert Date to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Remove invalid values
    df = df[df['Quantity'] > 0]
    df = df[df['Price'] > 0]

    # Create Revenue column
    df['Revenue'] = df['Price'] * df['Quantity']

    return df
