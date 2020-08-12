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

class tablero:
    def __init__(self):
        self.tablero = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.muestraTablero()
        self.cuenta = 0
        self.final = False
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
    def PosiY(self):
        try:
            y = int(input("Ingresa Valor Y: "))
            if (y == 0 or y == 1 or y == 2):
                return y
            else:
                print("Valor fuera de rango")
                y = self.posiY()
                return x
        except ValueError:
                print("Valor fuera de rango")
                self.posiY()
    
    def agregaEstado(self,estado, jugador):
        print("Turno de "+jugador)
        self.x = self.posiX()
        self.y = self.PosiY()
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
if __name__ == "__main__":
    player1=jugador(input("Nombre del Jugador 1: "),"O", True)
    player2=jugador(input("Nombre del Jugador 2: "),"X", False)
    tabl = tablero()
    turno = True
    while (tabl.regresaCuenta() < 9):
        if(turno == player1.regresaTurno()):
            tabl.agregaEstado(player1.regresaEstado(), player1.regresaName())
        else:
            tabl.agregaEstado(player2.regresaEstado(), player2.regresaName())
        if(tabl.regresaFinal()==True):
            if (turno == True):
                print(player2.regresaName()+" eres el rival mas debil, Adios")
            else:
                print(player1.regresaName()+" eres el rival mas debil, Adios ")
            break
        turno = not turno
        tabl.agregaCuenta()
    if (tabl.checaGanador == False):
        print("Nadie Ganó")    
    