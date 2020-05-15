A=int(input("Ingrese primer número"))
B=int(input("Ingrese segundo número"))
X=int(input("Seleccione la operación: 1 para suma, 2 para resta, 3 para multiplicación o 4 para división" ))

if X==1:
    Suma=A+B
    print("El resultado de la operación es:",Suma)

elif X==2:
    Resta= A-B
    print("El resultado de la operación es:",Resta)

elif X==3:
    Multiplicación=A*B
    print("El resultado de la operación es: ",Multiplicación)

elif X==4:
    División= A/B
    print("El resultado de la operación es:",División)


