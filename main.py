 #16:17
with open("melyseg.txt") as file:
    lista = [int(i) for i in file.readlines()]


print("1. feladat")
print(f"A fájl adatainak száma: {len(lista)}")

print("\n2. feladat")
betavolsag = int(input("Adjon meg egy távolságértéket!: "))
print(f"Ezen a helyen a felszín {lista[betavolsag]} mélyen van.")

print("\n3. feladat")
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
            
print("\n5. feladat")
with open("godrok.txt", "r", encoding="utf-8") as fill:
    print(f"Gödrök száma:", godorszam := sum(1 for i in fill.readlines()))


godrik = [i.strip() for i in open("godrok.txt").readlines()]
print("\n6. feladat")
if lista[betavolsag] != 0:
    for index, elem in enumerate(szolista):
        if elem[0] <= betavolsag <= elem[1]:
            meres = [int(i) for i in godrik[index].split()]
            print("a)")
            print(f"A gödör kezdete: {elem[0]+1} méter, a gödör vége: {elem[1]} méter.")
            print("c)")
            print(f"Legnagyobb mélység: {max(meres)}")
            print("d)")
            print(f"A térfogat {sum([i *10 for i in meres ])} m^3.")
            print("e)")
            print(f"A vízmennyiség {sum([(i-1) *10 for i in meres ])} m^3.")

            print("b feladat, majd holnap")
            


        
else:
    print("Az adott helyen nincs gödör")