import matplotlib.pyplot as plt

def sales_summary(df):
    print("\n--- SALES SUMMARY ---")
    print(df.groupby('Category')['Revenue'].sum())

def plot_sales_trend(df):
    daily_sales = df.groupby('Date')['Revenue'].sum()

    plt.figure()
    daily_sales.plot()
    plt.title("Daily Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("outputs/plots/sales_trend.png")
    plt.show()
