import pygame

#Inicializar pygame
pygame.init()

#crear ventana de interaccion
screen = pygame.display.set_mode((450,450))

#Titulo del juego
pygame.display.set_caption('Tc Tac Toe Jchock')

#Carga de Recursos Staticos de carpeta static/
fondo = pygame.image.load('static/tictactoe_background.png')
circulo = pygame.image.load('static/circle.png')
equis = pygame.image.load('static/x.png')

#dimensionar o escalar las imagenes, ajustes
fondo = pygame.transform.scale(fondo, (450,450))
circulo = pygame.transform.scale(circulo, (125,125))
equis = pygame.transform.scale(equis, (125,125))

#creamos un clock donde se habilitara los frames*seg de nuestro juego
clock = pygame.time.Clock()


#! LOGICA DEL JUEGO
#Coordenada de Tupplas donde lso elementos se van a graficar
coor = [[(40,50),(165,50),(290,50)],
        [(40,175),(165,175),(290,175)],
        [(40,300),(165,300),(290,300)]]

#Donde se van a almacenas las jugadas y la logica del juego
tablero = [['','','O'],
           ['','',''],
           ['X','','']]


#* graficar o renderizar las x y la y
def dibujar_x(fila,col):
    screen.blit(equis, coor[fila][col])

def dibujar_o(fila,col):
    screen.blit(circulo, coor[fila][col])

def graficar_board():
    screen.blit(fondo, (0,0))

    for fila in range (3):
        for col in range(3):
            if tablero [fila][col] == 'X':
                dibujar_x(fila,col)
            if tablero [fila][col] == 'O':
                dibujar_o(fila,col)



#* Definir los turnos de Los jugadores
#al colocar la x, siempre iniciara esta
turno = 'X'

#variable de control que si el juego esta o no terminado o en funcionamiento
game_over = False

#donde se vizualzia todos lso frames del juego
while not game_over:
    #definiciendo los30 fps
    clock.tick(30)

    #Captura todos los eventos de la interaccion anterior
    for event in pygame.event.get():
        #Evento de click en exit o bton cerrar
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            #print(mouseX,mouseY)
            if (mouseX >= 40 and mouseX < 415) and (mouseY >= 50 and mouseY < 425):
                print(mouseX,mouseY)
                
    graficar_board()

    #Actualizamos nuestro frame
    pygame.display.update()

    

pygame.quit()