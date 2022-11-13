from pygame import *

font.init()


 
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   def init(self, player_image, player_x, player_y, player_speed, player_width, player_height):
       super().init()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y <= 470:
            self.rect.y += 10
        if keys[K_DOWN] and self.rect.y >= 30:
            self.rect.y -= 10

class Enemy(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y <= 470:
            self.rect.y += 10
        if keys[K_s] and self.rect.y >= 30:
            self.rect.y -= 10

class Ball(GameSprite):
    def update(self):
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
img_back = "background.png"
display.set_caption("Pong game")
window = display.set_mode((500, 700))
background = transform.scale(image.load(img_back), (500, 700))

rocket1 = Player("rocket.png", 10, 250, 10, 10, 60)
rocket2  = Enemy("rocket.png", 690, 250, 10, 10, 60)
ball = Ball("ball.png", 350, 250, 25, 15, 15)
run = True
FPS = 60

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

            
    if not finish:
        window.blit(background,(0, 0))
        
        rocket1.update()
        rocket1.update()
        ball.update()

        rocket1.reset()
        rocket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
    


                