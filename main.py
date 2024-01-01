 #16:17
with open("melyseg.txt") as file:
    lista = [int(i) for i in file.readlines()]


print("1. feladat")
print(f"A fájl adatainak száma: {len(lista)}")

print("2. feladat")
betavolsag = int(input("Adjon meg egy távolságértéket!: "))
print(f"Ezen a helyen a felszín {lista[betavolsag]} mélyen van.")

print(f"Az érintett terület aránya: {round(( lista.count(0) / len(lista)) * 100 , 2)} %.")

with open("godrok.txt", "w", encoding="utf-8") as fil:

    belsolista = []
    for i, e in enumerate(lista):
        if e != 0:
            belsolista.append(e)
        else:
            if len(belsolista) != 0:
                print(*belsolista, file=fil)
                belsolista = []
            

with open("godrok.txt", "r", encoding="utf-8") as fil:
    szotar = {}
    szamlaloww = 0
    for i, e in enumerate(fil.readlines()):
        for j in e:
            szotar[i] = 
print("5. feladat")
with open("godrok.txt", "r", encoding="utf-8") as fill:

    print(f"Gödrök száma:", godorszam := sum(1 for i in fill.readlines())-1)

print("6. feladat")
if lista[betavolsag] != 0:
    pass
        
else:
    print("Az adott helyen nincs gödör")