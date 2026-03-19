import random

numarRandom= random.randint(1, 50)
print("Ghiceste numarul intre 1 si 50")
incercari =0
while    True:
    numar=int(input("Introduceti numarul: "))
    incercari +=1
    if numar < numarRandom:
        print("Numarul este prea mic")
    elif numar > numarRandom:
        print("Numarul este prea mare")
    elif numar == numarRandom:
        print(f"Felicitari! Ai ghicit numarul in {incercari} incercari!")
        break
