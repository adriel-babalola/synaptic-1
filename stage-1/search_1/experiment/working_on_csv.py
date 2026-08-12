import csv
import os

project_dir = os.path.dirname(__file__)
data_path = os.path.join(project_dir, "output", "info.csv")

title=["Name","Country", "Email"]

data_to_append = [
    title,
    ["janet", "USA", "her@gmail.com"],
    ["dude", "Nigeria", "dude@gmail.com"]
]

file = open(data_path, "a", newline="")
writer = csv.writer(file)

writer.writerows(data_to_append)

file.close() 