from Src.data_cleaning import load_and_clean_data
from Src.eda import sales_summary, plot_sales_trend
from Src.model import train_model

df = load_and_clean_data("data/sales_data.csv")

sales_summary(df)
plot_sales_trend(df)
model = train_model(df)
