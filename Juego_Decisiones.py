import os
import time

import Funciones
import Textos_principales
from colorama import Fore
#Yakuza = Rojo
#Principal = Verde
#Max = azul
#personaje final = fuxia
#travesti = amarillo
navaja = False
Muerte = 0
Corte = False
Quemadura = False
Decisiones = ""
golpe = 0


def continuar():
    input(Fore.LIGHTGREEN_EX + "Presiona enter para continuar....")
    os.system("cls")


# Todo: Comienza el juego ESCENARIO FIJO 0
print(Textos_principales.inicio)

Decision_importante_1 = 0
while Decision_importante_1 != "1" and Decision_importante_1 != "2":
    Decision_importante_1 = input(Fore.RESET + "Al caer sientes un fuerte dolor en tu cabeza\n"
                                                   "1.- Seguir Corriendo\n"
                                                   "2.- Esperar a que pase el dolor\n"
                                                   "Que haras?: ")
    # Todo: Comienza linea 1 parte1(Color magenta)
    if Decision_importante_1 == "1":
        Decisiones += "1"
        continuar()
        print(
            Fore.RESET + "Decides correr sin importar que, despues de un par de minutos corriendo llegas a lo que "
                           "parece ser\n "
                           "           ----------------------------UN BARRIO JAPONES-----------------------------\n")
        print("Esto te confunde aun mas, ¿Como rayos llegaste a un barrio japones?")
        Funciones.secundarias(0)
        continuar()
        print(Fore.RESET + "\n\nAvanzas sin saber a donde ir, buscas un lugar tranquilo\n"
                           "te percatas que durante todo lo ocurrido no te has revisado los bolsillo ni nada")
        Revisar = 0
        while Revisar != "1" and Revisar != "2":
            Revisar = (input("1.-Revisas tus bolsillos\n"
                             "2.- Prefieres no hacerlos\n"
                             "Que haras?"))
            if Revisar == "1":
                print(Fore.GREEN + "Has encontrado una navaja, puede que te sea util en algun momento")
                continuar()

                navaja = True
            elif Revisar == "2":
                print(
                    Fore.RED + "Estas demasiado cansado, tomando en cuenta todo lo que paso, lo encuentras innecesario\n")
                continuar()
            else:
                print("No has seleccionado ninguna opcion")
                continuar()
        print(Fore.RESET + "Te levantas para seguir con tu viaje")
        print(Textos_principales.texto_1_l1)
        if navaja:
            print(
                Fore.GREEN + "Recuerdo la navaja que tenia en mi bolsillo, pero esperare el momento oportuno para "
                             "usarla")
            continuar()
        else:
            print(Fore.RED + "Instintivamente te pones a la defensiva")
            continuar()
        print(Textos_principales.texto_2_l1)
        continuar()
        if navaja:
            print(
                Fore.RESET + "Saco la navaja y rapidamente se la clavo en el pecho trate de preguntarle el por que me "
                             "buscaban \n "
                             "que querian de mi, pero ya era tarde, habia muerto......")
        else:
            print(
                Fore.RESET + "Se acerca rapidamente lanzandome corte tras corte, mi cuerpo reacciona agarro el filo del "
                           "cuchillo \n "
                           "Cortandome la mano ,golpeo su mano desarmandolo, 'Se acabo, por que me buscas?quien "
                           "soy?que quieren de mi?DIME¡¡'\n "
                           "tomo el cuchillo amenazandolo de gravedad, pero este sin ningun miedo toma mi mano y "
                           "rapidamente \n "
                           "se clava el cuchillo en el pecho ,recurrio al Harakiri,el orgullo de los yakuzas es "
                           "irrompible......")
            print(Fore.LIGHTRED_EX + "Ahora tienes un corte en la mano")
            Corte = True
        print(Textos_principales.texto_final_l1)
    # Todo: FIN LINEA 1

    # Todo: COMIENZO LINEA 2 (Color CYAN)
    elif Decision_importante_1 == "2":

        Decisiones += "2"
        print(Textos_principales.texto_1_l2)
        continuar()
        print(Fore.RED + "---------------PASAN LAS HORAS---------------")
        continuar()
        print(Textos_principales.texto_2_l2)
        continuar()
        print(Textos_principales.texto_3_l2)
        golpe += 5
        continuar()
        print(Textos_principales.texto_4_l2)
        continuar()

        librarse = 0
        while librarse != "1" and librarse != "2" and librarse != "3":
            librarse = input("Ya despues de analizar ves que las unicas soluciones son\n"
                                 "1.-Tratar de quemar las ataduras\n"
                                 "2.-Romper la silla\n"
                                 "3.-Seguir pensando\n"
                                 "Que haras?: ")
            if librarse == "1":
                print(
                    Fore.LIGHTYELLOW_EX + "ves cerca de ti unas caja que se están quemando y te la arreglas para dar\n"
                                          "pequeños saltos junto a la silla para llegar a su lado y así poner tu "
                                          "espalda\n "
                                          "contra el fuego y lograr que se quemen las cuerdas, lo logras pero no "
                                          "sales\n "
                                          "ileso pero con pequeñas quemaduras en tu manos")
                print(Fore.LIGHTRED_EX + "Ahora tienes quemaduras en las manos")
                continuar()
                Quemadura = True
            elif librarse == "2":
                print(
                    Fore.GREEN + "Comienzas a sarandearte fuertemente, la silla es vieja(tipico de fabrica "
                                 "abandonada)\n "
                                 "depues de 2 min horriblemente largos logras romper la silla")
                continuar()
            elif librarse == "3":
                print(Fore.RED + "Sigues pensando pero no se te ocurre nada, tu silla comienza a encenderse, sientes \n"
                                 "como tu carne se caliente, el dolor es insoportable......")
                print(Fore.LIGHTRED_EX + "---------------HAS MUERTO---------------------")
                Muerte += 1
                eleccion = input(Fore.RESET + "1.-Si\n"
                                                  "2.-Salir\n"
                                                  "Quieres volver a la eleccion?:   ")
                if eleccion == "1":
                    librarse = 0
                elif eleccion == "2":
                    print(Fore.BLUE + "---------------------FIN DEL JUEGO------------------------")
                    continuar()
                    exit()
            else:
                print("No has elegido ninguna de las opciones")
                continuar()
        Funciones.secundarias(3)
        print(Textos_principales.texto_final_l2)
