# Parses filenames in the specified directory, saves them to a CSV file
import os, csv, sys

# Path where the .csv is saved e.g. C:/foobar.csv
f = open("/path/here",'r+', newline='', encoding="utf-8")
# Instantiates the CSV Writer
w = csv.writer(f)
# Inserts column names in the first row
w.writerow(('FileName', 'DirName'))
# Path to parse files from
for path, dirs, files in os.walk("I:/"):
    for filename in files:
        dir_path = os.path.dirname(os.path.abspath(filename))
        w.writerow([filename, path[2:]])