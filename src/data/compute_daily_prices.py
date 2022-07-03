## Enb este documento se realizará la limpieza de todos los precios diarios
## Este documento estará enlazado a los otros desde el archivo del pipeline
## al igual que los otros para su modificación se debe reemplazar la dirección registrada en
## df_prom por la nueva base creada


def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



    """
    import pandas as pd
    df = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    df_prom = df.groupby(['fecha']).mean().reset_index()
    df_prom.to_csv('data_lake/business/precios-diarios.csv', index=False)
    print("promedio diario --> data_lake/business/precios-diarios.csv")


if __name__ == "__main__":
    import doctest
    compute_daily_prices()
    doctest.testmod()
