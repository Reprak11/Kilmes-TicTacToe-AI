import random
import numpy as np

class jugador:
    def __init__(self, name, estado, turno):
        self.name = name
        self.estado = estado
        self.turno = turno
    def regresaTurno(self):
        return self.turno
    def regresaEstado(self):
        return self.estado
    def regresaName(self):
        return self.name

class pc:
    def __init__(self, estado, turno):
        self.name = 'miniT4ynis'
        self.estado = estado
        self.turno = turno
    def regresaTurno(self):
        return self.turno
    def regresaEstado(self):
        return self.estado
    def regresaName(self):
        return self.name

class tablero:
    def __init__(self):
        self.tablero = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.muestraTablero()
        self.cuenta = 0
        self.final = False
    def setModoJuego(self,formaJuego):
        self.formaJuego = formaJuego
    def setDificultad(self):
        try:
            difi = int(input("Seleccione Dificultad\n1: Facil\n2: Dificil\n"))
            if (difi == 1 or difi == 2):
                self.dificultad = difi
            else:
                print("Valor fuera de rango")
                self.setDificultad() 
        except ValueError:
            print("Valor fuera de rango")
            self.setDificultad()
    def regresaDificutad(self):
        return self.dificultad
    def muestraTablero(self):
        for i in range(0,len(self.tablero)):
            fila=""
            for j in range(0,len(self.tablero[0])):
                fila += str(self.tablero[i][j])
                if (j!=len(self.tablero[0])-1):
                    fila += "|"
            print(fila)
            if (i!= len(self.tablero)-1):
                print("─────")
        print("\n")

    def posiX(self):
        try:
            x = int(input("Ingresa Valor X: "))
            if (x == 0 or x == 1 or x == 2):
                return x
            else:
                print("Valor fuera de rango")
                x = self.posiX()
                return x
        except ValueError:
                print("Valor fuera de rango")
                self.posiX()
    def posiY(self):
        try:
            y = int(input("Ingresa Valor Y: "))
            if (y == 0 or y == 1 or y == 2):
                return y
            else:
                print("Valor fuera de rango")
                y = self.posiY()
                return y
        except ValueError:
                print("Valor fuera de rango")
                self.posiY()
    def randomPos(self):
        return random.randint(0,2)

    def cambiaEstado(self,estado):
        if(estado == "X"):
            estado = "O"
        else:
            estado = "X"
        return estado

    def ticTacTree(self,tablero, estado):
        nodoinicial = tablero
        nodotemp = np.copy(nodoinicial)
        hijos = []
        for i in range(0,3):
            for j in range(0,3):
                if nodoinicial[i][j] == " ":
                    nodotemp[i][j] = estado
                    self.checaGanador(nodotemp,i,j)
                    if (self.checkWinner()):
                        hijos.append([nodotemp])
                        self.changeWinner()
                    else:
                        estado = self.cambiaEstado(estado)
                        nietos = self.ticTacTree(nodotemp,estado)
                        if nietos == []:
                            hijos.append([nodotemp])
                        else:
                            hijos.append([nodotemp,nietos])
                        estado = self.cambiaEstado(estado)
                    nodotemp = np.copy(nodoinicial)
        return hijos

    def evaluaArbol(self, hijos):
        for i in range(0,len(hijos)):
            if (len(hijos[i]) == 1):
                if (type(hijos[i]) == list):
                    print(hijos[i])
                    print()
            else:
                self.evaluaArbol(hijos[i])
        return


    def MiniMax(self, estado):
        if self.cuenta < 4:
            if (self.tablero[0][0] == " "):
                self.tablero[0][0] = estado
                self.muestraTablero()
                self.checaGanador(self.tablero,0,0)
            elif (self.tablero[0][2] == " "):
                self.tablero[0][2] = estado
                self.muestraTablero()
                self.checaGanador(self.tablero,0,2)
            elif (self.tablero[2][0] == " "):
                self.tablero[2][0] = estado
                self.muestraTablero()
                self.checaGanador(self.tablero,2,0)
            elif (self.tablero[2][2] == " "):
                self.tablero[2][2] = estado
                self.muestraTablero()
                self.checaGanador(self.tablero,2,2)
            elif (self.tablero[1][1] == " "):
                self.tablero[1][1] = estado
                self.muestraTablero()
                self.checaGanador(self.tablero,1,1)
        else:
            hijos = self.ticTacTree(self.tablero, estado)
            self.evaluaArbol(hijos)
            self.x = int(input("Valor X"))
            self.y = int(input("Valor Y"))
            if self.tablero[self.x][self.y] == " ":
                self.tablero[self.x][self.y] = estado
                self.muestraTablero()
                self.checaGanador(self.tablero,self.x,self.y)
            else:
                self.MiniMax(estado,jugador)

    def agregaEstado(self,estado, jugador):
        if(self.formaJuego == 1 and jugador == "miniT4ynis"):
            if (self.dificultad == 1):
                self.x = self.randomPos()
                self.y = self.randomPos()
                if self.tablero[self.x][self.y] == " ":
                    self.tablero[self.x][self.y] = estado
                    self.muestraTablero()
                    self.checaGanador(self.tablero,self.x,self.y)
                else:
                    self.agregaEstado(estado,jugador)
            elif (self.dificultad == 2):
                self.MiniMax(estado)
        else:
            print("Turno de "+jugador)
            self.x = self.posiX()
            self.y = self.posiY()
            if self.tablero[self.x][self.y] == " ":
                self.tablero[self.x][self.y] = estado
                self.muestraTablero()
                self.checaGanador(self.tablero,self.x,self.y)
            else:
                print("No seas wey esa casilla ya está ocupada")
                self.agregaEstado(estado,jugador)
        
    def checaGanador(self, tablero,x,y):
            if (tablero[x][0] != " " and  tablero[x][0] == tablero[x][1] and tablero[x][1] == tablero[x][2]):
                self.changeWinner()
            if (tablero[0][y] != " " and  tablero[0][y] == tablero[1][y] and tablero[1][y] == tablero[2][y]):
                self.changeWinner()
            if (tablero[0][0] != " " and tablero[0][0] ==tablero[1][1] and tablero[1][1] == tablero[2][2]):
                self.changeWinner()
            if (tablero[0][2] != " " and tablero[0][2] == tablero[1][1] and tablero[1][1] == tablero[2][0]):
                self.changeWinner()
    def agregaCuenta(self):
        self.cuenta += 1
    def regresaCuenta(self):
        return self.cuenta
    def regresaFinal(self):
        return self.final
    def changeWinner(self):
        self.final = not self.final
    def checkWinner(self):
        return self.final

