from time import time
from random import init


dado = random.randint(1,6)
numero_intentos = 5
lanzar = input("Lanza el dado ingresando la letra D o ingresa la letra S para salir:  ")
if lanzar.upper == "D":
    print("Lanzando el dado.....")
    time.sleep(2)
    print("El dado ha sido lanzado, ahora debes adivinar el numero")
    while numero_intentos > 0:
        print("numero de intentos restantes: {}".format(numero_intentos))
        adivinar = int(input("Que numero crees que dio?:  "))
        if adivinar == dado:
            print("Ganaste el numero si era {}".format(dado))
        else:
            print("Has fallado, el numero era {}".format(dado))
            numero_intentos -= 1
            print("Tu numero de intentos restantes es : {}".format(numero_intentos))
