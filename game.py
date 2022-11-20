from pygame import *


clock = time.Clock()
# player1_score = 0
# player2_score = 0



# font.init()
# font1 = font.Font("Arial", 20)
# score = font1.render("rocket1:"player1_score, "\nrocket2:"player2_score, True, (255, 255, 255))
# font_win = font.Font("Arial", 60)
# win = font_win.render("Player 1 won",  True, (255, 255, 255))
# font_lose = font.Font("Arial", 60)
# lose = font_lose.render("Player 2 lose", True, (255, 255, 255))
speed_x = 3
speed_y = 3



class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height)) #вместе 55,55 - параметры
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
        self.rect.x += speed_x
        self.rect.y += speed_y
        
img_back = "background.png"
display.set_caption("Pong game")
window = display.set_mode((500, 500))
background = transform.scale(image.load(img_back), (500, 500))

rocket1 = Player("rocket.png", 10, 250, 10, 20, 80)
rocket2  = Enemy("rocket.png", 481, 251, 10, 20, 80)
ball = Ball("asteroid.png", 350, 250, 25, 55, 55)

run = False
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

            
    if not run:
        window.blit(background,(0, 0))
        # window.blit(score, (250, 20))
        rocket1.reset()
        rocket2.reset()
        ball.reset()
       

        rocket1.update()
        rocket1.update()
        ball.update()
        if ball.rect.x >= 470 or ball.rect.x <= 0:
            run = True
            # window.blit(font_win)
            
        if ball.rect.y >= 470 or ball.rect.y <= 0:
            speed_y *= -1
            
        
        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1
    display.update()
    clock.tick(FPS)
    


                