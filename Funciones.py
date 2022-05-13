
from colorama import Fore


def secundarias(x):
    if x == 0:
        print(Fore.BLUE+"Ves un gato")
        uno = input("Lo quieres acariciar?\n"
                    "1.-Si 2.-No: ")
        if uno == "1":
            print(Fore.GREEN+"Awwww, bueno continuemos")
        elif uno == "2":
            print(Fore.RED +"Mala persona -1 amabilidad\n" \
            " (No hay estadisticas asi que da igual) ")
        else:
            print(Fore.RED+"No eres mucho de seguir instrucciones verdad?, da igual vamos....")
    elif x == 1:
        print(Fore.BLUE+"Se acerca rapidamente una mujer hacia ti, sin tu poder reaccionar te golpea\n"
              "Entonces grita'ME DEJASTE PLANTADA EN EL ALTAR' te tira un anillo en la cara y se va")
    elif x == 2:
        print(Fore.RESET+"De la nada aparece un travesti de 2 metros(ES INTIMIDANTE¡¡¡¡¡)\n"
              "hay un silencio incomodo hasta que el travesti dice 'Me dejaste sola en el motel\n"
              "me quede atrapada en el baño y cuando sali no estabas '")
        Correr = input("1.-Correr\n"
                       "no hay mas opciones: ")
        if Correr == "1":
            print("Buena elecccion yo tampoco me quedaria, Corre mide 2 metros si no nos apuramos nos alcanzara"+Fore.GREEN)
        else:
            print("Querias elegir algo mas? ENSERIO?, da igual corre, necesitas estar vivo para seguir jugando"+Fore.RED)
    elif x == 3:
        print(Fore.RED+"Te caiste, ve bien por donde vas")
