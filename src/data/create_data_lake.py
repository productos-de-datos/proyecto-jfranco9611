def create_data_lake():
    # raise NotImplementedError("Implementar esta función")
    import os
    os.mkdir('data_lake')
    os.mkdir('data_lake/landing')
    os.mkdir('data_lake/raw')
    os.mkdir('data_lake/cleansed')
    os.mkdir('data_lake/business')
    os.mkdir('data_lake/business/reports')
    os.mkdir('data_lake/business/reports/figures')
    os.mkdir('data_lake/business/features')
    os.mkdir('data_lake/business/forecasts')


if __name__ == "__main__":
    import doctest

    create_data_lake()
    doctest.testmod()