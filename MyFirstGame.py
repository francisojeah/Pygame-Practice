#pygame coordinates are from the top left
import pygame
'''
Always use .init() method when using pygame
It initializes pygame
'''
pygame.init()

#To create window to draw in (width,height)
screenWidth = 650
screenHeight = 650
window = pygame.display.set_mode((screenWidth,screenHeight))
#To name the window
pygame.display.set_caption("My First game")

#To load an image in pygame we use pygame.image.load(Path)
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

#x and y are positions
x = 200 
y = 200
width = 60
height = 80
velocity = 20 # how fast the character moves

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0
#Always make a main loop when using pygame
run = True
while run:
    pygame.time.delay(200)#.delay() delays the game by the value given in milliseconds
    
    for event in pygame.event.get():#This gets a list of events that happen, mouse and keyboard
        if event.type ==pygame.QUIT:# if The big red 'X' button is clicked
            run = False #Ends loop

    keys = pygame.key.get_pressed()#a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.
    
    # To check what keys have been pressed and prevent box from leaving screen
    if keys[pygame.K_LEFT] and x >= velocity:
        x -= velocity

    if keys[pygame.K_RIGHT] and x < screenWidth - width - velocity:
        x += velocity

    #To allow users to not move up, down, or jump while in mid air
    if not(isJump):
        if keys[pygame.K_UP] and y >= velocity:
            y -= velocity

        if keys[pygame.K_DOWN] and y < screenHeight - height - velocity:
            y += velocity
        #Allows to jump with spacebar
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        '''
        This is the program that controls the jump. The shape goes up and down
        How it goes up; 10*10 = 100/2 = 50. Does this for 9,8,7 and so on and y is reducing and updating
        if sustains in mid air for a while because of little or no change in values of y, e.g jumpcpunt = 0,1,2
        how it goes up; as jumpCount is -ve, -5*5 = -25/2 = -12.5. that woule be -x- which is +, so it goes down
        '''
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1

        else: #This will run if jump is finished
            isJump = False 
            jumpCount = 10

   
    #To fill the screen with black to cover previous shapes .fill(colour) is used
    window.fill((0,0,0))

    #To draw a rectangle => surface,color,rect
    pygame.draw.rect(window, (0,255,0), (x,y,width,height))
    #To update screen
    pygame.display.update()

pygame.quit() #close game


