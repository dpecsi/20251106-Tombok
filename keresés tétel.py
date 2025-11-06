# Programozási tételek
# Keresés tétele

# Adott egy tömb
# Melyik a középső eleme?
# Válasz: 1 db tömb elem

import random
számok = []
for index in range(0,15):
    számok.append(random.randint(1,10))

print(*számok, sep=", ")

tömb_méret = len(számok)
#középső_index = int(tömb_méret/2)
középső_index = tömb_méret//2
középső_elem = számok[középső_index]
print(f"Középső elem: {középső_elem}")

# Alternatív megoldások
print(f"Középső elem: {számok[len(számok)//2]}")
print(f"Középső elem: {számok[int(len(számok)/2)]}")