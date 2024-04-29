import pygame
import time

def setup():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800

    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption('FinalGame')

    global spaceShipBG
    spaceShipBG = pygame.image.load('Sprites/spaceShipConceptArt2.jpg').convert_alpha()
    global spaceDude
    spaceDude = pygame.image.load('Sprites/spaceDudeCA.png').convert_alpha()
    imgSize = (0.2,0.2)
    pygame.transform.scale(spaceShipBG, imgSize)

    #BG = (50,50,50)
    BG = spaceShipBG

    global idleChar1
    idleChar1 = False
    global index
    index = 0
    global charAniState
    charAniState = 0

    #Start Game
    run = True

def char1Idle(x,y, size, speed, charAniState):
    time.sleep(speed) # frames per Second
    frame1 = pygame.image.load('Sprites/testIdle/stickTest1.png').convert_alpha()
    frame2 = pygame.image.load('Sprites/testIdle/stickTest2.png').convert_alpha()
    frame3 = pygame.image.load('Sprites/testIdle/stickTest3.png').convert_alpha()
    frames = [frame1, frame2, frame3]
    for i in frames:
        pygame.transform.scale(i, size)
    pos = x,y
    global index

    #keep index in range
    if (index >= 2):
        index = 2
    elif (index <= 0):
        index = 0
    else:
        index = index

    #idle animation
    if charAniState == 0:
        if (index == 0):
            screen.blit(frame1, tuple(pos))
            index += 1
        elif (index == 1):
            screen.blit(frame2, tuple(pos))
            index += 1
        elif (index == 2):
            screen.blit(frame3, tuple(pos))
            index = 0
        else:
            return
    else:
        return


run = True
setup()
while run:

    #update background
    #screen.fill(BG)
    bgPOS = 0,0
    spaceDudePOS = -250,100
    screen.blit(spaceShipBG, tuple(bgPOS))
    screen.blit(spaceDude, tuple(spaceDudePOS))


    char1Idle(300,-100, (0.5,0.5), 0.2, 0) #position , size, time Between frames, type of animation (0 = idle)
    
    #even handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        #if event.type == pygame.KEYDOWN:
            #used for testing
            #if event.key == pygame.K_r:
            #    index += 1
            #    #pygame.event.post(pygame.event.Event(drawTest))
            #if event.key == pygame.K_t:
            #    index -= 1
            #    #pygame.event.post(pygame.event.Event(drawTestOff))
    
        #if event.type == drawTest:
        #    idleChar1 = True
        #if event.type == drawTestOff:
        #    idleChar1 = False

    pygame.display.update()

pygame.quit()