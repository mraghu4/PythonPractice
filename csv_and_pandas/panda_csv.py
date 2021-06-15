import pandas as pd


def display(file_name):
    fd = pd.read_csv(file_name)
    print(fd.to_string())

def sort():
    fd = pd.read_csv("./price.csv")
    softed_csv = fd.sort_values(by=['Series reference'])
    softed_csv.to_csv("./price_sorted.csv")
    print(softed_csv)

display("./price.csv")
sort()
display("./price_sorted.csv")

