from math import *

x = int(input("Nombres de personnes à la soiréé : "))
nb = int(input("Combien de personnes détestent d'autres personnes : "))
round = 1
y = 0
while nb >= 1:
    y = y + int(input(f"Nombre de personnes detestés par la personne {round} : "))
    round = round + 1
    nb = nb - 1
z = int((x*x-x)/2 - y)
print("Nombre de clapements : ", z)
