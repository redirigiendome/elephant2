#Calcular el area de al menos 3 figuras geometricas
#Menu para elegir la figura
que="s"
while que=="s":
    print("Bienvenido al menú seleccionar una figura")
    print("Seleccione cualquiera de estas 3 figuras")
    print( )
    print("1. Cuadrado ")
    print("2. Triangulo")
    print("3. Circulo")
    selec=int(input("-> "))
    if selec==1:
        #Area de un cuadrado = Lado x Lado
        L1=int(input("Introduzca un lado del cuadrado -> "))
        Rep=L1*L1
        print("El area del cuadrado es de: ",Rep)
    if selec==2:
        #Area de un triangulo = (Base x Altura) / 2
        b=int(input("Introduzca la base del triangulo -> "))
        h=int(input("Introduzca la altura del triangulo -> "))
        rep2=(b*h)/2
        print("El area del triangulo con las medidas introducidas es de: ",rep2)
    if selec==3:
        #Area de un circulo = pi x Radio^2
        r=int(input("Introduzca el radio del circulo -> "))
        rep4=3.14*(r^2)
        print("El area del circulo es de: ",rep4)
    print("¿Quiere seguir usando el programa?")
    print(" S / N ")
    que=input("-> ")
