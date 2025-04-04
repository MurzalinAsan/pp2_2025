import pygame, sys, random, time

pygame.init()

fps = 60

speed = 4

clock = pygame.time.Clock()

money = 0

coincount = 0

bonuscount = 0

lastspeedup = 0

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((400, 600))
screen_width = 400
screen_height = 600
screen.fill(WHITE)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

pygame.display.set_caption("Racer")

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image1, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), 0)
    def move(self):
        self.rect.move_ip(0, speed + 2)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load("Coin2.png")
        self.image = pygame.transform.scale(self.image1, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), 0)
    def move(self):
        self.rect.move_ip(0, speed - 0.5)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), 0)
    def move(self):
        self.rect.move_ip(0, speed)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
    

EL = Enemy()
class PLayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("PLayer.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < screen_width:
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
    

PL = PLayer()

COIN = Coin()

BONUS = Coin2()

enemies = pygame.sprite.Group()
enemies.add(EL)
coins = pygame.sprite.Group()
coins.add(COIN)
all_sprites = pygame.sprite.Group()
all_sprites.add(PL)
all_sprites.add(EL)
all_sprites.add(COIN)
bonus = pygame.sprite.Group()
bonus.add(BONUS)




done = False
bonus_available = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    

    screen.blit(background, (0, 0))
    scores = font.render(f"Score: {money}", True, BLACK)
    screen.blit(scores, (10, 10))

    game_over = font.render("GAME OVER", True, BLACK)
    for i in all_sprites:
        screen.blit(i.image, i.rect)
        i.move()
    if pygame.sprite.spritecollideany(PL, enemies):
          screen.fill(RED)
          
          for entity in all_sprites:
                entity.kill() 
          screen.blit(game_over, (50, 100))
          time.sleep(2)
          

          done = True
    if pygame.sprite.spritecollideany(PL, coins):
        coincount += 1
        for coin in coins:
            coin.rect.top = 0
            coin.rect.center = (random.randint(30, 370), 0)
    
    if coincount % 4 == 0 and coincount != 0 and not bonus_available:
            bonus_available = True
    if bonus_available:
            BONUS.move()
            BONUS.draw(screen)

    if bonus_available and pygame.sprite.spritecollideany(PL, bonus):
            bonuscount += 2
            bonus_available = False
    if coincount != 0 and coincount % 10 == 0 and coincount != lastspeedup:
            speed += 1
            lastspeedup = coincount


            for i in bonus:
                i.rect.top = 0
                i.rect.center = (random.randint(30, 370), 0)

    money = coincount + bonuscount

    pygame.display.flip()
    clock.tick(fps)    