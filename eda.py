import pandas as pd 
import matplotlib.pyplot as plt 

def eda(file):
    df = pd.read_csv(file)
    print("First 5 rows:\n", df.head())
    print("\nSummary:\n", df.describe())
    df.hist()
    plt.show()