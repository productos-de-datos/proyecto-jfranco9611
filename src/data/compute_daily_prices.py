def compute_daily_prices():
    import pandas as pd
    df = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    df_prom = df.groupby(['fecha']).mean().reset_index()
    df_prom.to_csv('data_lake/business/precios-diarios.csv', index=False)
    print("promedio diario --> data_lake/business/precios-diarios.csv")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    compute_daily_prices()