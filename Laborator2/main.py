def castigator(a, b):
    if a=="Piatra" and b=="Foarfeca":
        return "Jucatorul 1 a castigat"
    elif a=="Foarfeca" and b=="Hartie":
        return "Jucatorul 1 a castigat"
    elif a=="Hartie" and b=="Piatra":
        return "Jucatorul 1 a castigat"
    elif a==b:
        return "Egalitate"
    else:
        return "Jucatorul 2 a castigat"
    
a = input("Jucatorul 1, introduceti Piatra, Hartie sau Foarfeca: ")
b = input("Jucatorul 2, introduceti Piatra, Hartie sau Foarfeca: ")
print(castigator(a, b))