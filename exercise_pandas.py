import pandas as pd

#1. A CSV file (Comma-Separated Values) is a plain text file that stores 
# data (data in rows and columns) in a simple format.

cars = pd.read_csv("cars_data.csv")

# 1. Print first 10 rows 
print(cars.head(10))

# 2. Print last 5 rows
print(cars.tail(5))

# 3. check how many non-null rows each column has
cars.info()

# 4. drop the entire row if any column has a missing value,
cars_cleaned = cars.dropna()

# 5. Calculate the mean of each numeric column
print(cars.mean(numeric_only=True))

# 6. Select the rows where the column "company" is equal to 'honda'
honda_cars = cars[cars['company'] == 'honda']
print(honda_cars)

# 7. Sort the data set by price in descending order 
cars_sorted_by_price = cars.sort_values(by='price', ascending=False)
print(cars_sorted_by_price)

# 8. Select the rows where the column "company" is equal to any of the values (audi, bmw, porsche)
selected_companies = cars[cars['company'].isin(['audi', 'bmw', 'porsche'])]
print(selected_companies)

# 9. Find the number of cars (rows) for each company
company_car_counts = cars['company'].value_counts()
print(company_car_counts)

# 10. Find the maximum price for each company
max_price_per_company = cars.groupby('company')['price'].max()
print(max_price_per_company)