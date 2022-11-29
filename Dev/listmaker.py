import random
foglrendszer=[]

lista =[]
szek= 0
eloadas = 0
for eloadas in range(0,64,1):
    
    for szek in range(0,624,1):
        i = 1
        if i == 0 :
            j = "F"
        elif i == 1:
            j = "U"
        else:
            print("valami error")              
        lista.append(j) 
    lista.append("\n")           
    foglrendszer.append(lista)
    lista=[]    
print(eloadas,len(lista))
    


a = len(lista)
print(foglrendszer[0])
print(foglrendszer[1])
print(foglrendszer[20])
with open("C:\git\PythonProject\Foglalas.txt","w",encoding="utf-8") as kifile:
    for out in range(0,64,1):
        kifile.writelines(foglrendszer[out])
        print(out)