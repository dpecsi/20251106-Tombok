# Programozási tételek
# Keresés tétele

# Adott egy tömb
# Megtalálható-e a tömbben egy érték
#   és ha igen, akkor hányadik helyen?
# Válasz: 1 db logikai érték, és 1 db sorszám

import random
számok = []
for _ in range(0,15):
    számok.append(random.randint(1,10))

print(*számok, sep=", ")

# Van-e páros szám a tömbben, és ha igen akkor hol?
holVan = 0
while holVan < len(számok) and számok[holVan]%2!=0:
    holVan += 1

if holVan < len(számok):
    print(f"Van találat: {számok[holVan]}, a {holVan}. indexű helyen")
else:
    print("Nincs találat")