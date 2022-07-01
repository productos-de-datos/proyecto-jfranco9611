def compute_daily_prices():
    import pandas as pd
    df = pd.read_csv("data_lake/cleansed/Data_Prices.csv",
                     index_col=None, header=0)
    df = df[["date", "price"]]
    df["date"] = pd.to_datetime(df["date"])
    compute_daily_prices = df.groupby("date").mean({"price": "price"})
    compute_daily_pric
        "data_lake/business/Data_Prices.csv", index=None, header=True)



if __name__ == "__main__":
    import doctest

    doctest.testmod()
    compute_daily_prices()
