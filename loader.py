from data.framer import csvframer
from time import sleep

folder = "historical/sets/"
with open("historical/LOADER.csv") as f:
    for ticker in f:
        print("Loading:", ticker)
        csvframer(ticker[:-1], folder)
        print("Loaded!")
        print("Time-out: 12 (s)")
        sleep(12)
