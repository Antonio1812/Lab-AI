def genereaza_factura():
    kwags = { "nume_client": input("Nume client: "), "pret" : int(input("Pret: ")), "cantitate": int(input("Cantitate: ")) }
    return f"Factura pentru {kwags['nume_client']}:\nPret: {kwags['pret']}\nCantitate: {kwags['cantitate']}\nTotal: {kwags['pret'] * kwags['cantitate']}"   

print(genereaza_factura())