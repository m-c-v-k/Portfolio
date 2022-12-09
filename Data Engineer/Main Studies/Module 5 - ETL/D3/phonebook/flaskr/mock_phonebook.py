import flaskr.data as data
from faker import Faker
import pandas as pd
from datetime import date

Faker.seed(0)
fake = Faker()

def format_date(date):
  return date.strftime("%y-%m-%d")

def initialize_mock(phonebook, size=10):
  names = data.generate(
    title=f"Loading {size} names",
    size=size,
    method=fake.name
  )

  numbers = data.generate(
    title=f"Loading {size} phone numbers",
    size=size,
    method=fake.phone_number
  )

  adress = data.generate(
    title=f"Loading {size} addresses",
    size=size,
    method=fake.address
  )

  dates = data.generate(
    title=f"Loading {size} dates",
    size=size,
    method=fake.date_time_between,
    start_date=date(2022, 6, 1),
    end_date=date(2022, 7, 10)
  )
  print(dates)

  dates = data.map(
    title=f"Transforming {size} dates to format Y/M/d",
    data=dates,
    method=format_date
  )
  print(dates)

  columns = ["name", "number", "address", "added"]
  phone_data = zip(names, numbers, adress, dates)

  df = pd.DataFrame(phone_data, columns=columns)
  phonebook.sql.write_to("phonebook", df)
