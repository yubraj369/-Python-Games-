import pygame 
import math 
import random 
from pygame import mixer 

# init pygame

pygame.init()

#create screen 

width = 800 
height = 600 

screen  = pygame.display.set_mode((width , height ))

#background sound 

mixer.music.load("background.wav")
mixer.music.play(-1)

 #player 
player_img = pygame.image.load("player.png")
player_x = 370
player_y = 480
playerx_change = 0 
playery_change = 0 

 #enemy  



 
enemy_img = []
enemy_x = []
enemy_y = []
enemyx_change =[]
enemyy_change =[]
no_of_enemies = 6

for i in range (no_of_enemies):
    enemy_img.append(pygame.image.load("enemy.png"))
    enemy_x.append( random.randint(0,700))
    enemy_y.append( random.randint(0,300))
    enemyx_change.append(1.5) 
    enemyy_change.append(40)

 #bullets  
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 480
bulletx_change = 1.5
bullety_change = 4
bullet_state = "ready"

#score and game over fonts 

score = 0 
font = pygame.font.Font("sysfont.ttf" , 32 )
over_text = pygame.font.Font("sysfont.ttf" , 50 )

textx = 10
texty = 10 

def game_over_txt(x,y ):
    game_over = over_text.render("GAME OVER ", True , (255,255,255))
    screen.blit(game_over , (x,y)) 

def player(x,y):
    screen.blit(player_img, (player_x , player_y))

#enemy 


def enemy(x,y , i):
    screen.blit(enemy_img[i], (x , y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img , ( x+16 , y+10 ))

def iscollision(x,y,w,z):
    distance = math.sqrt(math.pow( enemy_x[i] - bullet_x,2) + math.pow(enemy_y[i] - bullet_y,2))
    if distance <=27 : 
        return True 
    else:
        return False


def show_score (x , y ) :
    score_render = font.render("Score : " +str (score), True , (255,255,255))
    screen.blit(score_render , (x, y))


 #set logo icon and caption 

logo = pygame.image.load("icon.png")
pygame.display.set_icon(logo)

pygame.display.set_caption("space invaders ")

background = pygame.image.load("background.jpg")


running = True 
  
#game  loop 

while running: 
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_SPACE:
                bulletsound = mixer.Sound("laser.wav")
                bulletsound.play()
                if bullet_state == "ready":
                        bullet_x =  player_x
                        fire_bullet(player_x, bullet_y) 

        if event.type == pygame.KEYUP:
               if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerx_change = 0
    
    player_x += playerx_change
    
    if player_x <=0 :
        player_x = 0 
    elif player_x >= 736:
        player_x = 736

#enemy movement 


    for i in range (no_of_enemies):

        #game over 
        if enemy_y[i] > (player_y -50):
            for j in range (no_of_enemies):
                enemy_y[i] = 2000 
            game_over_txt(300,300)
            break
        enemy_x[i] += enemyx_change[i]
        
        if enemy_x[i] <=0 :
            enemyx_change[i] = 1.5
            enemy_y[i] +=enemyy_change[i]

        elif enemy_x [i]>= 736:
            enemyx_change[i] = -1.5
            enemy_y[i] +=enemyy_change[i]
                #collision
        collision = iscollision(enemy_x[i] , enemy_y [i], bullet_x , bullet_y)
        if collision : 
            collisionsound = mixer.Sound("explosion.wav")
            collisionsound.play()
            bullet_y = 480
            bullet_state =  "ready"
            score+=10 
            
            enemy_x[i] = random.randint(0,700)
            enemy_y[i] = random.randint(0,300)

        enemy(enemy_x[i],enemy_y[i] , i)


    #bullet movement  
    if bullet_y <=0 :
        bullet_y = 480 
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bullet_x , bullet_y)
        bullet_y -=bullety_change

   
    player(player_x,player_y)
    show_score(textx , texty)
    pygame.display.update()

