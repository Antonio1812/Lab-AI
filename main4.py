import random
print ("Bine ai venit la loteria Python!")

numere = [0, 0, 0, 0, 0, 0]

enumerate(numere)==[(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)] 

for i,numere in enumerate(numere):
    numere = random.randint(1, 49)
    print (i, numere)

print ("Introdu cele 6 numere, intre 1 si 49)")
numereJucator = [0, 0, 0, 0, 0, 0]
for i in range(6):
    numereJucator[i] = int(input(f"Numarul {i+1}: "))
print (numereJucator)



