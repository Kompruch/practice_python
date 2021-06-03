import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# test = np.array([[1,2,3,4],[2,9,3,5]])

# # test_plus = test + 2

# # test_loc = test[0,:]

# mean_test = np.mean(test, axis = 1)

# print(mean_test)

# print(test_plus)

df = pd.read_csv('/Users/ice_macbookair/Desktop/Ice Data engineer/practice_python/pandaspractice/pandas_for_everyone_master/data/gapminder.tsv', sep='\t')
# print(df.head())

# print(type(df))

# print(df.shape)

# print(df.columns)

# print(df.dtypes)

# print(df.info())

# print(df['country'])

# print(df.iloc[0])
# print(df.iloc[:20,0:3])
# subset = df.loc[:,['country','continent']]
# print(subset)

# print(df.loc[[0, 99, 999]])
# print(df.iloc[:, 0:6:])
# print(df.iloc[:, 0::2])
# print(df.iloc[:, :6:2])
# print(df.iloc[:, ::])

# a, b, c = df.loc[:,['lifeExp', 'pop', 'gdpPercap']].mean()
# # print(round(df_mean,2))
# b = round(b,2)
# print(a,"population: {:,}".format(b),c)

# g_con = df.groupby(['year', 'continent'])['lifeExp', 'pop', 'gdpPercap'].mean()
# print(round(g_con,2))

# df_flat = g_con.reset_index()
# print(df_flat.head(10))

# new_df = df.groupby('continent')['country'].nunique()
# new_df1 = df.groupby('continent')['country'].value_counts()
# print(new_df1)

# df2 = df.country.value_counts()
# print(df2)

year_life_exp = df.groupby('year')['lifeExp'].mean()
print(year_life_exp)

year_life_exp.plot()

plt.show()