import random as rd
def imprimeTablero(gato):
    for i in range(0,len(gato)):
        fila=""
        for j in range(0,len(gato[0])):
            fila += str(gato[i][j])
            if (j!=len(gato[0])-1):
                fila += "|"
        print(fila)
        if (i!= len(gato)-1):
            print("─────────")
    print("\n")

def creaTablero():
    gato=([-1,-1,-1],[-1,-1,-1],[-1,-1,-1])
    imprimeTablero(gato)
    return gato

def defineX():
    checaX = True
    while checaX:
        x=int(input("Pos:x  Valor entre 0-2\n"))
        if(x>=0 and x<3):
            checaX=False
        else:
            print("Valor no válido wey\n")
    return x
def defineY():
    checaY=True
    while checaY:
        y=int(input("Pos:y  Valor entre 0-2\n"))
        if(y>=0 and y<3):
            checaY=False
        else:
            print("Valor no válido wey\n")
    return y
def checaGanador(gato):
    hayGanador=False
    for i in range(0,len(gato)):
        if (gato[i][0] != -1 and gato[i][0] == gato [i][1] and gato[i][1]==gato[i][2]):
            hayGanador=True
            return hayGanador
    if (gato[0][0] != -1 and gato[0][0] == gato[1][0] and gato[1][0] == gato[2][0]) or (gato[0][1] != -1 and gato[0][1] == gato[1][1] and gato[1][1] == gato[2][1]) or (gato[0][2] != -1 and gato[0][2] == gato[1][2] and gato[1][2] == gato[2][2]):
        hayGanador=True
        return hayGanador
    if (gato[0][0] != -1 and gato[0][0] == gato[1][1] and gato[1][1]==gato[2][2]) or (gato[0][2] != -1 and gato[0][2] == gato[1][1] and gato[1][1] == gato[2][0]):
        hayGanador = True
        return hayGanador
    return hayGanador

def juega(gato,turno):
    cuenta=0
    ganador = False
    while(cuenta<9):
        if(turno):
            x=defineX()
            y=defineY()
            while(True):
                if (gato[x][y]==-1):
                    gato[x][y]="X"
                    break;
                else:
                    print("Casilla Ocupada")
                    x=defineX()
                    y=defineY()
                    imprimeTablero()
        else:
            x=rd.randint(0,2)
            y=rd.randint(0,2)
            while(True):
                if (gato[x][y]==-1):
                    gato[x][y]="0"
                    break;
                else:
                    x=rd.randint(0,2)
                    y=rd.randint(0,2)
        ganador=checaGanador(gato)
        if (ganador):
            if(turno):
                print("Gana Jugador")
                break;
            else:
                print("Gana PC")
                break;
        turno = not turno
        cuenta += 1;
        imprimeTablero(gato)
    if (ganador == False):
        print("Empate con sabor a derrota")
if __name__ == "__main__":
    gato=creaTablero()
    turno = True
    juega(gato,turno)