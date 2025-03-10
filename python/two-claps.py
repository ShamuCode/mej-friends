# Created by ShamuLC (ShamuCode)

from math import *

x = int(input("Number of persons at the party: "))
y = int(input("Number of claps for each person: "))
result = int(((x*(x-1))/2)*y)
print("Number of claps: ", result)
