dinero=0
contador=0

while contador<12:
    contador= contador+1
    ahorro= int(input("Ingrese la cantidad de dinero que desea ahorrar"))
    dinero= dinero+ahorro
    print("El ahorro hasta ahora es:",dinero)

print("La cantidad ahorrada este año es:", dinero)