class Juego:
    def __init__(self):
        self.tabl = tablero()
        self.turno = True
        self.formaJuego=self.modoJuego()
        self.tabl.setModoJuego(self.formaJuego)
        self.player1 = jugador(input("Nombre Player 1: "),'O',True)
        if (self.formaJuego == 1):
            self.tabl.setDificultad()
            self.player2 = pc('X',False)
        else:
            self.player2 = jugador(input("Nombre Player 2: "),'X',False)
        print(self.player1.regresaName())
        print(self.player2.regresaName())
        self.juegoTicTacToe()
    def modoJuego(self):
        try:
            formaJuego = int(input("Modo de Juego\n1:Player vs PC\n2:Player vs Player\n"))
            if (formaJuego != 1 and formaJuego != 2):
                formaJuego = self.modoJuego()
            return formaJuego
        except ValueError:
            print("Valor fuera de rango")
            self.modoJuego()
    def juegoTicTacToe(self):
        while (self.tabl.regresaCuenta() < 9):
            if(self.turno == self.player1.regresaTurno()):
                self.tabl.agregaEstado(self.player1.regresaEstado(), self.player1.regresaName())
            else:
                self.tabl.agregaEstado(self.player2.regresaEstado(), self.player2.regresaName())
            if(self.tabl.regresaFinal()==True):
                if (self.turno == True):
                    print(self.player2.regresaName()+" eres el rival mas debil, Adios")
                else:
                    print(self.player1.regresaName()+" eres el rival mas debil, Adios ")
                break
            self.turno = not self.turno
            self.tabl.agregaCuenta()
        if (self.tabl.checkWinner() == False):
            print("Nadie Ganó")


if __name__ == "__main__":
    juegoGato = Juego()    