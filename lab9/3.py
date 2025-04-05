import pygame, random, time

pygame.init()
font = pygame.font.SysFont("comicsansms", 24)
cellsize = 20
cellsheight = 20
cellswidth = 30
maxw = cellswidth * cellsize
maxh = cellsheight * cellsize

screen = pygame.display.set_mode((maxw, maxh))
done = False
centerx = 5
centery = 5
dx = 1
dy = 0
step = 20
color_grid = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
speed = 5

snakeshead = pygame.image.load("snake.jpeg")
snakeshead = pygame.transform.scale(snakeshead, (cellsize, cellsize))

betterfood_img = pygame.image.load("betterfood.jpg")
betterfood_img = pygame.transform.scale(betterfood_img, (cellsize, cellsize))

clock = pygame.time.Clock()

def movement(x, y, dx, dy):
    return x + dx, y + dy

def food_position(new_head, walls):
    while True:
        x = random.randint(0, cellswidth - 1)
        y = random.randint(0, cellsheight - 1)
        if (x, y) != new_head and (x, y) not in walls:
            return (x, y)

def food_draw(screen, food_pos):
    x, y = food_pos
    pygame.draw.rect(screen, YELLOW, pygame.Rect(x * cellsize, y * cellsize, cellsize, cellsize))

def snake_draw(screen, our_body):
    for i in range(len(our_body)):
        x, y = our_body[i]
        if i == 0:
            screen.blit(snakeshead, (x * cellsize, y * cellsize))
        else:
            pygame.draw.rect(screen, GREEN, pygame.Rect(x * cellsize, y * cellsize, cellsize, cellsize))

def upd_thebody(new_head, food_pos, our_body, betterfood_pos):
    new_body = [new_head] + our_body[:-1]
    ate = False
    if new_head == food_pos:
        new_body.append(our_body[-1])
        ate = True
    if new_head == betterfood_pos:
        new_body.append(our_body[-1])
        new_body.append(our_body[-1])
        ate = True
    return new_body, ate

def load_wall(level, t_width):
    wall_positions = []
    with open(f"levels/level{level}.txt", "r") as f:
        row = 0
        for line in f:
            col = 0
            for char in line:
                if char == "#":
                    wall_positions.append((col, row))
                if char != "\n":
                    col += 1
            row += 1
    return wall_positions

def collision(new_head, walls):
    return new_head in walls

def betterfood(new_head, our_body, walls, food_pos):
    while True:
        x = random.randint(0, cellswidth - 1)
        y = random.randint(0, cellsheight - 1)
        if (x, y) != new_head and (x, y) not in our_body and (x, y) not in walls and (x, y) != food_pos:
            return (x, y)

def draw_betterfood(screen, betterfood_pos):
    x, y = betterfood_pos
    screen.blit(betterfood_img, (x * cellsize, y * cellsize))

ate_cnt = 0
score = 0
level = 1
our_body = [(centerx, centery)]
walls = load_wall(level, cellsize)
food_pos = food_position(our_body[0], walls)
betterfood_pos = None
direction = (dx, dy)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                dx, dy = 0, 1
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                dx, dy = -1, 0
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                dx, dy = 1, 0

    direction = (dx, dy)
    centerx, centery = movement(centerx, centery, dx, dy)
    new_head = (centerx, centery)

    if centerx >= cellswidth: centerx = 0
    elif centerx < 0: centerx = cellswidth - 1
    if centery >= cellsheight: centery = 0
    elif centery < 0: centery = cellsheight - 1

    our_body, ate = upd_thebody(new_head, food_pos, our_body, betterfood_pos)

    if collision(new_head, walls):
        done = True
        


    screen.fill(BLACK)
    food_draw(screen, food_pos)
    snake_draw(screen, our_body)
    if betterfood_pos:
        draw_betterfood(screen, betterfood_pos)

    if new_head == food_pos:
        food_pos = food_position(new_head, walls)
        ate_cnt += 1
        score += 1

    if ate_cnt == 6 and betterfood_pos is None:
        betterfood_pos = betterfood(new_head, our_body, walls, food_pos)

    if ate_cnt >= 4 and betterfood_pos is None:
        level += 1
        ate_cnt = 0
        speed += 0.5
        walls = load_wall(level, cellsize)

    if betterfood_pos and new_head == betterfood_pos:
        betterfood_pos = None
        ate_cnt += 2
        score += 2


    

    for x, y in walls:
        pygame.draw.rect(screen, WHITE, pygame.Rect(x * cellsize, y * cellsize, cellsize, cellsize))

    for l_y in range(0, maxh, step):
        pygame.draw.line(screen, WHITE, (0, l_y), (maxw, l_y))
    for l_x in range(0, maxw, step):
        pygame.draw.line(screen, WHITE, (l_x, 0), (l_x, maxh))

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (30, 30))

    pygame.display.flip()
    clock.tick(speed)
