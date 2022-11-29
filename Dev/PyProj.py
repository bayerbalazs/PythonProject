import random
foglrendszer=[]
eloadas =[]
lista=[]
szek=0
for eloadas in range(0,3,1):
    for szek in range(0,625,1) :
        i = random.randrange(0,2)
        if i == 0 :
            j = "F"
        elif i == 1:
            j = "U"
        else:
            print("valami error")        
        lista.append(j)
        szek = szek + 1 
        foglrendszer.append(lista)
print (foglrendszer)
with open("C:\git\PythonProject\egynapfogl.txt","w",encoding="utf-8") as kifile:
    for eloadas in range(len(foglrendszer)):
        kifile.writelines(foglrendszer[eloadas])
with open ("C:\git\PythonProject\egynapfogl.txt","r",encoding="utf-8") as befile:
        
        for szek in range(len(befile):            
            befile.readlines(foglrendszer[eloadas])

        fogl = foglrendszer.count("F")
        ures = foglrendszer.count("U")
        sum = fogl + ures
print (lista)
print (fogl)  
print (ures)
print (sum)   



        
        
  






