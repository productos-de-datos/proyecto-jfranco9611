def make_forecasts():
    from train_daily_model import train_daily_model, load_data, rev_data, make_train_test_split

## Se crean la primera función
    def pkl_loading():
        import pickle
        with open("src/models/precios-diarios.pickle", "rb") as file:
            Rea_Model = pickle.load(file)
        return Rea_Model

## Se generan los estimadores
    def score(x_train, y_train):
        import numpy as np

        estimators = np.arange(10, 200, 10)
        scores = []
        for n in estimators:
            Rea_Model.set_params(n_estimators=n)
            Rea_Model.fit(x_train, y_train)
            scores.append(Rea_Model.score(x_test, y_test))
        return scores

## Se busca el mejor estimador
    def best_score(scores):
        import pandas as pd
        
        Bestim = pd.DataFrame(scores)
        Bestim.reset_index(inplace=True)
        Bestim = Bestim.rename(columns={0: 'scores'})
        Bestim = Bestim[Bestim['scores'] == Bestim['scores'].max()]
        Bestim['index'] = (Bestim['index']+1)*10
        Bestim = Bestim['index'].iloc[0]
        return Bestim

## Se busca el mejor estimador
    def btrain_estimator(Bestim):
        from sklearn.ensemble import RandomForestRegressor

        Rea_Model = RandomForestRegressor(n_estimators=Bestim, random_state=1017)
        Rea_Model.fit(x_train, y_train)
        return Rea_Model

## Se testea la predicción del modelo
    def prediction_test(Rea_Model):
        yp_test = Rea_Model.predict(x_test)
        return yp_test

## se realiza el pronostico
    def forecasts(yp_test, y_test, data):
        import pandas as pd
        import numpy as np

        df_Rea_Model = pd.DataFrame(y_test).reset_index(drop=True)
        df_Rea_Model['pronostico'] = yp_test
        np.random.seed(0)

        df_series = pd.Series(y_test)
        df_series = df_series.to_frame()
        df_series.reset_index(inplace=True)
        df_series = df_series[['index']]

        df_Rea_Model = pd.concat([df_Rea_Model, df_series], axis=1)
        data = data[['date']]
        data.reset_index(inplace=True)

        df_Rea_Model = pd.merge(df_Rea_Model, data, on='index', how='left')
        df_Rea_Model = df_Rea_Model[['date', 'price', 'pronostico']]
        return df_Rea_Model

## Se convierten los pronosticos
    def save_forecasts(df_Rea_Model):
        df_Rea_Model.to_csv('data_lake/business/forecasts/Data_Prices.csv', index=None)


## Ejecución del proceso
    data = load_data()
    x, y = rev_data(data)
    x_train, x_test, y_train, y_test = make_train_test_split(x, y)
    Rea_Model = pkl_loading()
    scores = score(x_train, y_train)
    Bestim = best_score(scores)
    Rea_Model = btrain_estimator(Bestim)
    yp_test = prediction_test(Rea_Model)
    df_Rea_Model = forecasts(yp_test, y_test, data)
    save_forecasts(df_Rea_Model)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_forecasts()