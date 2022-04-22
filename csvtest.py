import pandas as pd
import math 

A = pd.read_csv('destinations.csv', header=None)
fieldnames = ['destinationCode', 'normalName','destcoords1','destcoords2']

#coords to test
coords1 = -955145765
coords2 = 296942771

coord1vals = []
coord2vals = []
lengths = []
smallestDistance = 9999999999999

for x in A.values:
    coord1vals.append(int(x[int(fieldnames.index("destcoords1"))]))
    coord2vals.append(int(x[int(fieldnames.index("destcoords2"))]))

for i in range(len(coord1vals)):
    lengths.append(math.sqrt(math.pow(((int(coord1vals[i]))-(coords1)),2) + math.pow(((int(coord2vals[i]))-(coords2)),2)))

lengthsToSort = []

for i in lengths:
    lengthsToSort.append(i)

lengthsToSort.sort()
print(A.values[lengths.index(lengthsToSort[0])][int(fieldnames.index("normalName"))])

    