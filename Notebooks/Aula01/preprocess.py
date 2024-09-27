#!/bin/python3

import pandas as pd


class Preprocess:

    datasource_path: str = ...
    data = pd.DataFrame()

    def __init__(self, datasource_path) -> None:
        if not datasource_path:
            raise Exception("Datasource path not found")

        self.datasource_path = datasource_path
        self.load_data()

    def load_data(self, sourcetype: str = "scv") -> None:
        try:
            self.data = pd.read_csv(self.datasource_path)
        except Exception as e:
            raise e

    def clean(self, cols_to_delete: list) -> None:
        data = self.data
        # manual delete: when fields has not relevant
        if len(cols_to_delete) > 0:
            print(f"Deleting {len(cols_to_delete)} col(s): {cols_to_delete}")
            data.drop(columns=cols_to_delete, axis=1, inplace=True)

        # errors and inconsistencies

        # del duplicates
        duplicates = data.duplicated().sum()
        print(f"The dataset have {duplicates} duplicated row(s)")
        if duplicates > 0:
            data.drop_duplicates(inplace=True)
            print("Duplicates has been removed.")
        else:
            print("Nothing to do.")

        # missing values
        mv = data.isna().sum().sum()
        if mv > 0:
            for col in data.columns:
                if data[col].isna().sum() > 0 and data[col].dtypes != "object":
                    col_median = data[col].median()
                    data[col].fillna(col_median, inplace=True)
                elif data[col].isna().sum() > 0 and data[col].dtypes == "object":
                    col_mode = data[col].mode()
                    data[col].fillna(col_mode, inplace=True)
        else:
            print("No NaN values in dataframe")

        assert (
            data.isna().sum().sum()
        ) == 0, "MISSING VALUES PERSISIT AFTER PREPROCESS"

        # integrity

        # validation

        self.data = data
        pass

    def balance(self) -> None:
        pass

    def transform(sefl) -> None:
        pass

    def split_data(self) -> None:
        pass

    def reduction(self) -> None:
        pass
