import pygame

pygame.init

FPS                 = 60
WIDTH, HEIGHT       = 1000, 800                         #Define the sizes of the screen
WIDTHBTN, HEIGHTBTN = 100, 30                           #Define the sizes of the buttons
screen              = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Yosephus Plavious')
clock               = pygame.time.Clock()
start_pos           = pygame.Rect(50, HEIGHT-50,50,50) #Possision of the start button

