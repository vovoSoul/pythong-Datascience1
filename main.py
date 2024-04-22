#importing the csv file into the python file
import csv

#for better visuals in the terminal
from rich import print

#import matplotlib.pyplot as plt

#extracting the info from csv with DictReader
filename= 'data.csv'
with open (filename, 'r') as csvfile:
    reader= csv.DictReader(csvfile)
    for line in reader:
        #print(line)
        year= line['year']
        population= line['population']
        continent= line['continent']
        print(year)
        print(population)
        print(continent)




        