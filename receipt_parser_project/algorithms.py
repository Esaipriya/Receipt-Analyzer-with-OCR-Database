import pandas as pd

def to_dataframe(data):
    return pd.DataFrame(data, columns=["ID", "Vendor", "Date", "Amount"])

def aggregate_stats(df):
    return {
        "Total Spend": df["Amount"].sum(),
        "Average": df["Amount"].mean(),
        "Top Vendor": df["Vendor"].value_counts().idxmax()
    }

def group_by_vendor(df):
    return df.groupby("Vendor")["Amount"].sum().reset_index()

def time_series(df):
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return df.groupby(df['Date'].dt.to_period('M'))["Amount"].sum().reset_index()
