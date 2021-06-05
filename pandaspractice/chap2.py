from numpy import column_stack
import pandas as pd

# s = pd.Series(['banana', 42])
# print(s)

# m = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person','Who'])
# print(m)

# print(m.loc[['Person','Who']])


scientists = pd.DataFrame({'Name': ['Rosaline Franklin', 'William Gosset'], 
                            'Occupation': ['Chemist', 'Statistician'], 
                            'Born': ['1920-07-25','1876-06-13'], 
                            'Age':[37, 61]})

# print(scientists)

# scientists2 = pd.DataFrame({'Occupation': ['Chemist', 'Statistician'], 
#                             'Born': ['1920-07-25','1876-06-13'], 
#                             'Age':[37, 61]}, 
#                             index=['Rosaline Franklin', 'William Gosset'],
#                             columns=['Occupation','Born','Age'])

# first_row = scientists2.loc['William Gosset']
# print(first_row.index)
# print(first_row.values)

# ages = scientists2['Age']
# print(ages.mean())
# print(ages.median())
# print(ages.min())
# print(ages.quantile(0.25))

scientists = pd.read_csv('/Users/ice_macbookair/Desktop/Ice Data engineer/practice_python/pandaspractice/pandas_for_everyone_master/data/scientists.csv')
# print(scientists.head())
# print(scientists.info())
ages = scientists.Age
print(ages.mean())
# print(scientists.describe())