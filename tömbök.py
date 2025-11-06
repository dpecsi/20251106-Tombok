
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

print("-------------")

for index in range(1,10):
    print(index)

print("-------------")

segéd = range(1,10)
print(segéd[5])

print("-------------")
print(type(segéd))
print(type(list(segéd)))
print(type(számok))

print("-------------")
print(számok)
print(f"Első eleme a tömbnek: {számok[0]}")
print(f"Második eleme a tömbnek: {számok[1]}")
print(f"Utolsó eleme a tömbnek: {számok[-1]}")
print(f"2-3. eleme a tömbnek: {számok[1:]}")
print(f"2-3. eleme a tömbnek: {számok[1:3]}")
print(számok)
számok[1:3] = ["három", "kettő"]
print(számok)
számok.insert(2, 1000)
print(számok)
print("-------------")
print(len(számok))
