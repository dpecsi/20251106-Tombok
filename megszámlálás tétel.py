# Programozási tételek
# Megszámlálás tétele

# Adott egy tömb
# Hány eleme felel meg egy feltételnek?
# Válasz: 1 db szám

import random
#számok = [1,5,3,1,4,6,7,5,3]
számok = []

for index in range(0,15):
    számok.append(random.randint(1,10))

#print(", ".join(str(szám) for szám in számok))
#print(", ".join(map(str, számok)))
print(*számok, sep=", ")

# 15 db (1-10 közé eső) véletlen szám között, hány darab páros szám van
darab = 0
for szám in számok:
    if szám % 2 == 0:
        darab += 1
print(f"A véletlen számaim között {darab} darab páros szám van")

# Alternatív megoldások...
darab = len(list(filter(lambda x: x % 2 == 0, számok)))
print(f"A véletlen számaim között {darab} darab páros szám van")

darab = len([szám for szám in számok if szám % 2 == 0])
print(f"A véletlen számaim között {darab} darab páros szám van")
