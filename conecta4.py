class Jugador:

    def __init__(self):

        self.nombre = ""#nombre del jugador
        self.caracter = ""#caracter con el que quiere jugar

    def caracteristicas(self,string):

        self.nombre = input(string)
        self.caracter = input("Escoje un caracter para jugar: ")

            ###########################

class Juego:

    def __init__(self):

        self.table = []#[[" "," "," "," "," "," ",],[" "," "," "," "," "," ",],[" "," "," "," "," "," ",],[" "," "," "," "," "," ",],[" "," "," "," "," "," ",],[" "," "," "," "," "," ",],[" "," "," "," "," "," ",]]
        self.terminado = False
        self.ganador = " "
        self.turno = ""#para recordar el turno del jugador si deciden terminar el juego

    def genera_tablero(self):
        #imprimir bien el tablero
        #y que haga los casos
        print("-----------------")
        for i in range(6):
        	self.table.append([0] *7)
        n = 0
        for c in range(6):
        	n="|"
        	for f in range(7):
        		n = n + " " + str(self.table[c][f])
        	n=n+" |"
        	print(n)
        print("-----------------")
        print("  0  1  2  3  4  5  6")
        #m = 0
        #while(m < 12):
        #    if(m%2 == 0):
        #        f = int(1/2)
        #        for c in range(6):
        #            print("| "+self.table[f][c]+" ", end = '')#,end=' ') ##Me marca como erro de sintax por el end
        #        print("|")
        #    if(m%2 != 0):
        #        print("-----"*6)
        #    m += 1
        #print("   1   2   3   4   5   6")

    def tira(self,jugador):
        try:
            c = int(input("Turno de: "+jugador.nombre+"\nElige la columna donde quieras meter la ficha: "))
            self.genera_tablero()
            if(c > 6 or c < 1):
                print("##Fuera de rango##")
        except ValueError:
            print("Entrada Invalida, Debe ser un numero")

        f = 5#filas
        a = False

        while not a:
            if(self.table[0][c-1] != " "):
                print("la columna esta llena")
                c = int(input("En que columna quieres meter tu ficha: "))
            elif(self.table[f][c-1] == " "):
                self.table[f][c-1] = jugador.caracter
                a = True
            else:
                f -= 1#las fichas se rellenan de abajo hacia arriba en las columnas

    def ganar(self,jugador):

        f = 5#compara las filas
        while(f >= 0 and self.terminado == False):
            #compara la fila f 2-5
            if(jugador.caracter == self.table[f][5] and self.table[f][5] == self.table[f][4] and self.table[f][4] == self.table[f][3]): #and self.table[f][3] == self.table[f][2):
                self.terminado = True
                self.ganador = "Ha ganado: "+jugador.nombre
                print("Ha ganado: "+jugador.nombre)
            #compara la fila f 1-4
            elif(jugador.caracter == self.table[f][4] and self.table[f][4] == self.table[f][3] and self.table[f][3] == self.table[f][2] and self.table[f][2] == self.table[f][1] ):#lo mismo
                self.terminado = True
                self.ganador = "Ha ganado: "+jugador.nombre
                print("Ha ganado: "+jugador.nombre)
            #compara la fila f columna 0-3
            elif(jugador.caracter == self.table[f][3] and self.table[f][3] == self.table[f][2] and self.table[f][2] == self.table[f][1] and self.table[f][1] == self.table[f][0]):#lo mismo aunque no creo
                self.terminado = True
                self.ganador = "Ha ganado: "+jugador.nombre
                print("Ha ganado: "+jugador.nombre)
            f -= 1
        c = 0#compara las columnas
        while(c >= 0 and self.terminado == False):
            #compara la columna c 2-5
            if(jugador.caracter == self.table[c][5] and self.table[c][5] == self.table[c][4] and self.table[c][4] == self.table[c][3] and self.table[c][3] == self.table[c][2]):#posiblemente falte un caso
                self.terminado = True
                self.ganador = "Ha ganado: "+jugador.nombre
                print("Ha ganado: "+jugador.nombre)
            #compara la columna c 1-4
            elif(jugador.caracter == self.table[c][4] and self.table[c][4] == self.table[c][3] and self.table[c][3] == self.table[c][2] and self.table[c][2] == self.table[c][1]):#lo mismo
                self.terminado = True
                self.ganador = "Ha ganado: "+jugador.nombre
                print("Ha ganado: "+jugador.nombre)
            #compara la columna c 0-3
            elif(jugador.caracter == self.table[c][3] and self.table[c][3] == self.table[c][2] and self.table[c][2] == self.table[c][1] and self.table[c][1] == self.table[c][0]):#lo mismo aunque no creo
                self.terminado = True
                self.ganador = "Ha ganado: "+jugador.nombre
                print("Ha ganado: "+jugador.nombre)
            c -= 1

        #diagonales de izquierda a derecha
        f = 5
        while(f >= 3 and self.terminado == False):
            #compara las diagonales columna c fila f [f][0]-[f-3][2] hasta f[3]-[f-3][0] con f entre 5-3
            if(jugador.caracter == self.table[f][0] and self.table[f][0] == self.table[f-1][1] and self.table[f-1][1] == self.table[f-1][2] and self.table[f-1][2] == self.table[f-1][3]):##psiblemente este mal
                self.terminado = True
                self.ganador = "Ha ganado: "+jugador.nombre
                print("Ha ganado: "+jugador.nombre)
            elif(jugador.caracter == self.table[f][1] and self.table[f][1] == self.table[f-1][2] and self.table[f-1][2] == self.table[f-1][3] and self.table[f-1][3] == self.table[f-1][4]):
                self.terminado = True
                self.ganador = "Ha ganado: "+jugador.nombre
                print("Ha ganado: "+jugador.nombre)
            elif(jugador.caracter == self.table[f][2] and self.table[f][2] == self.table[f-1][3] and self.table[f-1][3] == self.table[f-1][4] and self.table[f-1][4] == self.table[f-1][5]):
                self.terminado = True
                self.ganador = "Ha ganado: "+jugador.nombre
                print("Ha ganado: "+jugador.nombre)
            f -= 1
        #diagonales de derecha a izquierda
        f = 5
        while(f >= 3 and self.terminado == False):
            #compara las diagonales columna c fila f [f][5]-[f-3][2] hasta f[3]-[f-3][0] con f entre 5-3
            if(jugador.caracter == self.table[f][5] and self.table[f][5] == self.table[f-1][4] and self.table[f-1][4] == self.table[f-1][3] and self.table[f-1][3] == self.table[f-1][2]):##psiblemente este mal
                self.terminado = True
                self.ganador = "Ha ganado: "+jugador.nombre
                print("Ha ganado: "+jugador.nombre)
            elif(jugador.caracter == self.table[f][4] and self.table[f][4] == self.table[f-1][3] and self.table[f-1][3] == self.table[f-1][2] and self.table[f-1][2] == self.table[f-1][1]):
                self.terminado = True
                self.ganador = "Ha ganado: "+jugador.nombre
                print("Ha ganado: "+jugador.nombre)
            elif(jugador.caracter == self.table[f][3] and self.table[f][3] == self.table[f-1][2] and self.table[f-1][2] == self.table[f-1][1] and self.table[f-1][1] == self.table[f-1][0]):
                self.terminado = True
                self.ganador = "Ha ganado: "+jugador.nombre
                print("Ha ganado: "+jugador.nombre)
            f -= 1
    def Terminado(self):#En caso de empate

        if(self.table[0][0] != " " and self.table[0][1] != " " and self.table[0][2] != " " and self.table[0][3] and self.table[0][3] != self.table[0][4]):
            self.terminado = True
            self.ganador = "Han empatado"
            print("Han empatado :/")

    def jugar(self,jugador1,jugador2):

        import random
        self.genera_tablero()
        i=random.randint(1,2)#para que sea aleatorio quien empieza a tirar la ficha
        while(self.terminado == False):

            if(i%2 == 0):
                self.tira(jugador1)#el jugador1 tira la ficha
                self.ganar(jugador1)#verifica si ha ganado

            elif(i%2 != 0):
                self.tira(jugador2)#el jugador2 tira la ficha
                self.ganar(jugador2)#verifica si ha ganado
            i += 1
            self.Terminado()#verifica si aun quedan jugadas o tiros disponibles
        ##########################3

            #######################

