__author__ = 'Kuba'

from threading import Thread


game_board=[]
tmp=[]

for a in range(200):
    for b in range(200):
        tmp.insert(b, 0)
    game_board.append(tmp)
    tmp = []

class Game(Thread):
    def __init__(self, start, radius, entitys, color):
        self.start=start
        self.radius=radius
        self.entitys = entitys
        self.color = color

    def check(self, i, j):
        for x in (i+1):
            for y in (j+1):


    def run(self):
        for i in range(200):
            for j in range(200):
                if (i and j is 0):
                    if()


