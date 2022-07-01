def create_data_lake():
    import os
    os.mkdir('./data_lake/')
    parent_dir = 'data_lake/'
    carpetas = ['landing', 'raw', 'cleansed', 'business']
    [os.mkdir(os.path.join(parent_dir, )) for c in carpetas]
    parent_dir = 'data_lake/business/'
    carpetas = ['reports', 'features', 'forecasts']

    os.mkdir(os.path.join(parent_dir, directory))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    create_data_lake()
