from pygame import *
from random import randint

window = display.set_mode((500,600))
window.fill((68, 227, 219))

class GameSprite(sprite.Sprite):
    def __init__(self, player_speed, player_image, player_x, player_y):
        super().__init__()
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image),(95,75))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, player_speed, player_image, player_x, player_y):
        super().__init__(player_speed, player_image, player_x, player_y)
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image),(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and gs.rect.x > 1:
            gs.rect.x -= 10
        if keys_pressed[K_d] and gs.rect.x < 400:
            gs.rect.x += 10
        if keys_pressed[K_SPACE] and gs.rect.y > 1:
            gs.rect.y -= 10

lost = 0
class Platform(GameSprite):
    def __init__(self, player_speed, player_image, player_x, player_y):
        super().__init__(player_speed, player_image, player_x, player_y)
        self.image = transform.scale(image.load(player_image), (200, 220))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 400:
            self.rect.y = 0
            self.rect.x = randint(80, 500 - 80)
            lost += 1

clock = time.Clock()
fps = 60

platforms = sprite.Group()

gs = Player(5, 'player.png', 220, 250)

plf = Platform(randint(2,3), 'plf.png', 210, 245)

platf_1 = Platform(randint(1,2), 'plf.png', randint(100, 400), randint(10, 50))
platf_2 = Platform(randint(1,2), 'plf.png', randint(100, 400), randint(10, 50))
platf_3 = Platform(randint(1,2), 'plf.png', randint(100, 400), randint(10, 50))
platf_4 = Platform(randint(1,2), 'plf.png', randint(100, 400), randint(10, 50))
platf_5 = Platform(randint(1,2), 'plf.png', randint(100, 400), randint(10, 50))
platf_6 = Platform(randint(1,2), 'plf.png', randint(100, 400), randint(10, 50))

platforms.add(platf_1, platf_2, platf_3, platf_4, platf_5, platf_6)

game = True
while game:
    window.fill((68, 227, 219))

    for e in event.get():
        if e.type == QUIT:
            game = False




    gs.reset()
    gs.update()

    platforms.update()
    platforms.draw(window)



    clock.tick(fps)

    display.update()
