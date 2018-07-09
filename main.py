import pygame
import math
from classes.PathMapping import Path
from classes.vertex import Spot

pygame.init()
screen_width = 800
screen_height = 800
gameDisplay = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Roomba Mapping')
image_orig = pygame.image.load('roomba.png')
image = image_orig.copy()
angle=10
current_roomba_x = 200
current_roomba_y = 200
new_roomba_x = 0
new_roomba_y = 0
path=[]

clock = pygame.time.Clock()

crashed = False
GRAY = (139,137,137)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
pathCounter=0

pathObj = Path(int(screen_width/5),int(screen_height/5))

def drawRoom():
	room_width = 390
	room_height = 780
	wall_thickness = 10
	pygame.draw.rect(gameDisplay, GRAY, [10,10,room_width,room_height],wall_thickness)


def rotateRoomba(x1,y1):
	x2,y2 = pygame.mouse.get_pos()
	deltax = (x2-x1)
	deltay = -(y2-y1)
	angle_rad = math.atan2(deltay,deltax)
	angle_deg = angle_rad*180.0/math.pi
	return angle_deg

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

		if event.type == pygame.MOUSEMOTION:
			rotate_angle = rotateRoomba(current_roomba_x,current_roomba_y)

		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			path=[]
			pathCounter=0
			new_roomba_x,new_roomba_y = event.pos
			grid = pathObj.getGrid()
			print(grid[int(current_roomba_x/5)][int(current_roomba_y/5)],grid[int(new_roomba_x/5)][int(new_roomba_y/5)])
			path = pathObj.calculatePath(grid[int(current_roomba_x/5)][int(current_roomba_y/5)],grid[int(new_roomba_x/5)][int(new_roomba_y/5)])
			print(path)
			path = list(reversed(path))
			
	
	gameDisplay.fill(WHITE)
	drawRoom()
	image = pygame.transform.rotate(image_orig,rotate_angle)
	image_circle = pygame.draw.circle(gameDisplay,RED,[current_roomba_x,current_roomba_y],35,1)
	if len(path)>0:
		current_roomba_x = path[pathCounter].i * 5
		current_roomba_y = path[pathCounter].j * 5
		pathCounter +=1
	if len(path) == pathCounter:
		pathCounter = 0
		path=[]
	image_rect = image.get_rect(center=(current_roomba_x,current_roomba_y))
	gameDisplay.blit(image,image_rect)
	pygame.display.flip()
	clock.tick(30)

pygame.quit()
quit()