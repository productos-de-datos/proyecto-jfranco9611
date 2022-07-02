def compute_monthly_prices():
    import pandas as pd
    df = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    df['fecha'] = df[['fecha']].apply(pd.to_datetime)
    df['fecha'] = df['fecha'].dt.to_period('M').dt.to_timestamp()
    df_M_prom = df.groupby(['fecha']).mean().reset_index()
    df_M_prom.to_csv('data_lake/business/precios-mensuales.csv', index=False)
    print("promedio mensual --> data_lake/business/precios-mensuales.csv")


if __name__ == "__main__":
    import doctest
    compute_monthly_prices()
    doctest.testmod()