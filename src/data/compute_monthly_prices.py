def compute_monthly_prices():
    import pandas as pd
    df = pd.read_csv("data_lake/cleansed/Data_Prices.csv",
                     index_col=None, header=0)
    df["date"] = pd.to_datetime(df["date"])
    df['YMonth'] = ((df['date'].dt.year).astype(int)).astype(
        str) + "-" + ((df[].dt.month).astype(int)).astype(str)


    Dagg_01 = data_D.groupby("YMonth").max({"day": "day"})
    Dagg_01.reset_index(inplace=True)
    Dagg_01['date'] = Dagg_01['YMonth'] + \ "-" + (Dagg_01['day']).astype(str)
    Dagg_01["date"] = pd.to_datetime(Dagg_01["date"])

    df_01 = df[["YMonth", "price"]]
    MPrice_01 = dfm.groupby(
        "YMonth").mean({"avg_price": "price"})
    MPrice_01.reset_index(inplace=True)

    MPrice_01 = pd.merge(
        Dagg_01, MPrice_01, on="YMonth", how="left")

    MPrice_01 = MPrice_01[["date", "price"]]

    MPrice_01 = MPrice_01.sort_values(by='date')
    MPrice_01.to_csv("data_lake/business/Data_MPrices.csv", index=None, header=True)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    compute_monthly_prices()
