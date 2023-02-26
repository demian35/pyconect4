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
        print("es turno de " + turno)
        if(turno== "A"):##cambio de turno
            turno= "R"##piezas rojas
            print("es turno de " + turno)
        else:
            turno="A"
            



if __name__=="__main__":
    main()

