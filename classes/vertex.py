import random

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


	def addNeighbors(self,grid,row,col):
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