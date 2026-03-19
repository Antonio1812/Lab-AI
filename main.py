nota = int(input("Introduceti nota examen: "))

note_valide = list(range(0, 11))

while nota not in note_valide:
    nota = int(input("Reintroduceti nota examen: "))

if nota < 5:
    print("Reexaminare")
elif nota <= 6:
    print("Suficient")
elif nota <= 8:
    print("Bine")
else:
    print("Excelent")