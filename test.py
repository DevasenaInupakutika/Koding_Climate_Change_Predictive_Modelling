import csv
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas

df = pd.read_csv('Total_Carbon_Dioxide_Emissions.csv')
print df

with open('Total_Carbon_Dioxide_Emissions.csv', 'rU') as f:
    reader = csv.reader(f)
    
    with open('Total_Carbon_Dioxide_Emissions_new.csv',mode='w') as outfile:
        writer = csv.writer(outfile)
       
        mydict = {row[0]:row[1:31] for row in reader}
        
#print mydict.keys()
#print len(mydict.keys())

mydict.values()
#print len(mydict.values())

#print mydict["Canada"]
#mydict = dict((float(k), map(float, v)) for k, v in mydict.iteritems())

xs, ys=zip(*((x, k) for k in mydict for x in mydict[k]))
#xl = [1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]

#plt.plot(xs,ys,'ro')
#plt.show()

#plt.figure()
df.plot()
plt.savefig('Emissions_plot.png')
