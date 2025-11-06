# Programozási tételek
# Eldöntés tétele

# Adott egy tömb
# Van-e a tömbnek valamilyen eleme
# Válasz: 1 db logikai érték

import random
számok = []
for index in range(0,15):
    számok.append(random.randint(1,10))

print(*számok, sep=", ")

# Van-e a számok között páros szám?
index = 0
while index < len(számok) and számok[index]%2!=0:
    index += 1

if index < len(számok):
    print("Van páros szám a tömb elemei között.")
else:
    print("Nincs páros szám a tömb elemei között.")

# Alternatív megoldások
van = False
for szám in számok:
    if szám % 2 == 0:
        van = True
        break

if van == True:
    print("Van páros szám a tömb elemei között.")
else:
    print("Nincs páros szám a tömb elemei között.")