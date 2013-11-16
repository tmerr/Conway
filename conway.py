"""Command line Conway's Game of Life."""

# Rules:
# 1. Live cell with less than two neighbors dies.
# 2. Live cell with two or three neighbors lives on.
# 3. Live cell with more than three live neighbors dies.
# 4. Dead cell with exactly three live neighbors becomes a live cell.

from time import sleep
from random import random
import os
from copy import deepcopy

def binaryrandom(chance1):
    return int(random() < chance1)

class Game(object):
    def __init__(self, xsize, ysize, initialboard = None):
        self.xsize, self.ysize = xsize, ysize
        if initialboard:
            self.board = initialboard
        else:
            # randomly generate board
            self.board = [[binaryrandom(.15) for x in range(xsize)] for y in range(ysize)]
        self.tmpboard = deepcopy(self.board)
        self.inbounds = lambda y, x: 0 <= y < ysize and 0 <= x < xsize
        self.pos = lambda y, x: self.board[y][x]

    def update_one(self, y, x):
        """Apply the rules to a single cell at y, x."""      
        numneighbors = 0
        for cury, curx in ((y+1, x), (y-1, x), (y, x-1), (y, x+1),
                        (y-1, x+1), (y+1, x-1), (y+1, x+1), (y-1, x-1)):
            if self.inbounds(cury, curx) and self.pos(cury, curx) == 1:
                numneighbors += 1
        
        if self.board[y][x] == 1:
            # rules 1, 2 and 3
            if numneighbors < 2 or numneighbors > 3:
                self.tmpboard[y][x] = 0
        else:
            # rule 4
            if numneighbors == 3:
                self.tmpboard[y][x] = 1

    def update_all(self):
        """Apply the rules to all cells."""
        for y in range(self.ysize):
            for x in range(self.xsize):
                self.update_one(y, x)
        self.board = deepcopy(self.tmpboard)

    def draw(self):
        """Draw a single frame."""
        dead = ' '
        alive = 'x'
        out = [] 
        for y in self.board:
            outln = []
            for x in y:
                if x == 0:
                    outln.append(dead)
                else:
                    outln.append(alive)
            out.append(''.join(outln))
        print('\n'.join(out))

    def run(self):
        """Draw and update in an infinite loop."""
        while True:
            os.system('cls')
            self.draw()
            sleep(.1)
            self.update_all()

def runglider():
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    game = Game(20, 20, board)
    game.run()

def runrandom():
    game = Game(60, 60)
    game.run()

if __name__ == '__main__':
    runrandom()
