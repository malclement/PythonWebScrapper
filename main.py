"""Selenium Web Scrapping Script"""
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


### Configuration
URL = "https://www.numbeo.com/quality-of-life/rankings_by_country.jsp?title=2014&region=150"
NUMBER_OF_COLUMNS = 10
CSV_PATH = "table_data.csv"
HEADER_TITLES = [
    "Country",
    "Quality of Life Index",
    "Purchasing Power Index",
    "Safety Index",
    "Health Care Index",
    "Cost of Living Index",
    "Property Price to Income Ratio",
    "Traffic Commute Time Index",
    "Pollution Index",
    "Climate Index"
]
START_COLUMN = 1
END_COLUMN = -1
TABLE_ID = "t2"



driver = webdriver.Chrome()
data = []

driver.get(URL)

# Find the table
table = driver.find_element(By.ID, TABLE_ID)

# Find all rows in the table body
rows = table.find_elements(By.XPATH, ".//tbody/tr")

for row in rows:
    # Initialize an empty list to store the data
    row_values = []

    # Iterate through the rows and extract data
    table_row = row.find_elements(By.XPATH, ".//td")

    for cell in table_row[START_COLUMN:END_COLUMN]:
        # Extract text from each cell and append it to the data list
        row_values.append(cell.text)
    
    data.append(row_values)

driver.quit()

# Write the data to the CSV file
with open(CSV_PATH, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write header row if needed (replace 'header' with your actual header row)
    writer.writerow(HEADER_TITLES)

    # Write the data rows
    writer.writerows(data)

print(f"Data has been scraped and saved to {CSV_PATH}.")
