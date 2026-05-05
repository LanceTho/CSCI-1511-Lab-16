"""
Lab16_LanceTho-1.py
Lance Thongsavanh
Write a program that reads the OHRU.csv file, which contains Ohio's unemployment rate since 1976. You will parse this data and create a time-series line plot using matplotlib.
Date.
"""
from pathlib import Path
import csv
import matplotlib.pyplot as plt
import datetime

path = Path("OHUR.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, col_title in enumerate(header_row):
#     print(f"{index} {col_title}, ", end=" ")
# print()

dates: list = []
unemp_rates: list[float] = []

for row in reader:
    date = row[0]
    rate = float(row[1])
    dates.append(date)
    unemp_rates.append(rate)

figure, graph = plt.subplots()

graph.plot(unemp_rates)
plt.show()
"""
Requirements:
You must import matplotlib.pyplot as plt, csv, and datetime.
You must use the provided OHUR.csv file.
Use a try-except block to gracefully handle any data conversion errors.
Use the csv module to read the file. Use enumerate() to read and analyze the header row.
Read the dates and unemployment rates into two separate lists.
You must use the datetime class to convert the date strings from the CSV into datetime objects for plotting.
The plot must have a title (e.g., "Ohio Unemployment (by Month): 1976 - 2022") and appropriate axis labels ("Date" and "Unemp Rate").
Your script must save the final plot to an image file (e.g., ohio_unemployment.png).
The generated plot image must be added to your repository.
"""
