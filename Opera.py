#Egy operaház 3 termének a foglalási rendszere
foglrendszer=[]
lista =[]
adat=[]
kelltxt=input("Készüljön foglalási file?(y/n)")
if kelltxt == "y":
    szek = 0
    eloadas = 0
    for eloadas in range(0,63,1):
    
        for szek in range(0,625,1):
                    
            lista.append("U") 
    lista.append("\n")           
    foglrendszer.append(lista)
    out = 0
    with open("C:\git\PythonProject\Foglalas.txt","w",encoding="utf-8") as kifile:
        for o in range(0,64,1):
            print(out)
            kifile.writelines(foglrendszer[o])
            
else:
        with open("C:\git\PythonProject\Foglalas.txt","r",encoding="utf-8")as befile:
            for i in range(0,63,1):
                adat=i.strip("\n")
                foglrendszer.append(adat)

