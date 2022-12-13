import pandas as pd
import os

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(df)


df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue':
                  ['Pretty good.', 'Bland.']})
print(df)

s = pd.Series([1, 2, 3, 4, 5])
print(s)

s = pd.Series([30, 35, 40.], index=['2015 Sales',
              '2016 Sales', '2017 Sales'], name='Product A')
print(s)

wine_reviews = pd.read_csv(f"{CURR_DIR_PATH}/data/winemag-data-130k-v2.csv")

print(wine_reviews.shape)
print(wine_reviews.head())
