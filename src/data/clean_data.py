## Definición funcion 1

    
    path_file = glob.glob(r'data_lake/raw/*.csv')
    data_01 = []

    for filename in path_file:
        df = pd.read_csv(filename, index_col=None, header=0)
        data_01.append(df)
    return data_01


## Definición funcion 2
def reading(data_01):
    import pandas as pd
    data_02 = pd.concat(data_01, axis=0, ignore_index=True)
    data_02 = data_02[data_02["Fecha"].notnull()]
    return data_02


## Definición funcion 3
def transform(data_02):


    for x1 in dat01:
        for x2 in range(0, 24):
            pr1 = (read_file.iloc[pr2, (x2+1)])
            data_03.append([x1, x2, pr1])
        pr2 += 1

    return data_03
    
    
 ## Definición funcion 4
 def consolid(data_03):
    import pandas as pd
    data_04 = pd.DataFrame(
        data_03, columns=["date", "hour", "price"])
    data_04 = data_04[data_04["price"].notnull()]
    return data_04
    
    
 ## Definición funcion 5
 def Final(data_04):
    data_04.to_csv("data_lake/cleansed/Data_Prices.csv",
                         index=None, header=True)

## Se agrupa la base
def clean_data():
    data_01 = loading()
    data_02 = reading(data_01)
    data_03 = transform(data_02)
    data_04 = consolid(data_03)
    Final(data_04)

## Se crea el test
def test_data_01():
    data_01 = loading()
    data_02 = reading(data_01)
    data_03 = transform(data_02)
    assert list(consolid(data_03).columns.values) == [
        'date', 'hour', 'price']

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    clean_data()
