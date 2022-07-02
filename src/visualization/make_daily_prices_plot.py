def make_daily_prices_plot():
    import pandas as pd
    df_m = pd.read_csv('data_lake/business/precios-diarios.csv', index_col=0)
    ax =df_m['precio'].plot(figsize=(15,5), kind='line', grid=True, x_compat=False)
    fig = ax.get_figure()
    fig.savefig('data_lake/business/reports/figures/daily_prices.png')
    print("Saved ---")

if __name__ == "__main__":
    import doctest
    make_daily_prices_plot()
    doctest.testmod()