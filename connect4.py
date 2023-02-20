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

if __name__=="__main__":
    tablero=creaTablero(6,7)
    print(tablero)

