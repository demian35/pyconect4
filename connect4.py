#funcion para generar tablero del juego recibe las filas y columas que queremos que tenga el tablero NXM
#guadaremos bits en una lsita para despues de ahi generar en tablero para el conecta 4
def creaTablero(N,M):
    t=[]
    for i in range(N):
        fila=[]
        for j in range(M):
            fila.append(0)
        t.append(fila)
    return t

##funcion que nos permitira imprimir el tablero 
def imprimeTablero(tablero):
     for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=" ")
        print()
     print()
     ##para cada elemento del tablero imprime todos desde el indice 0
     for i in range(len(tablero[0])):
         print(i,end=" ") #contamos las columnas para imprimir los indices y asi poder efectuar las jugadas
     print()

##funcion que detecta un empate
def empate(tablero):
    for i in range(len(tablero[0])):
        if(tablero[0][i]==0):##si todos los elementos de una fila son 0 entonces se sigue el juego
            return False
        else:
            return True ##caso contrario se declara partida emptada

def verificaFila(tablero,i,j):#funcion para verificar fila recibimos el tablero y los indices
    return tablero[i][j]==tablero[i][+1]==tablero[i][j+2]==tablero[i][j+3]!=0

def verificaCol(tablero,i,j):#funcion para verificar columna recibimos el tablero y los indices
    return tablero[i][j]==tablero[i+1][j]==tablero[i+2][j]==tablero[i+3][j]!=0   



def main():
    N=6
    M=7
    tablero=creaTablero(N,M)
    turno="A" ##inicializamos con las piezas amarillas
    while(True):##con cada tirada impiriremos el tablero
        imprimeTablero(tablero) 
        i=int(input("Tire "))##entrada del jugador 
        for j in range(len(tablero)):
            if(tablero[N-1-j][i]==0):
                tablero[N-1-j][i]=turno
                break

        if(empate(tablero)):
            break

        print("es turno de " + turno)
        if(turno== "A"):##cambio de turno
            turno= "R"##piezas rojas
            print("es turno de " + turno)
        else:
            turno="A"
            



if __name__=="__main__":
    main()

