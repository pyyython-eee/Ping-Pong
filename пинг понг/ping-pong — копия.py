#Создай собственный Шутер!
from pygame import *
from random import randint
speed_x = 3
speed_y = 3
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def recet(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed [K_s] and self.rect.y < 620:
            self.rect.y += self.speed  
 

class Player1(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed [K_DOWN] and self.rect.y < 620:
            self.rect.y += self.speed  

    


 
platform = Player('New Piskel (18).png', 30, 30, 2)
platform2 = Player1('New Piskel (18).png', 600, 30, 2)
ball = GameSprite('New Piskel (19).png', 70, 50, 2)
window = display.set_mode((700, 500))
display.set_caption("pygame window")
background = transform.scale(image.load("New Piskel (20).png"), (700, 700))

clock = time.Clock()
FPS = 60

clock.tick(FPS)

game = True 
while game:
    window.blit(background,(0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
            ball.rect.x += speed_x
            ball.rect.y += speed_y
        if ball.rect.y > 700-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(platform, ball) or sprite.collide_rect(platform2, ball):
            speed_x *= -1
    ball.recet()
    ball.update()
    platform.recet()
    platform.update() 
    platform2.recet()
    platform2.update() 
    display.update() 



