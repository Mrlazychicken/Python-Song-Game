import sys
import pygame
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Predefined some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Song:
    def __init__(self, name, abCover):
        self.name = name
        self.abCover = pygame.image.load("abCover.png")


class SongSelector:
    def __init__(self, sList):
        self.sList = sList

    def findSong(self):
        getSong()
        playSong()


class Game:
    def __init__(self, players, rounds):
        self.players = players
        self.rounds = rounds


# Game Loop, once pygame.display.update() occurs then change happen
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
