def transform_data():
    import pandas as pd

    # Transforma de 1995 a 1999 excluyendo las 3 primeras filas
    for i in range(1995, 2000):
        file_ = 'data_lake/raw/' + str(i) + '.csv'
        path = "data_lake/landing/" + str(i) + ".xlsx"
        df = pd.read_excel(path, skiprows=range(1, 3), header=1, usecols = "A:Y")
        df.to_csv(file_, sep=',', encoding='utf-8')
        print ("transform: ", path, "to", file_)

    # Transforma de 2000 a 2016 excluyendo las 2 primeras filas
    for i in range(2000, 2016):
        file_ = 'data_lake/raw/' + str(i) + '.csv'
        path = "data_lake/landing/" + str(i) + ".xlsx"
        df = pd.read_excel(path, skiprows=range(1, 2), header=1, usecols = "A:Y")
        df.to_csv(file_, sep=',', encoding='utf-8')
        print("transform: ", path, "to", file_)

    # Transforma de 2016 y 2017 solo los unicos xls
    for i in range(2016, 2018):
        file_ = 'data_lake/raw/' + str(i) + '.csv'
        path = "data_lake/landing/" + str(i) + ".xls"
        df = pd.read_excel(path, skiprows=range(1, 2), header=1, usecols = "A:Y")
        df.to_csv(file_, sep=',', encoding='utf-8')
        print("transform: ", path, "to", file_)

    # Transforma de 2018 a 2022 sin exclusion
    for i in range(2018, 2022):
        file_ = 'data_lake/raw/' + str(i) + '.csv'
        path = "data_lake/landing/" + str(i) + ".xlsx"
        df = pd.read_excel(path, usecols = "A:Y")
        df.to_csv(file_, sep=',', encoding='utf-8')
        print("transform: ", path, "to", file_)


if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()