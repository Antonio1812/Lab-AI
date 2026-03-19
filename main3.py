orase = str("Bucuresti, Cluj-Napoca, Timisoara, Iasi").split(", ")

enumerate(orase)==[(1, 'Bucuresti'), (2, 'Cluj-Napoca'), (3, 'Timisoara'), (4, 'Iasi')]

for i, orase in enumerate(orase):
    print(i, orase)