# Todo: TERMINO LINEA 2
    else:
        print("No has seleccionado ninguna opcion")
        continuar()

# Todo: INICIO ESCENARIO FIJO 1
print(Textos_principales.texto_1_escenario_1)
continuar()
if Decisiones == "1":
    print("De pronto aparece el tipo al que los yakuzas habian golpeado")
elif Decisiones == "2":
    print("De pronto aparece un tipo medio golpeado ")
print(Textos_principales.texto_2_escenario_1)
continuar()
print(Textos_principales.texto_3_escenario_1)
continuar()
print(Fore.LIGHTBLUE_EX + "-------------------CAMINAN POR UNOS MINUTOS-----------------")
continuar()
Funciones.secundarias(2)
continuar()
print(Textos_principales.texto_4_escenario_1)
continuar()
hola = True

while hola:
    preguntar = input(Fore.RESET +"Ya dentro del auto decides preguntar\n"
                          "1.-Quien soy?\n "
                          "2.- Donde vamos?\n"
                          "3.-Quien eres?\n "
                          "4.-para seguir la historia\n"
                          "Preguntar:  ")
    if preguntar == "1":
        print(Fore.LIGHTBLUE_EX +"-Ya te lo dije, no es importante en estos momentos, hay cosas mas importantes ahora")
        continuar()
    elif preguntar == "2":
        print(Fore.LIGHTBLUE_EX +
            "-Tenemos que buscar a esa persona antes de que ellos la encuentren, vamos al ultimo lugar que supe que "
            "se"
            "encontraba")
        continuar()
    elif preguntar == "3":
        print(Fore.LIGHTBLUE_EX +"-Me llamo max por ciertas cosas del destino nos conocimos y terminamos metidos en "
                                 "este lio")
        continuar()
    elif preguntar == "4":
        hola = False
    else:
        print("No has seleccionado ninguna opcion")
        continuar()

