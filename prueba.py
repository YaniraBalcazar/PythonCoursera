opcion = -1
while opcion != 0:
    opcion=int(input("Elija opcion 1, 2 o 0 (salir):"))
    if opcion != 0:
        if opcion == 1:
          print("Ejecutamos la opcion 1")
        elif opcion == 2:
          print("Ejecutamos la opcion 2")
    else:
        print("Has decidido salir.")