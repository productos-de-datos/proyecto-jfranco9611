def clean_data()
    import pandas as pd
    df_fin = pd.DataFrame(columns=['Fecha', 'hora', 'precio'])
    for i in range(1997, 2022):
        file_ = 'data_lake/raw/' + str(i) + '.csv'
        df_ini = pd.read_csv(file_)
        df_melt = pd.melt(df_ini, id_vars=['Fecha'], value_vars=df_ini.columns[2:], var_name='hora',
                          value_name='precio')
        df_fin = pd.concat([df_fin, df_melt], axis=0)
        print("clean and concat", file_)
    df_fin.columns = ['fecha', 'hora', 'precio']
    df_fin.to_csv('data_lake/cleansed/precios-horarios.csv', sep=',', encoding='utf-8', index=False)


if __name__ == "__main__":
    import doctest

    clean_data()
    doctest.testmod()