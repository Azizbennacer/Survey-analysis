import pandas as pd
import matplotlib.pyplot as plt
def load_data():
    df = pd.read_csv("C:\\Users\\Mega Pc\\OneDrive\\Desktop\\Survey mini project\\data\\Survey about marriage.csv")
    print(df)
    return df

def data_taste(df):
    return(df.head())