from math import *

x = int(input("Nombres de personnes à la soiréé : "))
y = int(input("Nombres de duos detestées (par groupe de 2) : "))
z = int((x*x-x)/2 - y)
print("Nombre de clapements : ", z)