import pygame
import math

pygame.init()

widht = 800
h = 600
screen = pygame.display.set_mode((widht, h))
clock = pygame.time.Clock()

canva = pygame.Surface((widht, h))
canva.fill((0, 0, 0))

icon_sz = (40, 40)

brush = pygame.Surface(icon_sz)
brush.fill((200, 200, 200))
pygame.draw.line(brush, (255, 255, 255), (5, 20), (35, 20), 5)

rect_ic = pygame.Surface(icon_sz)
rect_ic.fill((200, 200, 200))
pygame.draw.rect(rect_ic, (255, 255, 255), (5, 5, 30, 30), 2)

circle = pygame.Surface(icon_sz)
circle.fill((200, 200, 200))
pygame.draw.circle(circle, (255, 255, 255), (20, 20), 15, 2)

eraser = pygame.Surface(icon_sz)
eraser.fill((200, 200, 200))
pygame.draw.rect(eraser, (255, 255, 255), (5, 5, 30, 30))

icons = {
    "brush": pygame.Rect(10, 10, 40, 40),
    "rect": pygame.Rect(60, 10, 40, 40),
    "circle": pygame.Rect(110, 10, 40, 40),
    "eraser": pygame.Rect(160, 10, 40, 40)
}

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colors = {
    "r": pygame.Rect(10, 60, 30, 30),
    "g": pygame.Rect(50, 60, 30, 30),
    "b": pygame.Rect(90, 60, 30, 30),
    "bl": pygame.Rect(130, 60, 30, 30)
}

color = WHITE
erasing = "brush"
draw = False
start = (0, 0)
last = (0, 0)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                p = event.pos
                for c, r in colors.items():
                    if r.collidepoint(p):
                        if c == "r": color = RED
                        elif c == "g": color = GREEN
                        elif c == "b": color = BLUE
                        elif c == "bl": color = BLACK
                for t, r in icons.items():
                    if r.collidepoint(p):
                        erasing = t
                if not any(r.collidepoint(p) for r in icons.values()) and not any(r.collidepoint(p) for r in colors.values()):
                    draw = True
                    start = p
                    last = p

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and draw:
                end = event.pos
                if erasing == "rect":
                    x = min(start[0], end[0])
                    y = min(start[1], end[1])
                    rw = abs(end[0] - start[0])
                    rh = abs(end[1] - start[1])
                    pygame.draw.rect(canva, color, (x, y, rw, rh), 2)
                elif erasing == "circle":
                    dx = end[0] - start[0]
                    dy = end[1] - start[1]
                    r = int(math.sqrt(dx*dx + dy*dy))
                    pygame.draw.circle(canva, color, start, r, 2)
                draw = False

        if event.type == pygame.MOUSEMOTION:
            if draw:
                if erasing == "brush":
                    pygame.draw.line(canva, color, last, event.pos, 5)
                    last = event.pos
                elif erasing == "eraser":
                    pygame.draw.line(canva, BLACK, last, event.pos, 20)
                    last = event.pos

    screen.blit(canva, (0, 0))
    screen.blit(brush, icons["brush"].topleft)
    screen.blit(rect_ic, icons["rect"].topleft)
    screen.blit(circle, icons["circle"].topleft)
    screen.blit(eraser, icons["eraser"].topleft)

    pygame.draw.rect(screen, RED, colors["r"])
    pygame.draw.rect(screen, GREEN, colors["g"])
    pygame.draw.rect(screen, BLUE, colors["b"])
    pygame.draw.rect(screen, BLACK, colors["bl"])

    pygame.display.flip()
    clock.tick(60)
