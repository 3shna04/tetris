# Example file showing a circle moving on screen
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 680
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Game Start!')

def drawGrid():
    SCREEN.fill(BLACK)
    blockSize = 40 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((680, 800))
clock = pygame.time.Clock()
running = True
dt = 0
direction_queue = []
existing = []
c=0
i=0
prp , prc = 0, 0

d=[[40,40],[80,40],[40,80],[120,40],[40,120],[80,80],[120,80],[80,120],[120,120]]
colours=["red", "blue", "yellow", "green"]
score = 0

player_pos = pygame.Vector2((screen.get_width() / 2)-20, 0)
initial = pygame.Vector2((screen.get_width() / 2)-20, 0)
w=40
h=40
print(player_pos)
r=random.randint(0,8)
cr=random.randint(0,3)

while running:
    #c=0
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            direction_queue.append(event.key)

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("purple")
    drawGrid()

    for point in range(800,0,-40):
        c = 0
        for l in existing:
            if l[1]+l[3] >= point and point > l[1]:
                c+=l[2]
                #print(point,c)
        if c==680:
            print("in",c,point)
            #print("pre",existing)
            score += 100
            for i in range(0, len(existing)):
                if existing[i][1]<point:
                    if existing[i][1]+existing[i][3]>=point:
                        existing[i][3]-=40    
                    existing[i][1]+=40
        
    for l in existing:
        if l[1] >= 800:
            existing.remove(l)   

    for l in existing:
       rect = pygame.Rect(l[0], l[1], l[2], l[3])
       pygame.draw.rect(screen,l[4],rect,0)
       
    rect = pygame.Rect(player_pos.x,player_pos.y, d[r][0], d[r][1])
    pygame.draw.rect(screen,colours[cr],rect,0)

    for l in existing:
        if l[0]-d[r][0]<player_pos.x and l[0]+l[2]>player_pos.x:
            if player_pos.y+d[r][1]==l[1]:   
                existing.append([player_pos.x,player_pos.y,d[r][0],d[r][1],colours[cr]])
                r=random.randint(0,8)
                cr=random.randint(0,3)
                rect = pygame.Rect(initial.x,initial.y, d[r][0], d[r][1])
                pygame.draw.rect(screen,colours[cr],rect,0)
                player_pos = pygame.Vector2((screen.get_width() / 2)-20,40)

    if player_pos.y+d[r][1]==screen.get_height():
        #print([player_pos.x,player_pos.y])
        existing.append([player_pos.x,player_pos.y,d[r][0],d[r][1],colours[cr]])
        r=random.randint(0,8)
        cr=random.randint(0,3)
        rect = pygame.Rect(initial.x,initial.y, d[r][0], d[r][1])
        pygame.draw.rect(screen,colours[cr],rect)
        player_pos = pygame.Vector2((screen.get_width() / 2)-20,40)
        
    if len(direction_queue) != 0:
        keys = direction_queue[0]
        #print(dt)
        if keys==pygame.K_a:
            player_pos.x = player_pos.x - 40
            counter=1
            #print(player_pos)
        if keys==pygame.K_d:
            player_pos.x = player_pos.x + 40
            counter=1
            #print(player_pos)
        if keys==pygame.K_s:
            player_pos.y += 40
            counter=1
            #print(player_pos)
        direction_queue.clear()

    pygame.display.set_caption('Score: ' + str(score))
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics
    dt = clock.tick(20) / 1000

pygame.quit()