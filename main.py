from pygame import*

window = display.set_mode((700,500))
back = (102, 90, 202)  #0-255 0-255 0-255
window.fill(back)

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, x, y, w, h, player_speed):
        self.image = transform.scale(image.load(player_image),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_p] and self.rect.y>5: #[K_UP] [K_DOWN]
            self.rect.y -= self.speed
        if keys[K_l] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

player_left = Player('racket.png', 20, 200, 70, 100, 10)
player_right = Player('racket.png', 600, 200, 70, 100, 10)
ball = Gamesprite('ball.png', 300, 200, 50, 50, 10)
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    if finish != True:
        window.fill(back)
        player_left.reset()
        player_right.reset()
        ball.reset()
        player_left.update_left()
        player_right.update_right()
    display.update()
    time.delay(50)