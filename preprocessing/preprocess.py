import pandas as pd 
def load_and_clean(file):
    df = pd.read_csv(file)
    df = df.dropna()
    print("Data loaded and cleaned successfully")
    return df