print("Bienvenido al juego conecta 4")
jugador_1 = Jugador()
jugador_1.caracteristicas("Jugador 1, Ingresa tu nombre: ")

jugador_2 = Jugador()
jugador_2.caracteristicas("Jugador 2, Ingresa tu nombre: ")
#inicia partida
table = Juego()
table.jugar(jugador_1, jugador_2)

def volver_a_jugar(pregunta):
    if(pregunta == 1):
        entrada = input("Jugaran los mismos jugadores (si/no): ")
        while(entrada != "si" and entrada != "no"):
            entrada = input("Jugaran los mismos jugadores (si/no): ")
    if(pregunta == 2):
        entrada = input("Que jugador cambiara (1/2/ambos): ")
        while(entrada != "1" and entrada != "2" and entrada != "ambos"):
            entrada = input("Que jugador cambiara (1/2/ambos): ")
    return entrada

inicio = True
while(inicio):
    table = Juego()
    reinicio = input("Quieren iniciar otro juego (si/no): ")
    if(reinicio == "si"):
        jugadores = volver_a_jugar(1)
        if(jugadores == "si"):
            print("Juegan los mismos jugadores, la partida sera aleatoria")
        elif(jugadores == "no"):
            cambio = volver_a_jugar(2)
            if(cambio == "ambos"):
                jugador_1.caracteristicas("Jugador 1, Ingresa tu nombre: ")
                jugador_2.caracteristicas("Jugador 2, Ingresa tu nombre: ")
            elif(cambio == 1):
                jugador_1.caracteristicas("Jugador 1, Ingresa tu nombre: ")
            elif(cambio == 2):
                jugador_2.caracteristicas("Jugador 2, Ingresa tu nombre: ")
        table.jugar(jugador_1,jugador_2)

    elif(reinicio == "no"):#Fin del juego
        print("Gracias por jugar :D")
        inicio = False
