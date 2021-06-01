from numpy import dtype
import pandas as pd

df = pd.read_csv('/Users/ice_macbookair/Desktop/Ice Data engineer/practice_python/pandaspractice/pandas_for_everyone_master/data/gapminder.tsv', sep='\t')
print(df.head())

print(type(df))

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.info())

print(df['country'])

print(df.iloc[1])