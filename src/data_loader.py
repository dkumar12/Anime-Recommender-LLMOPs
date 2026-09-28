import pandas as pd

class AnimieDataLoader:
    def __init__(self,original_csv:str,processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        df = pd.read_csv(self.original_csv, encoding='utf-8',on_bad_lines="skip").dropna()

        required_columns = {"Name","Genres","sypnopsis"}
        missing = required_columns - set(df.columns)
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

        df['combined_column'] = (
            "Title: "+df["Name"]+" Overview: "+df["sypnopsis"]+" Genres: "+df["Genres"]
        )

        df[['combined_column']].to_csv(self.processed_csv, index=False, encoding='utf-8')

        return self.processed_csv