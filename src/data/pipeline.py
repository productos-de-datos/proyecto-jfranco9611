import luigi
from luigi import Task, LocalTarget

from src.data.transform_data import transform_data


class D_Ingest(Task):
    from ingest_data import ingest_data

    def output(saaelf):
        return LocalTarget('data_lake/landing/arc.csv')

    def run(self):
        with self.output().open('w') as files:
            ingest_data()


class D_Transform(Task):
    from transform_data import transform_data

    def requires(self):
        return D_Ingest()

    def output(self):
        return LocalTarget('data_lake/raw/arc.txt')

    def run(self):
        with self.output().open('w') as files:
            transform_data()


class D_Clear(Task):
    from clean_data import clean_data

    def requires(self):
        return D_Transform()

    def output(self):
        return LocalTarget('data_lake/cleansed/arc.txt')

    def run(self):
        with self.output().open('w') as files:
            clean_data()


class DPrice_Daily(Task):
    from compute_daily_prices import compute_daily_prices

    def requires(self):
        return D_Clear()

    def output(self):
        return LocalTarget('data_lake/business/arc.txt')

    def run(self):
        with self.output().open('w') as files:
            compute_daily_prices()


class DPrice_Montly(Task):
    from compute_monthly_prices import compute_monthly_prices

    def requires(self):
        return DPrice_Daily()

    def output(self):
        return LocalTarget('data_lake/business/arc.txt')

    def run(self):
        with self.output().open('w') as files:
            compute_monthly_prices()


if __name__ == '__main__':
    luigi.run(["DPrice_Montly", "--local-scheduler"])

if __name__ == "__main__":
    import doctest

    doctest.testmod()
