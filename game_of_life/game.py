
import pygame, sys, os
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((720, 576)) #okno
pygame.display.set_caption('Gra w pyGame') #etykieta
graphic = pygame.image.load("d3.png") #ladowanie pliku graficznego
screen = pygame.display.get_surface() #pobieranie informacji o ekranie
screen.blit(graphic, (0, 0)) #przypisanie grafiki(grahic) do konkretngo miejsca na ekracjie
pygame.display.flip()


def input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        else:
            print event

while True:
    input(pygame.event.get())