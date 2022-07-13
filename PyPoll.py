# Adding dependencies
import csv
import os
from wsgiref import headers

# File to load variable
file_to_load = os.path.join('Resources', 'election_results.csv')

# File to save variable
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Open election results and read file
with open(file_to_load, encoding='UTF-8') as election_data:

# Read the file obj w/ the reader function
    file_reader = csv.reader(election_data)

#Print the header row
    headers = next(file_reader)
#Print header row
    print(headers)

#Total number of votes cast

#A complete list of candidates who received votes

#Total number of votes each candidate received

#Percentage of votes each candidate won

#The winner of the election based on popular vote

# Close file





