#nap(1-7),eloadas(1-3),sor(1-25),szek(1-25)
def lekerdez(nap,terem,eloadas,sor,szek):
    foglalas=[]
    hely=((int(sor)-1) * 25) + (int(szek))
    ea=(((int(nap)-1)*3)+(int(eloadas)-1))
    print(hely)
    print(ea)
    with open("C:\git\PythonProject\Foglalas.txt","r",encoding="utf-8")as befile:
        for sor in befile:
            adat=sor.strip()
            foglalas.append(adat)        
    print(foglalas[0][624])    
    if   foglalas[ea][hely] == "F":
        return True
    elif foglalas[ea][hely] == "U":
        return False
    else:
        print("se F se U")


print(lekerdez (1,1,25,25))
