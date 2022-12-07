#! python3

# Importing necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import os

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
automobile_path = CURR_DIR_PATH + "/Automobile_data.csv"
automobile_cleaned_path = CURR_DIR_PATH + "/Automobile_data_cleaned.csv"


df = pd.read_csv(automobile_cleaned_path)

automobile_df = pd.read_csv(automobile_path)
print(automobile_df.to_string())

print(automobile_df.head(5))
print(automobile_df.tail(5))

automobile_df = pd.read_csv(
    automobile_path,
    na_values={
        'price': ["?", "n.a", "NaN"]
    }
)

automobile_df['price'] = automobile_df['price'].fillna(-1)

print(automobile_df.to_string())
automobile_df.to_csv(automobile_cleaned_path)

df = df[['company', 'price']][df.price == df['price'].max()]
print(df)


manufracturer = df.groupby('company')
toyata_df = manufracturer.get_group('toyota')
print(toyata_df)

brand_count = df['company'].value_counts()
print(brand_count)

manufracturer_price = df.groupby('company')
priceDF = manufracturer_price['price'].max()
print(priceDF)

manufracturer_avg_mile = df.groupby('company')
avg_mileDf = manufracturer_avg_mile['average-mileage'].mean()
print(avg_mileDf)

sortedDf = df.sort_values('price')
print(sortedDf)

car_price = {'Company': ['Toyota', 'Honda', 'BMV',
                         'Audi'], 'Price': [23845, 17995, 135925, 71400]}
car_priceDf = pd.DataFrame.from_dict(car_price)
car_horsepower = {'Company': ['Toyota', 'Honda',
                              'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]}
cars_horsepowerDf = pd.DataFrame.from_dict(car_horsepower)
car_price_horsepowerDf = pd.merge(car_priceDf, cars_horsepowerDf, on='Company')
print(car_price_horsepowerDf)

company_group = df.groupby('company')
max_price_df = company_group["company", "price"].max()

max_price_df.plot(kind="bar", x="company", y="price")
plt.show()
