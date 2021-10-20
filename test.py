import random
a = 1
b = 2
c = 3

liste = [a,b,c,4,5,6]

def hei(a,b):
    return a > b

print(hei(a,b))
print(liste[:3])
print(liste[-3:])
ny_liste = liste.clear()
print(ny_liste)
print(liste)


print(random.randint(0,1))