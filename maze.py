#создай игру "Лабиринт"!
from pygame import *

window=display.set_mode((700,500))
display.set_caption("Лабиринт")
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick=mixer.Sound("kick.ogg")
money=mixer.Sound("money.ogg")
background=transform.scale(image.load('background.jpg'),(700,500))   
FPS=60

# print(font.get_fonts())

font.init()
font=font.SysFont('arial',70)
win=font.render("Ти виграв!", True, (215, 119, 247))

lose=font.render("Ти програв!", True, (215, 119, 247))
wait = 60

clock=time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, p_speed):
         super().__init__()
         self.image=transform.scale(image.load(p_image),(55,55))
         self.speed=p_speed
         self.rect=self.image.get_rect()
         self.rect.x=p_x
         self.rect.y=p_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y)) 

packman=GameSprite("hero.png", 0, 350, 5)
monster=GameSprite("cyborg.png", 500, 320, 2)

class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y >5:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y <430:
            self.rect.y+=self.speed

packman=Player("hero.png", 0, 416, 5)

class Enemy(GameSprite): 
    direction="left"
    def update(self):
        if self.rect.x <= 470:
            self.direction= "right"
        if self.rect.x >= 570:
            self.direction= "left"

        if self.direction=="left":
            self.rect.x -= self.speed
        if self.direction=="right":
            self.rect.x += self.speed

monster=Enemy("cyborg.png", 500, 320, 3)
treasure=GameSprite("treasure.png", 590, 430, 0)

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2,color_3, wall_x, wall_y, wall_w, wall_h):
         super().__init__()
         self.color_1=color_1
         self.color_2=color_2
         self.color_3=color_3
         self.width=wall_w
         self.height=wall_h
         self.image=Surface((self.width, self.height))
         self.image.fill((color_1,color_2,color_3))
         self.rect=self.image.get_rect()
         self.rect.x=wall_x
         self.rect.y=wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

wall_1=Wall(18,253,104,70,110,9,370)
wall_2=Wall(18,253,104,70,10,600,9)
wall_3=Wall(18,253,104,670,10,9,470)
wall_4=Wall(18,253,104,70,480,500,9)
wall_5=Wall(18,253,104,70,110,35,9)
wall_6=Wall(18,253,104,100,110,9,100)
wall_7=Wall(18,253,104,100,185,9,9)
wall_8=Wall(18,253,104,70,250,240,9)
wall_9=Wall(18,253,104,200,10,9,150)
wall_10=Wall(18,253,104,460,130,9,350)
wall_11=Wall(18,253,104,301,100,9,150)
wall_12=Wall(18,253,104,380,10,9,360)
wall_13=Wall(18,253,104,149,361,240,9)
wall_14=Wall(18,253,104,460,121,100,9)
wall_15=Wall(18,253,104,560,90,9,40)
wall_16=Wall(18,253,104,149,361,9,40)
wall_17=Wall(18,253,104,380,361,9,40)
wall_18=Wall(18,253,104,265,450,9,40)
wall_19=Wall(18,253,104,569,200,110,9)
wall_20=Wall(18,253,104,460,290,110,9)

def collide_rect(left,right):
    return left.rect.colliderect(right.rect)


game=True
finish=False
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False

    if finish != True:
        window.blit(background,(0,0))
        packman.reset()
        packman.update()
        monster.reset()
        monster.update()
        treasure.reset()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()
        wall_6.draw_wall()
        wall_7.draw_wall()
        wall_8.draw_wall()
        wall_9.draw_wall()
        wall_10.draw_wall()
        wall_11.draw_wall()
        wall_12.draw_wall()
        wall_13.draw_wall()
        wall_14.draw_wall()
        wall_15.draw_wall()
        wall_16.draw_wall()
        wall_17.draw_wall()
        wall_18.draw_wall()
        wall_19.draw_wall()
        wall_20.draw_wall()

        if sprite.collide_rect(packman,monster) or sprite.collide_rect(packman,wall_1) or sprite.collide_rect(packman,wall_2) or sprite.collide_rect(packman,wall_3) or sprite.collide_rect(packman,wall_4) or sprite.collide_rect(packman,wall_5) or sprite.collide_rect(packman,wall_6) or sprite.collide_rect(packman,wall_7) or sprite.collide_rect(packman,wall_8) or sprite.collide_rect(packman,wall_9) or sprite.collide_rect(packman,wall_10) or sprite.collide_rect(packman,wall_11) or sprite.collide_rect(packman,wall_12) or sprite.collide_rect(packman,wall_13) or sprite.collide_rect(packman,wall_14) or sprite.collide_rect(packman,wall_15) or sprite.collide_rect(packman,wall_16) or sprite.collide_rect(packman,wall_17) or sprite.collide_rect(packman,wall_18) or sprite.collide_rect(packman,wall_19) or sprite.collide_rect(packman,wall_20):
            window.blit(background,(0,0))
            wait = 60
            window.blit(lose, (200,200))
            finish=True
            kick.play()
            packman=Player("hero.png", 0, 416, 5)

        if sprite.collide_rect(packman,treasure):
            window.blit(background,(0,0))
            wait = 60
            window.blit(win, (200,200))
            finish=True
            money.play()

    if wait>0:
        wait=wait-1
    if wait==0:
        finish=False
        wait=-1


    
    clock.tick(FPS)
    display.update()