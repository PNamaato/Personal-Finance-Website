# Handles data storage and retrieval (could be CSV, SQLite, etc.)

import pandas as pd

def load_data(file_name):
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        return pd.DataFrame()

def save_data(df, file_name):
    df.to_csv(file_name, index=False)
