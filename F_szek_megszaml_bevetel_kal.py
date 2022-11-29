foglalas=[]
with open("GIKT.txt", "r", encoding="utf-8") as befile:
    for sor in befile:
        adat=sor.strip() # enter eltávolítása sor végéről
        foglalas.append(adat)

#nem kell gondoskodni a fajl bezárásról, with bezárja maga
print(foglalas)

betukdb=0
for allista in foglalas:
    for allistaelem in allista:
        betukdb+=len(allistaelem)
        F = foglalas.count("F")
print(betukdb)

foglaltdb=0
foglalt = ["F"]
for allista in foglalas:
    for allistaelem in allista:
        for elem in foglalt:
            foglaltdb+=allistaelem.count(elem)
print(foglaltdb)

def bevetel(ossz):
    return ossz * 12000


print(bevetel(foglaltdb))