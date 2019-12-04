# This is file read/write module of assignment 3
import csv

# Read a file
def file_reader(file_name):
    with open(file_name) as dirty_csv_file:
        dirty_reader = csv.reader(dirty_csv_file, quoting=csv.QUOTE_NONE)
        for dirty_list in dirty_reader:
            pass
    return dirty_list

# Write a file
def file_writer(file_name, list):
    with open(file_name, "w", newline = "") as csv_file:
        clean_writer = csv.writer(csv_file)
        clean_writer.writerow(list)



