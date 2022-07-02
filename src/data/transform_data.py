##  ## Definición funcion 1
def Sys_Line(year, A_Type):
    DLine_01 = "data_lake/landing/{}.{}".format(year, A_Type)
    return DLine_01


 ## Definición funcion 2
def loading(DLine_01, DHead_01):
    import pandas as pd
    Dat_01 = pd.read_excel(DLine_01, header=DHead_01)
    Dat_01 = Dat_01.iloc[:, 0:25]
    Dat_01.columns = ['date', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                         '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
    return Dat_01


 ## Definición funcion 3
def Final(Dat_01, year):
    Dat_01.to_csv("data_lake/raw/{}.csv".format(year), index=None)


 ## Definición principal
def transform_data():
    for year in range(1995, 2022):
        if year in range(1995, 2000):
            out_file = Sys_Line(year, "xlsx")
            file = loading(out_file, 3)
            Final(file, year)
        elif (year in range(2000, 2016)):
            out_file = Sys_Line(year, "xlsx")
            file = loading(out_file, 2)
            Final(file, year)
        elif (year in range(2016, 2018)):
            out_file = Sys_Line(year, "xls")
            file = loading(out_file, 2)
            Final(file, year)
        else:
            out_file = Sys_Line(year, "xlsx")
            file = loading(out_file, 0)
            Final(file, year)


 ## Creación de test
def test_answer():
    assert Sys_Line('2021', "xlsx") == "data_lake/landing/2021.xlsx"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    transform_data()
