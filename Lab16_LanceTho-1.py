"""
Lab16_LanceTho-1.py
Lance Thongsavanh
Write a program that reads the OHRU.csv file, which contains Ohio's unemployment rate since 1976. You will parse this data and create a time-series line plot using matplotlib.
Date.
"""

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
