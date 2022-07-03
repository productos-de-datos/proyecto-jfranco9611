## Este documento crea la estructura del data lake para la coherción de todos los archivos
## la estructura de este mismo se encuentra denotada en el comentario de la defición





def create_data_lake():
    """Cree el data lake con sus capas.


    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```
    """
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



