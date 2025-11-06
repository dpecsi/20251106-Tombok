
# szám = 5
# szám = int(5)
# szám = int(input("Kérek egy számot: "))

számok = [5,4,3,2]

szám = számok[0] + 10
számok[1] = 1000        # 5 1000 3 2

for elem in számok:
    if elem % 2 == 0:
        print(elem)

print("-------------")

# számok [4] = 1 # hibás mert kívül indexelt a tartományon
számok.append(1)        # 5 1000 3 2 1
számok.remove(1000)     # 5 3 2 1
utolsó = számok.pop()   # 5 3 2

for elem in számok:
    print(elem)