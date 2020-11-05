import random
import numpy as np
import pandas as pd
import sys
import pygame
#GAME OF LIFE
#If a living cell has fewer than 2 or greater than 3 neighbours, it dies
#If an empty cell has 3 neighbours exactly, it becomes living
print("Running")
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Game of Life')
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT+20))
w = 20
Wide = int(WIDTH/w)
Height = int(HEIGHT/w)
grid = [[1]*Wide for n in range(Height)]
Game = np.random.randint(0,2, size=(Height,Wide))
print(np.sum(Game))

def Neighbours(Game):
    Game1 = Game.copy()
    k = 0
    for a in range(Height):
        for b in range(Wide):
            for c in range(-1, 2):
                for d in range(-1,2):
                    if (a+c>=0 and b+d>=0) and (a+c<Height and b+d<Wide) and (c!=0 or d!=0):
                        if Game[a+c][b+d] == 1:
                            k = k + 1
            Game1[a,b]=k
            k=0
    return Game1
def LifeorDeath(Game, Game1):
    for a in range(Height):
        for b in range(Wide):
            for c in range(-1, 2):
                for d in range(-1,2):
                    if (a + c >= 0 and b+d >= 0) and (a + c < Height and b + d < Wide):
                        if Game[a][b] ==0:
                            if Game1[a][b]==3:
                                Game[a][b]=1
                        elif Game[a][b]==1:
                            if Game1[a][b]!=2 and Game1[a][b]!=3:
                                Game[a][b] = 0
    return Game
def Draw_Game(Game):
    screen.fill((255, 255, 255))
    for a in range(Height):
        for b in range(Wide):
            if Game[a][b]==1:
                pygame.draw.rect(screen,(0,0,200),(a*w,b*w,w,w))
Iterations = 1000
for k in range(Iterations):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(np.sum(Game))
            sys.exit()
    N = Neighbours(Game)
    Game = LifeorDeath(Game, N)
    Draw_Game(Game)
    pygame.display.update()
    clock.tick(20)
print(np.sum(Game))