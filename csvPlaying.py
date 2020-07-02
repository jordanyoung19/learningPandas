# working with csv files using pandas
import pandas as pd

df = pd.read_csv("Sacramentorealestatetransactions.csv")

'''
print(df.head())
print(df.describe())
'''

df['expensive'] = df['price'] > 150000
print(df.head())