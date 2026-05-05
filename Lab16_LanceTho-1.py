"""
Lab16_LanceTho-1.py
Lance Thongsavanh
Write a program that reads the OHRU.csv file, which contains Ohio's unemployment rate since 1976. You will parse this data and create a time-series line plot using matplotlib.
5/5/2026
"""

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

def process_data() -> tuple:
    """Processes data from a csv file

    Returns:
        tuple: a tuple of lists of certain data
    """
    path = Path("OHUR.csv")
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    dates: list = []
    unemp_rates: list[float] = []

    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            rate = float(row[1])
        except ValueError as e:
            print(date)
        else:
            dates.append(date)
            unemp_rates.append(rate)
    
    return dates, unemp_rates

def graph_data() -> None:
    """Graphs the data gathered from calling the process_data() function and saves it as an image
    """
    dates, unemp_rates = process_data()

    figure, graph = plt.subplots()

    graph.plot(dates, unemp_rates, color="blue")

    graph.set_title("Ohio Unemployment (by Month): 1976 - 2022")
    graph.set_ylabel("Unemp Rate")
    graph.set_xlabel("Date")
    figure.autofmt_xdate()

    plt.savefig("ohio_unemployment.png")

if __name__ == "__main__":
    graph_data()