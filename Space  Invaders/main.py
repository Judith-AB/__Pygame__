import pygame
import random
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((800,600))
run=True
#Title
pygame.display.set_caption("---SPACE---")

#Background and sound effects
bg = pygame.transform.scale(pygame.image.load('background.jpg'), (800, 600))
laser_sound = mixer.Sound('laser.mp3')
hit_sound = mixer.Sound('hit.mp3')

#sound
mixer.music.load('backgroundmusic.mp3')
mixer.music.play(-1)  # -1 means the music will loop indefinitely
mixer.music.set_volume(0.3)  # Set volume (0.0 to 1.0)  


pygame.display.set_caption("Space Shooter Game")


#Icon
icon=pygame.image.load('startup.png')
pygame.display.set_icon(icon)
#Player
plyrimg=pygame.image.load('spaceship.png')
plx=370
ply=500
pl_change=0

#Enemy
enemyimg=[]
enx=[]
eny=[]
enx_change=[]
eny_change=[]
enemy_count = 6  # Number of enemies
for i in range(enemy_count):
    enemyimg.append(pygame.image.load('art.png')) 
    enx.append(random.randint(0,736))
    eny.append(random.randint(50,150))
    enx_change.append(2)
    eny_change.append(40)



#Bullet
bulletimg=pygame.image.load('war.png')
bullet_x=0
bullet_y=480

bullet_y_change=2
bullet_state="ready"  #ready - you can't see the bullet, fire - bullet is moving
score=0
font=pygame.font.Font('freesansbold.ttf', 25)

# Function to display the score on the screen
def show_score(x,y):
    score_text = font.render("Score :" + str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))

def player(x,y):
    screen.blit(plyrimg,(x,y))   #blit: to draw


def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def bullet(x,y):
    screen.blit(bulletimg,(x,y))
def  fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x+16,y+10))  # +16 and +10 to center the bullet on the player ship
#Collision Detection

def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2) ** 0.5
    if distance < 27:  
        return True
    else:
        return False
     
#Game Loop
while run:
    screen.blit(bg, (0, 0))
    dark_overlay = pygame.Surface((800, 600))     # Size of the screen
    dark_overlay.set_alpha(100)                   # 0 = fully transparent, 255 = fully opaque
    dark_overlay.fill((0, 0, 0))                  # Must fill with black
    screen.blit(dark_overlay, (0, 0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        #checking the key pressed is right/left
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                pl_change=1.5
            if event.key==pygame.K_LEFT:
                pl_change=-1.5
            if event.key==pygame.K_SPACE:
                if bullet_state=="ready":
                    laser_sound.play()
                    bullet_x   = plx
                    fire_bullet(bullet_x,bullet_y)
 
            
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                pl_change=0

    plx+=pl_change                 #boundary check
    if plx<=0:
        plx=0
    elif plx>=736:
        plx=736

    for i in range(enemy_count):

        #Game Over Condition
        if eny[i] > 455:
            for j in range(enemy_count):
                eny[j] = 2000
            font_game_over = pygame.font.Font('freesansbold.ttf', 64)
            game_over_text = font_game_over.render("GAME OVER", True, (255, 0, 0))
            screen.blit(game_over_text, (200, 250))  # Center the text
            pygame.display.update()  
            pygame.time.delay(2000)
            run = False
        #Enemy Movement
        enx[i] += enx_change[i]
        if enx[i] <= 0:
            enx_change[i] = 2
            eny[i] += eny_change[i]
        elif enx[i] >= 736:
            enx_change[i] = -2
            eny[i] += eny_change[i]
          
        #Collision
        collision = isCollision(enx[i], eny[i], bullet_x, bullet_y)
        if collision:
            hit_sound.play()
            bullet_y = 480
            bullet_state = "ready"
            score+=1
            # print("Score:", score)
            # Reset enemy position after collision  
            enx[i] = random.randint(0, 736)
            eny[i] = random.randint(50, 150)
        enemy(enx[i],eny[i],i)
   
    #Bullet Movement
    if bullet_state=="fire":
        fire_bullet(bullet_x,bullet_y)
        bullet_y-=bullet_y_change
    
    if bullet_y<=0: 
        bullet_y=480
        bullet_state="ready"
  
  
    player(plx,ply)
    show_score(10, 10)  # Display the score at position (10, 10)
    
    pygame.display.update()



   