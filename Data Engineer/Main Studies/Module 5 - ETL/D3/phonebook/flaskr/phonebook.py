from sqlalchemy import create_engine  # sql driver
from datetime import date
import pandas as pd


class SQLWriter:
    def __init__(self, db_path):
        print("sqlite://" + db_path)
        self.engine = create_engine("sqlite:///" + db_path)  # local sqlite

    def get_data(self, dbname):
        if not (self.engine.has_table(dbname)):
            return []
        return pd.read_sql(dbname, self.engine, columns=["name", "number", "address", "added"])

    def write_to(self, dbname, df):
        df.to_sql(dbname, self.engine, if_exists="replace")


class Phonebook:
    def __init__(self, db_path):
        self.sql = SQLWriter(db_path)
        self.data = []

    def get_data(self):
        if len(self.data) == 0:
            self.data = self.sql.get_data("phonebook")

        return self.data

    def write_to(self, entry):
        self.data = self.get_data().append(entry, ignore_index=True)

    def save_all_updates(self):
        self.sql.write_to("phonebook", self.data)

    def get_all(self):
        return self.get_data().to_json(orient="records")

    def get_by_name(self, name):
        df = self.get_data()
        return df[df["name"].str.contains(name)].to_json(orient="records")

    def get_rows(self, rows):
        df = self.get_data()
        df = df.head(int(rows))
        return df.to_json(orient="records")

    def get_by_address(self, address):
        df = self.get_data()
        return df[df['address'].str.contains(address)].to_json(orient="records")

    def add(self, entry):
        from datetime import date
        today = date.today()
        if entry['added'] < str(today):
            entry['added'] = today
        self.write_to(entry)

    def delete_by_name(self, full_name):

        self.data = self.get_data()

        self.data.drop(
            index=self.data[(self.data.name == full_name)].index, inplace=True)
        self.save_all_updates()

        return "Entry deleted"

    def get_by_date(self, start, end):
        df = self.get_data()
        df = df.loc[df['added'].between(start, end)]

        return df.to_json(orient="records")

        """
        df = df['added'] = pd.to_datetime(df['added'])

        mask = (df['added'] >= start_month) & (df['added'] <= end_month)

        return df.loc[mask].to_json(orient="records")
        """
