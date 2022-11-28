def lekerdez(nap,sor,szek):
    foglalas=[]
    hely=(int(sor) * 25) + int(szek)
    print(hely)
    print(True)
    print(False)
    with open("C:\git\PythonProject\Foglalas.txt","r",encoding="utf-8")as befile:
        for sor in befile:
            adat=sor.strip()
            foglalas.append(adat)
    print (foglalas[0])
    print (foglalas[1])
    print (foglalas[2])        
        
    if foglalas[nap][hely] == "U":
        return False
    else :
        return True

print(lekerdez(1,0,15))
print(True)