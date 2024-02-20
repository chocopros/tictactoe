import pygame

#Inicializar pygame
pygame.init()

#crear ventana de interaccion
screen = pygame.display.set_mode((450,450))

#Titulo del juego
pygame.display.set_caption('Tc Tac Toe Jchock')

#Carga de Recursos Staticos de carpeta static/
fondo = pygame.image.load('static/tictactoe_background.png')