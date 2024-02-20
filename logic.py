
tablero = [['x','x','x'],
           ['','','']]

# print(tablero[0])
# print(tablero[1])

for i in range(2):
    if tablero[i][0] == tablero[i][1] == tablero[i][2] != '':
        print(f'ganador {tablero[i][1]}')


