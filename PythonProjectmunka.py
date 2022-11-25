import random
Hetfo_DE =[]
szek=0
for szek in range(0,624,1) :
    i = random.randrange(0,2)
    Hetfo_DE.append(i)
    szek = szek + 1 

print (Hetfo_DE)
with open("Pproject.txt","r",encoding="utf-8") as kifile:
    kifile.writelines(Hetfo_DE)
