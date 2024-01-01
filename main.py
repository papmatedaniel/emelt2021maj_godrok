 #16:17
with open("melyseg.txt") as file:
    lista = [int(i) for i in file.readlines()]


print("1. feladat")
print(f"A fájl adatainak száma: {len(lista)}")

print("2. feladat")
betavolsag = int(input("Adjon meg egy távolságértéket!: "))
print(f"Ezen a helyen a felszín {lista[betavolsag]} mélyen van.")

print("3. feladat")
print(f"Az érintett terület aránya: {round(( lista.count(0) / len(lista)) * 100 , 2)} %.")

with open("godrok.txt", "w", encoding="utf-8") as fil:
    szolista = []
    belsolista = []
    for i, e in enumerate(lista):
        if e != 0:
            belsolista.append(e)
        else:
            if len(belsolista) != 0:
                print(*belsolista, file=fil)
                szolista.append((i-len(belsolista), i))
                belsolista = []
            
print("5. feladat")
with open("godrok.txt", "r", encoding="utf-8") as fill:
    print(f"Gödrök száma:", godorszam := sum(1 for i in fill.readlines()))


godrik = [i.strip() for i in open("godrok.txt").readlines()]
print("6. feladat")
if lista[betavolsag] != 0:
    for index, elem in enumerate(szolista):
        if elem[0] <= betavolsag <= elem[1]:
            meres = godrik[index+1]
            print("a)")
            print(f"A gödör kezdete: {elem[0]+1} méter, a gödör vége: {elem[1]} méter.")

        
else:
    print("Az adott helyen nincs gödör")