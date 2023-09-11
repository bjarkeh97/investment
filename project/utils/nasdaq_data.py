import pandas as pd
import os

"""
Data from https://www.nasdaqomxnordic.com/
"""

def get_csv(path: str) -> pd.Series:
    basename = os.path.basename(path).removesuffix(".csv")
    df = pd.read_csv(path, sep=";")
    try:
        highs = df["Highprice"].replace(",","", regex=True).astype(float)
        lows = df["Lowprice"].replace(",","", regex=True).astype(float)
    except AttributeError:
        highs = df["Highprice"]
        lows = df["Lowprice"]
    avg = (highs+lows)/2
    index = pd.to_datetime(df["Date"])
    avg_prices = pd.Series(data=avg.to_list(), index=index.to_list())
    avg_prices = avg_prices.rename(basename)
    return avg_prices

def nordic_str_to_float(string: str) -> float:
    string = string.replace(".","")
    string = string.replace(",", ".")
    return float(string)

if __name__ == "__main__":
    test_path = "C:/Users/Bruger/Code/quantitative_investment/data_nasdaq/sectors/HEALTHDK.csv"
    df = get_csv(path=test_path)
    print(df)