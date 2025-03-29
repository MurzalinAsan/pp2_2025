import pygame, datetime

pygame.init()




maxw = 400
maxh = 400
clockimg = pygame.image.load("clock.png")
w, h = clockimg.get_size()
screen = pygame.display.set_mode((w, h))
done = False


minhand = pygame.image.load("min_hand.png")
sechand = pygame.image.load("sec_hand.png")

center = (w // 2, h // 2)


def func(screen, img, center, a):
        rotated = pygame.transform.rotate(img, -a)
        n = rotated.get_rect(center=center)
        screen.blit(rotated, n)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        t = datetime.datetime.now()

        s = t.second
        m = t.minute
        screen.blit(clockimg, (0, 0))
        seconds_a = s * 6
        min_a = m * 6 + (s / 60) * 6

        func(screen, sechand, center, seconds_a)
        func(screen, minhand, center, min_a)
        
        pygame.display.flip()
        pygame.time.delay(1000)
        
