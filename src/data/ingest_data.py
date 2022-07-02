def ingest_data():
    import urllib.request
    for i in range(1995, 2022):
        try:
            url = 'https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/' + str(i) + '.xlsx'
            file_ = 'data_lake/landing/' + str(i) + '.xlsx'
            print(url, file_)
            urllib.request.urlretrieve(url, file_)
        except:
            url = 'https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/' + str(i) + '.xls'
            file_ = 'data_lake/landing/' + str(i) + '.xls'
            print(url, file_)
            urllib.request.urlretrieve(url, file_)
            print("An exception occurred")


if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()