# Programozási tételek
# Összegzés tétele

# Adott egy numerikus tömb
# Mennyi a tömb elemeinek az "összege"
# Válasz: 1 db szám

import random
számok = []
for index in range(0,15):
    számok.append(random.randint(1,10))

print(*számok, sep=", ")

összeg = 0
for szám in számok:
    összeg += szám

# Mennyi a tömb elemeinek az "összege"
print(f"A számok összege: {összeg}")

# Alternatív megoldás
print(f"A számok összege: {sum(számok)}")