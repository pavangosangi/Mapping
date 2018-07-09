import pygame
from array import *
import math
import random

pygame.init()
screen_width = 800
screen_height = 600
gameDisplay = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('PathFinding')

class Spot:
	def __init__(self,i,j):
		self.i = i
		self.j = j
		self.f=0
		self.g=0
		self.h=0
		self.neighbors = []
		self.previous = []
		self.wall = False

		if random.uniform(0,1)<0.4:
			self.wall = True


	def show(self,color):
		if self.wall:
			# pygame.draw.rect(gameDisplay, GRAY, [self.i*w,self.j*h,w,h],1)
			pygame.draw.rect(gameDisplay, GRAY, [self.i*w,self.j*h,w-2,h-2])
		else:
			# pygame.draw.rect(gameDisplay, WHITE, [self.i*w,self.j*h,w,h],1)
			pygame.draw.rect(gameDisplay, color, [self.i*w,self.j*h,w-2,h-2])

	def addNeighbors(self,grid):
		i = self.i
		j = self.j
		if i<row-1:
			self.neighbors.append(grid[i+1][j])
		if i>0:
			self.neighbors.append(grid[i-1][j])
		if j<col-1:
			self.neighbors.append(grid[i][j+1])
		if j>0:
			self.neighbors.append(grid[i][j-1])
		if i>0 and j>0:
			self.neighbors.append(grid[i-1][j-1])
		if i<col-1 and j>0:
			self.neighbors.append(grid[i+1][j-1])
		if i>0 and j<row-1:
			self.neighbors.append(grid[i-1][j+1])
		if i<col-1 and j<row-1:
			self.neighbors.append(grid[i+1][j+1])



row = 25
col = 25
grid = [0]*row
for i in range(row):
	grid[i] = [0] * col

for i in range(row):
		for j in range(col):
			grid[i][j] = Spot(i,j)

for i in range(row):
		for j in range(col):
			grid[i][j].addNeighbors(grid);

w = screen_width / col
h = screen_height / row

clock = pygame.time.Clock()
crashed = False
GRAY = (139,137,137)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)

openSet = []
closedSet = []
path = []
start = grid[0][0]
end = grid[row-1][col-1]
start.wall = False
end.wall = False
openSet.append(start)
pathFound = False

def heuristic(a,b):
	return math.sqrt((a.i-b.i)**2 + (a.j-b.j)**2)
	# return abs(a.i-b.i) + abs(a.j-b.j)

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
	if pathFound == False:
		gameDisplay.fill(BLACK)
		if len(openSet) > 0:
			winner = 0;
			for i in range(len(openSet)):
				if openSet[i].f < openSet[winner].f:
					winner = i

			current = openSet[winner]
			if current == end:
				print("Done")
				pathFound = True

			openSet.remove(current)
			closedSet.append(current)

			neighbors = current.neighbors
			for i in range(len(neighbors)):
				neighbor = neighbors[i]
				if neighbor not in closedSet and not neighbor.wall:
					tempG = current.g + 1
					newPath = False
					if neighbor in openSet:
						if tempG < neighbor.g:
							neighbor.g = tempG
							mewPath = True
					else:
						neighbor.g = tempG
						newPath = True
						openSet.append(neighbor)
					if newPath:
						neighbor.h = heuristic(neighbor,end)
						neighbor.f = neighbor.g + neighbor.h
						neighbor.previous = current
			path = []
			temp = current
			path.append(temp)
			while temp.previous:
				path.append(temp.previous)
				temp = temp.previous
		for i in range(row):
			for j in range(col):
				grid[i][j].show(WHITE)

		for i in range(len(closedSet)):
			closedSet[i].show(RED)

		for i in range(len(openSet)):
			openSet[i].show(GREEN)

		for i in range(len(path)):
			path[i].show(BLUE)

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
quit()