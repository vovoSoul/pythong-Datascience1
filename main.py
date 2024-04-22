#importing the csv file into the python file
import csv

#for better visuals in the terminal
from rich import print

import matplotlib.pyplot as plt

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
        
    
plt.plot([2001,2002,2003, 2004], [20, 40, 60, 90], label="africa", marker="o")
plt.plot([2001, 2002, 2003, 2004], [20, 50, 100, 200], label="asia", marker="o")
plt.legend()
plt.tight_layout()
plt.xlabel("Years")
plt.ylabel("Population")
plt.title("Number of Internet User per Continent through years")
plt.grid(True)

plt.show()
    