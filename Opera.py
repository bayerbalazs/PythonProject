#Egy operaház 3 termének a foglalási rendszere
foglrendszer=[]
lista =[]
adat=[]
kelltxt=input("Készüljön új foglalási file?(y/n)")
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

def lekerdez(nap,terem,eloadas,sor,szek):
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