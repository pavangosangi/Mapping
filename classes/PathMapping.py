from classes.vertex import Spot
import math

class Path:
	def __init__(self,row,col):
		self.row = row
		self.col = col
		self.grid = [0]*row
		for i in range(row):
			self.grid[i] = [0] * col

		for i in range(row):
			for j in range(col):
				self.grid[i][j] = Spot(i,j)

		for i in range(row):
			for j in range(col):
				self.grid[i][j].addNeighbors(self.grid,row,col)

	def getGrid(self):
		return self.grid

	def heuristic(self,a,b):
		return math.sqrt((a.i-b.i)**2 + (a.j-b.j)**2)

	def calculatePath(self,start,end):
		openSet = []
		closedSet = []
		path = []
		start.wall = False
		end.wall = False
		openSet.append(start)
		pathFound = False
		print("calcPath")
		while not pathFound:
			if len(openSet) > 0:
				winner = 0;
				for i in range(len(openSet)):
					if openSet[i].f < openSet[winner].f:
						winner = i

				current = openSet[winner]
				if current == end:
					temp = current
					path.append(temp)
					while temp.previous:
						path.append(temp.previous)
						temp = temp.previous
					print("Done")
					pathFound = True

				openSet.remove(current)
				closedSet.append(current)

				neighbors = current.neighbors
				for i in range(len(neighbors)):
					neighbor = neighbors[i]
					if neighbor not in closedSet:
						tempG = current.g + 1
						newPath = False
						if neighbor in openSet:
							if tempG < neighbor.g:
								neighbor.g = tempG
								newPath = True
						else:
							neighbor.g = tempG
							newPath = True
							openSet.append(neighbor)
						if newPath:
							neighbor.h = self.heuristic(neighbor,end)
							neighbor.f = neighbor.g + neighbor.h
							neighbor.previous = current

		return path