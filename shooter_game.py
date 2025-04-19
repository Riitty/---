#Создай собственный Шутер!

from pygame import *
from random import random, randint

window = display.set_mode((700,500))
display.set_caption('ping-pong')
background = transform.scale(image.load('istockphoto-904853290-612x612.jpg'), (700,500))
mixer.init()
mixer.music.load('b6c47dcdd5bd8ea.mp3')
mixer.music.set_volume(0.2)
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_height, player_width, player_image, player_speed, player_x, player_y):
        super().__init__()
        self.height = player_height
        self.width = player_width
        self.image = transform.scale(image.load(player_image), (self.height, self.width))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_height, player_width, player_image, player_speed, player_x, player_y):
        super().__init__(player_height, player_width, player_image, player_speed, player_x, player_y)
    def move_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 300:
            self.rect.y += self.speed
    def move_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed

player1 = Player(20, 200,'7613952.png', 5, 30, 250)
player2 = Player(20, 200,'7613952.png', 5, 650, 250)


clock = time.Clock()
FPS = 120
game = True
finish = False

while game != False:
    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)

    if finish != True:
        window.blit(background, (0,0))
        player1.reset()
        player1.move_1()
        player2.reset()
        player2.move_2()

    display.update()