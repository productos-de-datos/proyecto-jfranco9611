def make_features():
    import shutil
    shutil.copy('data_lake/business/Data_Prices.csv',
                'data_lake/business/features/Data_Prices.csv')

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_features()