print("------------COMIENZA A SONAR UN TELEFONO-------------")

print(Fore.LIGHTBLUE_EX + "'Oh es mi celular, deja contesto'")
continuar()
print(Fore.RESET + "Se le ve frustrado, lo miras esperando a que te diga que sucede\n"
                   +Fore.LIGHTBLUE_EX +"-Me acaba de llamar mi fuente de informacion hay una nueva "
                                       "ubicacion registrada y no tiene certesa"
                   " de cual sera mejor revisar, esta su "
                   "departamento o una "
                   "bodega que estaba a su nombre'")
Decision_importante_2 = 0
while Decision_importante_2 != "1" and Decision_importante_2 != "2":
        Decision_importante_2 = input(Fore.RESET + "1.-Departamento\n"
                                                       "2.-Bodega\n"
                                                       "Donde quieres ir?:")
        # Todo: Linea 3 Apartamento
        if Decision_importante_2 == "1":
            Decisiones += "1"
            print("Decides ir al departamento, Max solo te mira y decide hacerte caso")
            print("------------MANEJAN POR UNOS MINUTOS------------------")
            continuar()
            print(Textos_principales.texto_1_linea3)
            decision_l3 = 0
            while decision_l3 != "1" and decision_l3 != "2":
                decision_l3 = input("1.-Preguntar que pasa\n"
                                        " 2.-Esperar a que salga y no decir nada\n"
                                        "Que haras?: ")
                if decision_l3 == "1":
                    print(Fore.RESET + "Preguntas a Max que le sucede,este solo te mira,entonces responde\n"
                                       +Fore.LIGHTBLUE_EX+"-Es imposible que le "
                                       "tomes el peso, "
                                       "has olvidado todo, pero de aqui en adelante piensa que podemos morir facilmente, asi "
                                       "que "
                                       "ten cuidado'")
                elif decision_l3 == "2":
                    print(
                        Fore.RESET + "Esperas a que Max baje del auto, lo observas intranquilo, el solo te mira y sigue "
                                     "caminando")
                else:
                    print("No has seleccionado ninguna opcion")
                    continuar()
            print(Textos_principales.texto_2_linea3)
            continuar()
            print(Textos_principales.texto_3_linea3)
            continuar()
            print(Textos_principales.texto_4_linea3)
            decision_l3_1 = 0
            while decision_l3_1 != "1" and decision_l3_1 != "2":
                decision_l3_1 = input("1.-No era una mafia?\n"
                                                    "2.-Quien rayos son esos tipos de traje?\n"
                                                    "Cual va a ser tu pregunta?: ")

                if decision_l3_1 == "1":
                    print(Fore.RESET + "No, a esos le debiamos el dinero que pedimos prestado...")
                elif decision_l3_1 == "2":
                    print(
                        Fore.RESET + "Para resumirtelo son una asociacion dispuesta a todo con tal de conseguir lo que "
                                     "quieren...")
                else:
                    print("No has seleccionado ninguna opcion")
                    continuar()

            print(Textos_principales.texto_5_linea3)
            continuar()
            print(Textos_principales.texto_6_linea3)
            continuar()
            decision_l3_2 = 0
            while decision_l3_2 != "1" and decision_l3_2 != "2":
                decision_l3_2 = input(Fore.RESET + "1.-Animas a Max\n"
                                                       "2.-Preguntar cuantas balas tiene\n"
                                                       "Que haras?: ")
                if decision_l3_2 == "1":
                    print(Fore.GREEN + "Animas a Max en voz baja , El cierra los ojos por un momento ya se le ve mas "
                                       "concentrado\n"
                                       "Max te lo agradece")
                elif decision_l3_2 == "2":
                    print(Fore.GREEN + "Max te mira algo extrañado pero responde 'Tengo 5' el no entiende por que la "
                                       "pregunta pero"
                                       " se le ve\n"
                                       "mas tranquilo")
                else:
                    print("No has seleccionado ninguna opcion")
                    continuar()
            continuar()
            print(Textos_principales.texto_7_linea3)
            continuar()
            while True:
                decision_l3_3 = input(Fore.RESET + "NECESITAS HACER ALGO AHORA\n"
                                                       "1.-Ves una pistola en el piso, la tomas\n"
                                                       "2.-Corres aprovechando que sigue lejos\n"
                                                       "3.-Esperas que se acerce para atacarle\n"
                                                       "Que haras?:  ")
                if decision_l3_3 == "1":
                    print("Agarras la pistola y rapidamente disparas, lo hieres en la pierna haciendolo caer, corres "
                          "hacia el\n"
                          "golpeando su cabeza con una patada, el tipo cae totalmente noqueado al piso")
                    break
                elif decision_l3_3 == "2":
                    print("Corres despavorido aprovechando que aun se encuentra lejos esperanzado de salvarte, pero "
                          "escuchas\n"
                          "un disparo y todo se va a negro, Realmente pensanste que correr era una buena opcion contra una"
                          "pistola")
                    print(Fore.RED + "MORISTE.......")
                    while True:
                        eleccion_1 = input("1.-Volver a las opciones 2.-Salir: ")
                        if eleccion_1 == "1":
                            print("Volviendo.......")
                            break
                        elif eleccion_1 == "2":
                            print(Fore.BLUE + "-----------FIN DEL JUEGO-------------")
                            continuar()
                            exit()
                elif decision_l3_3 == "3":
                    print("Esperas a que el hombre se acerca y cuando lo tienes a una distancia prudente lo tumbas, "
                          "intercambian\n golpes por unos segundos(recibes 7 golpes) hasta que al final tu persistencia "
                          "gana, el hombre "
                          "ya no\n"
                          " se levanta, ganaste pero algo golpeado")
                    break
                else:
                    print("No has seleccionado ninguna opcion")
                    continuar()
            continuar()
            print(Textos_principales.texto_final_linea3)
            continuar()
        # Todo: LINEA 4 BODEGA
        if Decision_importante_2 == "2":
            Decisiones += "2"
            print("Decides ir a la Bodega, Max solo te observa y conduce hacia la bodega")
            print("-------------CONDUNCEN UNOS MINUTOS-------------------")
            print(Textos_principales.texto_1_linea4)
            continuar()
            print(Textos_principales.texto_2_linea4)
            continuar()
            print(Fore.LIGHTRED_EX + "---------------PASAN UN PAR DE MINUTOS----------------")
            continuar()
            print(Textos_principales.texto_3_linea4)
            continuar()
            print(Textos_principales.texto_4_linea4)
            continuar()
            print(Textos_principales.texto_5_linea4)
            decision_l4_0 = 0
            while decision_l4_0 != "1" and decision_l4_0 != "2":
                decision_l4_0 = input("1.-Seguir por el callejon \n"
                                      "2.-Usar una cuerda para subir por una ventana cercana"
                                      "Por donde quieres ir?:  ")
                if decision_l4_0 == "1":
                    print(Fore.GREEN + "Sigues por el callejon, despues de unos minutos caminando este te lleva a las "
                                       "afueras del"
                                       "anden.")
                elif decision_l4_0 == "2":
                    print(Fore.GREEN + "Usas la cuerda y logras engancharla en la ventana")
                    if Corte == True or Quemadura == True:
                        print("Comienzas a escalar pero las heridas en tus manos no te dejan avanzar y caes, decides ir por el "
                              "callejon\n el cual te lleva a las afueras del anden.")
                        print(Fore.RED+"Ahora tienes un pie esguinzado")
                        continuar()
                        print(Fore.BLUE+"Caminas lento por tu nueva herida")
                        time.sleep(3)
                        continuar()
                        print(Fore.BLUE+"Realmente caminas demasiado lento")
                        time.sleep(3)
                    else:
                        pelea = 0
                        while pelea != "1" and pelea != "2" and pelea != "3":
                            print("Comienzas a escalar logrando subir por la ventana, parece ser un tipo de habitacion, "
                                  "decides salir"
                                  "rapidamente\n pero en tu camino se cruza el travesti de 2 metros'Como no me vas a pagar "
                                  "te voy a "
                                  "tener\n que golpear cariño'(Te guiña el ojo), te agarra y arroja hacia una pared")
                            pelea = input("1.-Usas tus habilidades de combate para acabar con el\n"
                                              "2.-Agarras un fierro que hay cerca de ti para golpearlo\n"
                                              "3-.La rabia y el estres te consumen y te enfrentas a el de frente\n"
                                              "Que haras?: ")
                            if pelea == "1":
                                print("Sientes que tu cuerpo ya sabe lo que hay que hacer y sigues ese sentimiento, corres,"
                                      " esquivas y "
                                      "golpeas\n logrando tirarlo no permanentemente pero si para lograr escapar")
                            elif pelea == "2":
                                print("El tipo se abalanza sobre ti, lo esquivas y agarras el fierro, rapidamente golpeas"
                                      " su cabeza"
                                      "repetidamente, el suelo y las paredes se pintaron con la sangre del malvado travesti "
                                      "gigante"
                                      "abandonas la cruda escena....")
                            elif pelea == "3":
                                print("Vas de frente con toda la furia acumulada, logras hacer contacto pero la realidad toca "
                                      "tu puerta"
                                      "\n el travesti gigante te agarra y golpea de manera repetida(6 veces), hasta que pasado"
                                      " unos "
                                      "minutos se "
                                      "aburre\n y se va")
                                golpe += 6
                            else:
                                print("No has seleccionado ninguna opcion")
                                continuar()
            continuar()
            print(Fore.LIGHTBLUE_EX + "logras llegar a la calle, el anden se encuentra frente a ti...")
