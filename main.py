#importing the csv file into the python file
import csv

#for better visuals in the terminal
#from rich import print

import matplotlib.pyplot as plt

population_per_continent={}
# want the above created empty dic to look something like:
# population_per_container= {
# {africa: {population:[100, 200,300], years:[2000, 2001, 2002]},
# {asi: {population:[100, 200,300], years:[2000, 2001, 2002]},
# {europe: {population:[100, 200,300], years:[2000, 2001, 2002]}
# }
#so you can access data per continent

#extracting the info from csv with DictReader
filename= 'data.csv'
with open (filename, 'r') as csvfile:
    reader= csv.DictReader(csvfile)
    for line in reader:
        #print(line)
        year= int(line['year'])
        population= int(line['population'])
        continent= line['continent']
        #print(year)
        #print(population)
        #print(continent)
        if continent not in population_per_continent:
            population_per_continent[continent]= {'population':[], 'years':[]}
        
        population_per_continent[continent]['population'].append(population)
        population_per_continent[continent]['years'].append(year)
print(population_per_continent)
#this gives the dicttionary with layout now we can access

for continent in population_per_continent:
    print(continent)  
    years= population_per_continent[continent]['years'] 
    print(years)
    population=population_per_continent[continent]['population']
    plt.plot(years, population, label=continent, marker="o")

plt.legend()
plt.tight_layout()
plt.xlabel("Years")
plt.ylabel("Population")
plt.title("Number of Internet User per Continent through years")
plt.grid(True)

plt.show()


    