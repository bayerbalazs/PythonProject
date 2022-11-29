def lekerdez(nap,sor,szek):
    foglalas=[]
    hely=(int(sor) * 25) + int(szek)
    eloadas=(int(nap))
    print(hely)
    print(eloadas)
    print(True)
    print(False)
    with open("C:\git\PythonProject\Foglalas.txt","r",encoding="utf-8")as befile:
        for sor in befile:
            adat=sor.strip()
            foglalas.append(adat)
    print (foglalas[0])
    print (foglalas[1])
    print (foglalas[2])        
        
    if foglalas[eloadas][hely] == "U":
        return False
    else :
        return True

lekerdez (0,1,1)
