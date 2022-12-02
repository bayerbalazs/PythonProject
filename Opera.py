#Egy operaház 3 termének a foglalási rendszere egy hétre
foglrendszer=[]
lista =[]
adat=[]
kelltxt=input("Készüljön új foglalási file?(y/n)")
napok=int(input("Kérlek add meg a foglalás napját.(1-7)"))
termek=int(input("Kérlek add meg a foglalás termét.(1-3)"))
eloadasok=int(input("Kérlek add meg a foglalás előadását.(1-3)"))
sorok=int(input("Kérlek add meg a foglalás sorát.(1-25)"))
szekek=int(input("Kérlek add meg a foglalás székét.(1-25)"))

if kelltxt == "y":
    szek = 0
    eloadas = 0
    with open("C:\git\PythonProject\Foglalas.txt","w",encoding="utf-8") as kifile:
        for eloadas in range(0,63,1):    
            for szek in range(0,625,1):                    
                lista.append("U") 
            lista.append("\n")           
        kifile.writelines(lista)         
            
else:
        with open("C:\git\PythonProject\Foglalas.txt","r",encoding="utf-8")as befile:
            for sor in befile:
                adat=sor.strip()
                foglrendszer.append(adat)

def lekerdezszeket(nap,terem,eloadas,sor,szek):
    foglalas=[]
    nap1=(int(nap)-1)*9
    terem1=(int(terem)-1)*3
    eloadas1=int(eloadas)-1
    sor1=int(sor)-1
    szek1=int(szek)-1
    hely=(sor1 * 25) + szek1
    ea=(nap1)+(eloadas1)+(terem1)
    
    with open("C:\git\PythonProject\Foglalas.txt","r",encoding="utf-8")as befile:
        for sor in befile:
            adat=sor.strip()
            foglalas.append(adat)  
     
    if   foglalas[ea][hely] == "F":
        return True
    elif foglalas[ea][hely] == "U":
        return False
    else:
        print("se F se U")

def foglalszeket(nap,terem,eloadas,sor,szek):
    foglalas=[]
    nap1=(int(nap)-1)*9
    terem1=(int(terem)-1)*3
    eloadas1=int(eloadas)-1
    sor1=int(sor)-1
    szek1=int(szek)-1
    hely=(sor1 * 25) + szek1
    ea=(nap1)+(eloadas1)+(terem1)
    
    with open("C:\git\PythonProject\Foglalas.txt","r",encoding="utf-8")as befile:
        for sor in befile:
            adat=sor.strip()
            foglalas.append(adat)  
     
    if   foglalas[ea][hely] == "U":        
         foglalas[ea].insert(hely,"F")
         return True

    elif foglalas[ea][hely] == "F": 
        return False
    else:
        print("se F se U")

foglalszeket(napok,termek,eloadasok,sorok,szekek)