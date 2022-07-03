## Al igual que el archivo de compute_daily_prices este realizara el computo para
## los precios de forma mensual. También estará enlazado a los demás archivos desde el pipeline
## para su uso en otra base solo de sebe modificar el campo df_M_prom por el nuevo repositorio


def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
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