# Todo: Comienza tramo final de la historia
print(Textos_principales.texto_1_lineafinal)
while True:
    print("Comencemos dime que resultado arroja este codigo\n")
    print("color1 =  naranja\n"
          "color2 = azul\n"
          "color3 = rojo\n"
          "for x in color1:\n"
          "print(x)\n")
    print("1.- escribe naranja letra por letra hacia abajo\n"
          "2.- escribe rojo todo junto de manera horizontal(hacia el lado)\n"
          "3.-AZUL ESSSSS AZUL\n")
    respuesta = input("Digita tu respuesta: ")
    if respuesta == "1":
        print("Respuesta correcta, desactivando seguridad, avance")
        break
    elif respuesta == "2" or respuesta == "3":
        print("Respuesta incorrecta realizando ejecucion inmediata")
        print("Sientes un piquete en tu mano, un dolor agonizante te sube por el cuerpo comienzas a gritar y retorcerte"
              "\n hasta que te desmayas del dolor.....\n"
              "Estas muerto.....")
        Muerte +=1
        while True:
            volver_a_la_prueba = input("Quieres volver a la prueba?\n"
                                           "1.- Volver 2.-Salir: ")
            if volver_a_la_prueba == "1":
                print("Volviendo......")
                continuar()
                break
            elif volver_a_la_prueba == "2":
                print(Fore.BLUE + "-----------------FIN DEL JUEGO---------------")
                continuar()
                exit()
            else:
                print("No has seleccionado ninguna opcion")
    else:
        print("No has selecionado ninguna opcion")
        continuar()
print(Fore.LIGHTGREEN_EX + "Avanzas por la puerta que se acababa de abrir")

print(Textos_principales.texto_2_lineafinal)
continuar()
print(Textos_principales.texto_2_lineafinal_extra)
continuar()
Funciones.secundarias(1)
continuar()
print(Fore.RESET + "La mujer que rescataste queda igual de impacatada que tu, quien rayos era esa....")
print("-"*20+"FIN"+"-"*20)
print("Tus decisiones importantes han sido")
if Decisiones == "11":
    print("--Seguiste corriendo--\n"
          "--Fuiste al Departamento--")
    continuar()
elif Decisiones == "12":
    print("--Seguiste corriendo--\n"
          "--Fuiste a la Bodega--")
    continuar()
elif Decisiones == "21":
    print("--Decidiste esperar--\n"
          "--Fuiste al Departamento--")
    continuar()
elif Decisiones == "22":
    print("--Decidiste esperar--\n"
          "--Fuiste a la bodega--")
    continuar()
print("Te han golpeado {} veces".format(golpe))
continuar()
print("Has muerto {} veces".format(Muerte))
continuar()
print("Gracias por jugar")
time.sleep(2)
exit()