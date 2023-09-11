import pandas as pd
import os

"""
To get data.

Download from NORDNET. Insert into https://www.convertcsv.com/csv-viewer-editor.htm and download again (this step should somehow be automatic)
"""

def get_csv(path: str) -> pd.Series:
    basename = os.path.basename(path).removesuffix(".csv")
    df = pd.read_csv(path, sep="	", encoding = "utf-8")
    highs = df["Højeste"]
    lows = df["Laveste"]
    avg = (highs+lows)/2
    index = pd.to_datetime(df["Dato"], format="%d.%m.%Y")
    avg_prices = pd.Series(data=avg.to_list(), index=index.to_list())
    avg_prices = avg_prices.rename(basename)
    return avg_prices

if __name__ == "__main__":
    test_path = "C:/Users/Bruger/Code/quantitative_investment/data_nordnet/crypto/BTCXBT.csv"
    df = get_csv(path=test_path)
    print(df)