def make_features():
    import pandas as pd
    df = pd.read_csv('data_lake/business/precios-diarios.csv')
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')
    df['weekday'] = df.fecha.dt.weekday
    df.to_csv('data_lake/business/features/precios_diarios.csv', index=False)
    print ("Saved features--->")
    return True

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_features()
