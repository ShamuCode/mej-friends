# Created by ShamuLC (ShamuCode)

from math import *

x = int(input("Number of people at the party: "))
nb = int(input("How many people hate other people: "))
round = 1
y = 0
while nb >= 1:
    y = y + int(input(f"Number of people hated by person {round}: "))
    round = round + 1
    nb = nb - 1
z = int((x * (x - 1)) / 2 - y)
print("Number of claps: ", z)
