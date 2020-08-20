import random

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

    def agregaEstado(self,estado, jugador):
        if(self.formaJuego == 1 and jugador == "miniT4ynis"):
            print("Hola")
            self.x = self.randomPos()
            self.y = self.randomPos()
            if self.tablero[self.x][self.y] == " ":
                self.tablero[self.x][self.y] = estado
                self.muestraTablero()
                self.checaGanador(self.x,self.y)
            else:
                self.agregaEstado(estado,jugador)
        else:
            print("Turno de "+jugador)
            self.x = self.posiX()
            self.y = self.posiY()
            if self.tablero[self.x][self.y] == " ":
                self.tablero[self.x][self.y] = estado
                self.muestraTablero()
                self.checaGanador(self.x,self.y)
            else:
                print("No seas wey esa casilla ya está ocupada")
                self.agregaEstado(estado,jugador)
        
    def checaGanador(self, x,y):
            if (self.tablero[x][0] != " " and  self.tablero[x][0] == self.tablero[x][1] and self.tablero[x][1] == self.tablero[x][2]):
                self.changeWinner()
            if (self.tablero[0][y] != " " and  self.tablero[0][y] == self.tablero[1][y] and self.tablero[1][y] == self.tablero[2][y]):
                self.changeWinner()
            if (self.tablero[0][0] != " " and self.tablero[0][0] ==self.tablero[1][1] and self.tablero[1][1] == self.tablero[2][2]):
                self.changeWinner()
            if (self.tablero[0][2] != " " and self.tablero[0][2] == self.tablero[1][1] and self.tablero[1][1] == self.tablero[2][0]):
                self.changeWinner()
    def agregaCuenta(self):
        self.cuenta += 1
    def regresaCuenta(self):
        return self.cuenta
    def regresaFinal(self):
        return self.final
    def changeWinner(self):
        self.final = not self.final

class Juego:
    def __init__(self):
        self.tabl = tablero()
        self.turno = True
        self.formaJuego=self.modoJuego()
        self.tabl.setModoJuego(self.formaJuego)
        self.player1 = jugador(input("Nombre Player 1: "),'O',True)
        if (self.formaJuego == 1):
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
        if (self.tabl.checaGanador == False):
            print("Nadie Ganó")


if __name__ == "__main__":
    juegoGato = Juego()    