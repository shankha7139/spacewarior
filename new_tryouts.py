import pygame
import random
import math
pygame.init()
background = pygame.image.load('background.png')
screen=pygame.display.set_mode((800,600))
player=pygame.image.load('player.png')
playx=385
playy=495
player_change=0
player_changey=0


dushman=[]
dux=[]
duy=[]
du_change=[]
du_changey=[]
x=5
for i in range(x):
    dushman.append(pygame.image.load('enemy.png'))
    dux.append(random.randint(0,736))
    duy.append(random.randint(0,80))
    du_change.append(2.5)
    du_changey.append(10)
    

    
bullet=pygame.image.load('bullet.png')
bulletx=0
bullety=495
bullet_change=0
bullet_changey=1.2
bullet_state='ready'


score=0
font = pygame.font.Font('freesansbold.ttf',20)
tx=10
ty=10

khatam_font = pygame.font.Font('freesansbold.ttf',64)


def shore(x,y):
    s=font.render("SCORE::"+str(score),True,(255,255,0))
    screen.blit(s,(x,y))

def khallas():
    O=khatam_font.render("GAME OVER",True,(255,255,0))
    screen.blit(O,(200,250))
    
def p(x,y):
    screen.blit(player,(x,y))

def dush(x,y,j):
    screen.blit(dushman[j],(x,y))
    
def bullet_fire(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bullet,(x+16,y+10))

def collide(dux,duy,bulletx,bullety):
    d=math.sqrt((math.pow(dux-bulletx,2))+(math.pow(duy-bullety,2)))
    if d<27:
        return True
    else:
        return False
    
    
    
run=True
while run:
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))

    for e in pygame.event.get():

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT or e.key == pygame.K_a :
                player_change=-0.5

            if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                player_change=0.5

            if e.key == pygame.K_UP or e.key == pygame.K_w:
                player_changey=-0.5
                
            if e.key == pygame.K_DOWN or e.key == pygame.K_s:
                player_changey=0.5
                
            if e.key == pygame.K_SPACE:
                if bullet_state=="ready":
                    bulletx=playx
                    bullet_fire(bulletx,bullety)
                    
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT or e.key == pygame.K_a or e.key == pygame.K_d:
                player_change = 0
            if e.key == pygame.K_UP or e.key == pygame.K_DOWN or e.key == pygame.K_w or e.key == pygame.K_s:
                player_changey = 0
                
        if e.type== pygame.QUIT:
            run= False
            pygame.quit()
            


    playx+=player_change
    #playy+=player_changey
    if playx <= 0:
        playx = 0
    elif playx >= 736:
        playx = 736

    if playy <= 400:
        
        playy = 400
    elif playy >= 536:
        playy = 536
    for j in range(x):

        if duy[j]> 455:
            for k in range (x):
                duy[j]=5000

            khallas()
            break
        
        dux[j]+=du_change[j]
        #duy+=du_changey
        if dux[j] <= 0:
            du_change[j]=0.3
            duy[j]+=du_changey[j]
        elif dux[j] >= 736:
            du_change[j]=-0.3
            
            duy[j]+=du_changey[j]
            
        col=collide(dux[j],duy[j],bulletx,bullety)
        if col:
            bullety=495
            bullet_state="ready"
            score+=1
            print(score)
            dux[j]=random.randint(0,736)
            duy[j]=random.randint(0,80)
    
        dush(dux[j],duy[j],j)
        
    if bullety <= 0:
        bullety = 495
        bullet_state = "ready"

    if bullet_state is "fire":
        bullet_fire(bulletx, bullety)
        bullety -= bullet_changey

        
        
    p(playx,playy)
    shore(tx,ty)
    pygame.display.update()
