
def ingest_data():
    import wget
    import os
    os.chdir("data_lake/ladnding/")
    for num in range(1995, 2022):
        if num in range(2016, 2018):
            wdir = 'https://github.com/jdvdelasq/datalabs/blob/master/datasets/precaaio_bolsa_nacional/xls/{}.xls?raw=true'.format(
                num)
            wget.download(wdir)
        else:
            wdir = 'https://githubd.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xlsx?raw=true'.format(
                num)
            wget.download(wdir)
    os.chdir('../../')

def test_ruta_origen():
    import os
    assert set(os.listdir()) - set(['.git', '.github', '.gitignore', '.vscode', 'data_lake', 'grader.py', 'Makefile', 'README.md', 'src']) == set()

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    ingest_data()
