import random
foglrendszer=[]

lista =[]
szek= 0
eloadas = 0
for eloadas in range(0,21,1):
    for szek in range(0,625,1):
        i = random.randrange(0,2)
        if i == 0 :
            j = "F"
        elif i == 1:
            j = "U"
        else:
            print("valami error")              
        lista.append(j)
    print(eloadas,len(lista))
    foglrendszer.append(lista)

a = len(lista)
print(a)
with open("C:\git\PythonProject\Foglalas.txt","w",encoding="utf-8") as kifile:
    for eloadas in range(len(foglrendszer)):
        kifile.writelines(foglrendszer[eloadas])
with open("C:\git\PythonProject\Foglalas.txt","w",encoding="utf-8") as be:
    print(foglrendszer[0])        
    print(foglrendszer[1])
    print(foglrendszer[2])
    print(foglrendszer[3])
    print(foglrendszer[4])
    print(foglrendszer[5])
    print(foglrendszer[6])
    print(foglrendszer[7])
    print(foglrendszer[8])
    print(foglrendszer[9])
    print(foglrendszer[10])
    print(foglrendszer[11])
    print(foglrendszer[12])
    print(foglrendszer[13])
    print(foglrendszer[14])
    print(foglrendszer[15])
    print(foglrendszer[16])
    print(foglrendszer[17])
    print(foglrendszer[18])
    print(foglrendszer[19])
    print(foglrendszer[20])




        
        
  






