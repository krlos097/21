import random

#Crear el Mazo (1 a 10 y J,Q,K)
def crearMazo():
    return range(1,11) + [10, 10, 10]

def crearPalos(palos):
    if (palos == 0):
        return []
    else:
        return crearMazo() + crearPalos(palos - 1)
    
def Barajar(mazo):
    random.shuffle(mazo)
    return mazo

def crearBaraja():
    return Barajar(crearPalos(4))

def analizarCartas(cartas):
    print [str(carta) if carta != 1 else "1/11" for carta in cartas]

def Ases(cartas, ases):
    if (ases == 0):
        return sum(cartas)
    elif (sum(cartas) + 10 * ases <= 21):
        return sum(cartas) + 10 * ases;
    else:
        return Ases(cartas, ases - 1)
    
#Obtener el puntaje de las cartas que hay en la Mano
def Puntaje(cartas):
    return Ases(cartas, cartas.count(1))

def T_Jugador(cartas):
    print "Sus cartas son: "
    analizarCartas(cartas[0])

    if (Puntaje(cartas[0]) < 21 and bool(input("Pedir cartas (1) / Plantarse (0): "))):
        return T_Jugador([cartas[0] + [cartas[2][0]]] + [cartas[1]] + [cartas[2][1:]])
    else:
        return cartas


def T_Repartidor(cartas):
    
    if (Puntaje(cartas[1]) < 22):
        return T_Repartidor([cartas[0]] + [cartas[1] + [cartas[2][0]]] + [cartas[2][1:]])            
    else:
        print "Las cartas del Repartidor son:"
        analizarCartas(cartas[1])
        return cartas


def ResultadoFinal(Pjugador, Prepartidor):
    print "Puntaje jugador: " + str(Pjugador) + "\nPuntaje repartidor: " + str(Prepartidor) + "\n-----------------------------"
    
    if (Pjugador > 21):
        print "El Repartidor GANA el juego."
        
    elif Pjugador == 21 and (Prepartidor > 21 or Prepartidor < 21):
        print "El Jugador GANA el juego."
        
    elif (Pjugador == 21 and Prepartidor == 21):
        print "GANA EL REPARTIDOR."
        
    elif (Pjugador < 21 and (Prepartidor > 21 or Prepartidor < Pjugador)):
        print "Jugador GANA el juego."
        
    elif (Pjugador < 21 and Prepartidor > Pjugador and Prepartidor <22):
        print "El Repartidor GANA el juego."

    elif (Pjugador == Prepartidor):
        print "Gana el repartidor"

#Funcion principal del Juego, donde se compila todo (Crear Mazo/Repartir Cartas/Establecer los Turnos/Imprimir el Resultado del Juego).
def ElJuego(cartas,Turno):
    if cartas[2] == []:
        print "\nCreando Baraja..."
        ElJuego(cartas[0:2] + [crearBaraja()], Turno)
    elif cartas[0] == []:
        print "Repartiendo primeras cartas..."
        ElJuego([cartas[2][0:2]] + [cartas[1]] + [cartas[2][2:]], Turno)
        
    elif cartas[1] == []:
        print "Repartiendo segundas cartas..."
        ElJuego([cartas[0]] + [[cartas[2][0]]] + [cartas[2][1:]], Turno)

    elif Turno == 'Jugador':
        print "-------------------------------"
        print "Turno del Jugador\n"
        ElJuego(T_Jugador((cartas)),'Repartidor')
        
    elif Turno == 'Repartidor':
        print "\n-------------------------------"
        print "Turno del Repartidor\n"
        if (Puntaje(cartas[0])<22 and Puntaje(cartas[1])<Puntaje(cartas[0])):
            ElJuego(T_Repartidor((cartas)), 'FIN')
        else:
            print "Las cartas finales del Repartidor son: "
            analizarCartas(cartas[1])
            ResultadoFinal(Puntaje(cartas[0]),Puntaje(cartas[1]))
    else:
        print "\n\n--- RESULTADO DEL JUEGO ---\n" 
        print "Las cartas finales del Jugador son: "
        analizarCartas(cartas[0])
        print "Las cartas finales del Repartidor son: "
        analizarCartas(cartas[1])
        print "\n--------------------------------------------"
        print "El puntaje final de los participantes es:"
        ResultadoFinal(Puntaje(cartas[0]),Puntaje(cartas[1]))

#Funcion Main del Juego
def Juego():
    print "JUEGO DE 21"
    ElJuego([[], [], []], 'Jugador')
    print "\nFin Del Juego"

#Iniciar el Juego
Juego()
