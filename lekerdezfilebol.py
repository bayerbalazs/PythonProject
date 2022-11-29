#nap(1-7),terem(1-3),eloadas(1-3),sor(1-25),szek(1-25)
def lekerdez(nap,terem,eloadas,sor,szek):
    foglalas=[]
    nap1=(int(nap)-1)*9
    terem1=int(terem)-1
    eloadas1=int(eloadas)-1
    sor1=int(sor)-1
    szek1=int(szek)-1
    hely=(sor1 * 25) + szek1
    ea=(nap1)+(eloadas1)+(terem1)
    print(ea)
    print(hely)
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


print(lekerdez (7,3,3,25,25))
