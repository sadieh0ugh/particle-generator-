import pygame
import random
done = False
screen = pygame.display.set_mode([700,500])
count = 0
def place():
    global locs,speeds,size,tone
    locs = []
    speeds = []
    size = []
    tone = []
    for i in range(100):
        x = random.randrange(700)
        y = random.randrange(500)
        locs.append([x,y])
        speedx = random.randrange(-1,1)
        speedy = random.randrange(-2,2)
        if speedx == 0:
            speedx += 1
        elif speedy == 0:
            speedx -= 1
        speeds.append([speedx,speedy])
        s = random.randrange(2,13)
        size.append(s)
        val = 255-(s*20)
        tone.append([0,val,0])
def move():
    for i in range(len(locs)):
        locs[i][1] += speeds[i][1]
        locs[i][0] += speeds[i][0]
        pygame.draw.circle(screen,tone[i],locs[i],size[i])
        if locs[i][1] > 500 or locs[i][1] < 0:
            speeds[i][1] *= -1
        elif locs[i][0] > 700 or locs[i][0] < 0:
            speeds[i][0] *= -1
place()
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill([0,0,0])
    move()
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()

# change tone
