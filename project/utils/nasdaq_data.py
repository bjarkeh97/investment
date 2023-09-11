import pandas as pd
import os

"""
Data from https://www.nasdaqomxnordic.com/
"""

def get_csv(path: str) -> pd.Series:
    basename = os.path.basename(path).removesuffix(".csv")
    df = pd.read_csv(path, sep=";")
    highs = df["Highprice"].apply(nordic_str_to_float)
    lows = df["Lowprice"].apply(nordic_str_to_float)
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
    test_path = "C:/Users/Bruger/Code/quantitative_investment/data_nasdaq/index/FIRSTNORTHDK.csv"
    df = get_csv(path=test_path)
    print(df)