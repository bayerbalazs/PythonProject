import random
Hetfo_DE =[]

szek=0
for szek in range(0,624,1) :
    i = random.randrange(0,2)
    if i == 0 :
        j = "F"
    elif i == 1:
        j = "U"
    else:
        print("valami error")        
    Hetfo_DE.append(j)
    szek = szek + 1 

print (Hetfo_DE)
with open("C:\git\PythonProject\Pproject.txt","w",encoding="utf-8") as kifile:
    kifile.writelines(Hetfo_DE)
with open ("C:\git\PythonProject\Pproject.txt","r",encoding="utf-8") as befile:
    for i in range:   
        adat=sor.strip()
        lista.append(adat)
  
print(foglalt)  





