from pygame import *
from random import random, randint

window = display.set_mode((700,500))
display.set_caption('ping-pong')
background = transform.scale(image.load('istockphoto-904853290-612x612.jpg'), (700,500))
mixer.init()
mixer.music.load('b6c47dcdd5bd8ea.mp3')
mixer.music.set_volume(0.2)
mixer.music.play()
score_1 = 0
score_2 = 0
win_player = None
font.init()
shr = font.Font(None, 30)
shr2 = font.Font(None, 100)
print_score_1 = shr.render(f'Счёт: {score_1}', True, (255,255,255))
print_score_2 = shr.render(f'Счёт: {score_2}', True, (255,255,255))

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

class Ball(GameSprite):
    def __init__(self, player_height, player_width, player_image, player_speed, player_x, player_y, player_speed_x, player_speed_y):
        super().__init__(player_height, player_width, player_image, player_speed, player_x, player_y)
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
    def update(self):
        if self.rect.y < 490 and self.rect.y > 10:
            self.rect.y += self.speed_y
        if self.rect.x < 690 and self.rect.x > 10:
            self.rect.x += self.speed_x
        



player1 = Player(20, 200,'7613952.png', 5, 30, 250)
player2 = Player(20, 200,'7613952.png', 5, 650, 250)
wall1 = Player(700, 1, '7613952.png', None, 0, 499)
wall2 = Player(700, 1, '7613952.png', None, 0, 15)
wall3 = Player(1, 500, '7613952.png', None, 10, 0)
wall4 = Player(1, 500, '7613952.png', None, 690, 0)
ball = Ball(20,20, 'ball.png', None, 350, 250, 5, 5)


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
        wall1.reset()
        wall2.reset()
        wall3.reset()
        wall4.reset()
        player1.reset()
        player1.move_1()
        player2.reset()
        player2.move_2()
        ball.reset()
        ball.update()
        window.blit(print_score_1, (20, 20))
        window.blit(print_score_2, (600, 20))

        if sprite.collide_rect(ball, wall1) or sprite.collide_rect(ball, wall2):
            ball.speed_y = -ball.speed_y
        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
            ball.speed_x = -ball.speed_x
        if sprite.collide_rect(ball, wall3):
            ball.rect.x = 350
            ball.rect.y = 250
            score_2 += 1
            print_score_2 = shr.render(f'Счёт: {score_2}', True, (255,255,255))
        if sprite.collide_rect(ball, wall4):
            ball.rect.x = 350
            ball.rect.y = 250
            score_1 += 1
            print_score_1 = shr.render(f'Счёт: {score_1}', True, (255,255,255))
        if score_1 >= 10:
            win_player = 'Игрок 1'
            win = shr2.render(f'Победил {win_player}!', True, (255,0,0))
            window.blit(win, (70, 200))
            finish = True
        elif score_2 >= 10:
            win_player = 'Игрок 2'
            win = shr2.render(f'Победил {win_player}!', True, (255,0,0))
            window.blit(win, (70, 200))
            finish = True
    display.update()
