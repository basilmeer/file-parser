# Parses filenames in the specified directory, saves them to a CSV file
import os, csv, sys

# Change the path of the file to save in the CSV data
f = open("K:/Programming/Python/names.csv",'r+', newline='', encoding="utf-8")
# Instantiates the CSV Writer
w = csv.writer(f)
# Inserts column names in the first row
w.writerow(('FileName', 'DirName'))
# Write the path of the parent directory to scrap the data out from
for path, dirs, files in os.walk("I:/"):
    for filename in files:
        dir_path = os.path.dirname(os.path.abspath(filename))
        w.writerow([filename, path[2:]])