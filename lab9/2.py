import pygame, random

pygame.init()

font = pygame.font.SysFont("comicsansms", 24)
cellsize = 20
cellsheight = 20
cellswidth = 30
maxw = cellswidth * cellsize
maxh = cellsheight * cellsize

screen = pygame.display.set_mode((maxw, maxh))

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)

dx, dy = 1, 0
speed = 5
direction = (dx, dy)
step = 20

centerx, centery = 5, 5
our_body = [(centerx, centery)]
level = 1
score = 0
ate_cnt = 0
done = False

radius = cellsize // 2

food_timer = 0
betterfood_timer = 0
food_lifetime = 7000
betterfood_lifetime = 5000

def movement(x, y, dx, dy):
    return x + dx, y + dy

def food_position(exclude, walls):
    while True:
        x = random.randint(0, cellswidth - 1)
        y = random.randint(0, cellsheight - 1)
        if (x, y) not in exclude and (x, y) not in walls:
            return (x, y)

def draw_food(screen, pos, is_better=False):
    x, y = pos
    if is_better:
        pygame.draw.circle(screen, ORANGE, (x * cellsize + radius, y * cellsize + radius), radius)
    else:
        pygame.draw.rect(screen, YELLOW, pygame.Rect(x * cellsize, y * cellsize, cellsize, cellsize))

def draw_snake(screen, body):
    for x, y in body:
        pygame.draw.rect(screen, RED, pygame.Rect(x * cellsize, y * cellsize, cellsize, cellsize))

def upd_thebody(new_head, body, food_pos, betterfood_pos):
    new_body = [new_head] + body[:-1]
    if new_head == food_pos:
        new_body.append(body[-1])
        return new_body, 'normal'
    elif new_head == betterfood_pos:
        new_body.extend([body[-1], body[-1]])
        return new_body, 'better'
    return new_body, None

def load_wall(level):
    wall_positions = []
    with open(f"levels/level{level}.txt", "r") as f:
        row = 0
        for raw_line in f:
            line = raw_line.rstrip("\n")
            col = 0
            for char in line:
                if char == "#":
                    wall_positions.append((col, row))
                col += 1
            row += 1
    return wall_positions

walls = load_wall(level)
food_pos = food_position(our_body, walls)
betterfood_pos = None
food_timer = pygame.time.get_ticks()
betterfood_timer = 0

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
    centerx %= cellswidth
    centery %= cellsheight
    new_head = (centerx, centery)

    if new_head in walls:
        done = True

    current_time = pygame.time.get_ticks()

    our_body, ate = upd_thebody(new_head, our_body, food_pos, betterfood_pos)
    if ate == 'normal':
        score += 1
        ate_cnt += 1
        food_pos = food_position(our_body, walls)
        food_timer = current_time
    elif ate == 'better':
        score += 3
        betterfood_pos = None

    if ate_cnt == 6 and betterfood_pos is None:
        betterfood_pos = food_position(our_body, walls)
        betterfood_timer = current_time
    elif ate_cnt >= 4 and betterfood_pos is None:
        level += 1
        ate_cnt = 0
        speed += 0.5
        walls = load_wall(level)

    if current_time - food_timer > food_lifetime:
        food_pos = food_position(our_body, walls)
        food_timer = current_time
    if betterfood_pos and current_time - betterfood_timer > betterfood_lifetime:
        betterfood_pos = None

    screen.fill(BLACK)
    draw_food(screen, food_pos)
    if betterfood_pos:
        draw_food(screen, betterfood_pos, is_better=True)
    draw_snake(screen, our_body)

    for x, y in walls:
        pygame.draw.rect(screen, WHITE, pygame.Rect(x * cellsize, y * cellsize, cellsize, cellsize))

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    for l_y in range(0, maxh, cellsize):
        pygame.draw.line(screen, WHITE, (0, l_y), (maxw, l_y))
    for l_x in range(0, maxw, cellsize):
        pygame.draw.line(screen, WHITE, (l_x, 0), (l_x, maxh))

    pygame.display.flip()
    clock.tick(speed)
