def load_data():
    import pandas as pd

    in_path = 'data_lake/business/features/Data_Prices.csv'
    data_pr = pd.read_csv(in_path, sep=",")
    return data_pr


def rev_data(data_pr):
    import pandas as pd

    df = data_pr.copy()
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df['year'], df['month'], df['day'] = df['date'].dt.year, df['date'].dt.month, df['date'].dt.day

    y = df["price"]
    x = df.copy()
    x.pop("price")
    x.pop("date")
    return x, y


def make_train_test_split(x, y):
    from sklearn.model_selection import train_test_split

    (x_train, x_test, y_train, y_test) = train_test_split(
        x,
        y,
        test_size=0.25,
        random_state=1017,
    )
    return x_train, x_test, y_train, y_test


def model_training(x_train, x_test):
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import RandomForestRegressor

    scaler = StandardScaler()
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)
    Rea_Model = RandomForestRegressor(n_jobs=-1)
    return Rea_Model


def save_model(Rea_Model):
    import pickle

    with open("src/models/Data_Price.pickle", "wb") as file:
        pickle.dump(Rea_Model, file,  pickle.HIGHEST_PROTOCOL)


def train_daily_model():
    data = load_data()
    x, y = rev_data(data)
    x_train, x_test, y_train, y_test = make_train_test_split(x, y)
    Rea_Model = model_training(x_train, x_test)
    save_model(Rea_Model)

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    train_daily_model()