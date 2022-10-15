#create a Maze game!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
            if self.rect.x <=350:
                self.direction = "right"
        else:
            self.rect.x += self.speed
            if self.rect.x > 635:
                self.direction = "left"
        #if self.rect.x < Player.rect.x:
            #self.rect.x += self.speed
        #if self.rect.x > Player.rect.x:
            #self.rect.x -= self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_height, wall_width, wall_x, wall_y):
        super().__init__()
        self.width = wall_width
        self.height = wall_height
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))



window = display.set_mode((700, 500))
display.set_caption('labyrinthe')
backround = transform.scale(image.load("background.jpg"), (700, 500))
hero = Player('hero.png', 5, 80, 4)
enemy = Enemy('cyborg.png', 80, 280, 2)
finish = False

wall1 = Wall(255,255,255,300,20,100,100)
wall2 = Wall(255,255,255,200,20,500,200)
wall3 = Wall(255,255,255,20,300,100,100)

#tresure = GameSprite('tresure.png', 120, 80, 0)

clock = time.Clock()
FPS = 60

#mixer.init()
#mixer.music.load('jungles.ogg')
#mixer.music.play()

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game=False
    
    if finish != True:
        if sprite.collide_rect(hero, enemy) or sprite.collide_rect(hero, wall1) or sprite.collide_rect(hero, wall2) or sprite.collide_rect(hero, wall3):
            finish = True
            kick.play()

    window.blit(backround, (0, 0))
    
    hero.update()  
    enemy.update()  
    
    hero.draw()
    enemy.draw()
#    tresure.draw()
    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
    display.update()
    clock.tick(FPS)
