import pygame, sys, random
from pygame import KEYDOWN
from pygame.math import Vector2

# INITIALIZATIONS
pygame.init()
cell_size = 24
columns = 30
rows = 20
w,h = cell_size*columns, cell_size*rows
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
pygame.display.set_caption("Joc_00")

# FRUIT LIST
fruits = []
for i in range(1,14):
    if i < 10:
        i = '0'+str(i)
    else:
        i = str(i)
    p = pygame.image.load(f"gallery/{i}.png").convert_alpha()
    fruits.append(p)

# SNAKE BODY
snake_head = [pygame.image.load("gallery/snake000.png").convert_alpha(),
                  pygame.image.load("gallery/snake001.png").convert_alpha(),
                  pygame.image.load("gallery/snake002.png").convert_alpha(),
                  pygame.image.load("gallery/snake003.png").convert_alpha()]

snake_tail = [pygame.image.load("gallery/snake004.png").convert_alpha(),
              pygame.image.load("gallery/snake005.png").convert_alpha(),
              pygame.image.load("gallery/snake006.png").convert_alpha(),
              pygame.image.load("gallery/snake007.png").convert_alpha()]

snake_body = [pygame.image.load("gallery/snake008.png").convert_alpha(),
                  pygame.image.load("gallery/snake009.png").convert_alpha(),
                  pygame.image.load("gallery/snake010.png").convert_alpha(),
                  pygame.image.load("gallery/snake011.png").convert_alpha(),
                  pygame.image.load("gallery/snake012.png").convert_alpha(),
                  pygame.image.load("gallery/snake013.png").convert_alpha()]

# GRASS
grass = pygame.image.load("gallery/tile1234.png").convert_alpha()

# FONT
game_font = pygame.font.Font(None,24)

class SNAKE:
    def __init__(self):
        self.reset()

    def draw_snake(self):
        for p in range(len(self.body)):
            snake_rect = pygame.Rect(self.body[p].x * cell_size, self.body[p].y * cell_size, cell_size, cell_size)
            if p == 0 :
                if self.direction.x == 0 and self.direction.y == -1:
                    part = snake_head[0]
                elif self.direction.x == 1 and self.direction.y == 0:
                    part = snake_head[1]
                elif self.direction.x == 0 and self.direction.y == 1:
                    part = snake_head[2]
                elif self.direction.x == -1 and self.direction.y == 0:
                    part = snake_head[3]
            elif p == len(self.body)-1:
                if self.body[p-1].x == self.body[p].x:
                    if self.body[p-1].y < self.body[p].y:
                        part = snake_tail[0] # UP
                    else:
                        part = snake_tail[2] # DOWN
                elif self.body[p-1].y == self.body[p].y:
                    if self.body[p-1].x > self.body[p].x:
                        part = snake_tail[1] # RIGHT
                    else:
                        part = snake_tail[3] # LEFT
            else:
                if self.body[p - 1].x == self.body[p].x and self.body[p + 1].x == self.body[p].x:
                    part = snake_body[4]  # UP or DOWN
                elif self.body[p - 1].y == self.body[p].y and self.body[p + 1].y == self.body[p].y:
                    part = snake_body[5]  # RIGHT or LEFT
                elif (self.body[p-1].y < self.body[p].y and self.body[p+1].x > self.body[p].x)\
                        or (self.body[p+1].y < self.body[p].y and self.body[p-1].x > self.body[p].x):
                    part = snake_body[0]
                elif (self.body[p-1].x > self.body[p].x and self.body[p+1].y > self.body[p].y)\
                        or (self.body[p+1].x > self.body[p].x and self.body[p-1].y > self.body[p].y):
                    part = snake_body[1]
                elif (self.body[p-1].x < self.body[p].x and self.body[p+1].y > self.body[p].y)\
                        or (self.body[p+1].x < self.body[p].x and self.body[p-1].y > self.body[p].y):
                    part = snake_body[2]
                elif (self.body[p-1].y < self.body[p].y and self.body[p+1].x < self.body[p].x)\
                        or (self.body[p+1].y < self.body[p].y and self.body[p-1].x < self.body[p].x):
                    part = snake_body[3]

            screen.blit(part, snake_rect)


    def move_snake(self):
        if self.add:
            body_copy = self.body[:]
        else:
            body_copy = self.body[:-1]

        x_new, y_new = body_copy[0].x + self.direction.x, body_copy[0].y + self.direction.y
        if x_new > columns-1:
            x_new = 0
        elif x_new < 0:
            x_new = columns

        if y_new > rows-1:
            y_new = 0
        elif y_new < 0:
            y_new = rows
        body_copy.insert(0,Vector2(x_new,y_new))
        self.body = body_copy[:]

    def eat(self):
        self.add = True
        self.move_snake()
        self.add = False

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def play_die_sound(self):
        self.die_sound.play()

    def reset(self):
        x_init = columns // 2
        y_init = rows // 2
        self.body = [Vector2(x_init, y_init), Vector2(x_init + 1, y_init), Vector2(x_init + 2, y_init)]
        self.direction = Vector2(-1, 0)
        self.add = False
        self.crunch_sound = pygame.mixer.Sound("sounds/apple_bite.ogg")
        self.die_sound = pygame.mixer.Sound("sounds/DieSound_CC0_by_EugeneLoza.ogg")

class FRUIT:
    def __init__(self):
        self.coordinates()

    def coordinates(self):
        self.x = random.randint(0, columns - 1)
        self.y = random.randint(0, rows - 1)
        self.poz = Vector2(self.x, self.y)
        self.nr = random.randint(0, len(fruits) - 1)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.poz.x * cell_size ,self.poz.y * cell_size, cell_size, cell_size)
        screen.blit(fruits[self.nr],fruit_rect)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.collision()
        self.hit()

    def draw_elements(self):
        self.draw_grass()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.draw_score()

    def collision(self):
        if self.fruit.poz == self.snake.body[0]:
            self.fruit.coordinates()
            self.snake.eat()
            self.snake.play_crunch_sound()

        for part in self.snake.body[1:]:
            if part == self.fruit.poz:
                self.fruit.coordinates()

    def hit(self):
        for part in self.snake.body[1:]:
            if part == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.play_die_sound()
        self.snake.reset()

    def draw_grass(self):
        for i in range(0,columns,2):
            for j in range(0,rows,2):
                grass_rect = pygame.Rect(i * cell_size, j * cell_size, cell_size*2, cell_size*2)
                screen.blit(grass,grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,False,"black")
        score_rect = score_surface.get_rect(center = (cell_size*2,cell_size))
        apple_rect = fruits[4].get_rect(midright = (score_rect.left,score_rect.centery))

        screen.blit(score_surface,score_rect)
        screen.blit(fruits[4],apple_rect)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

ok = 0
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == SCREEN_UPDATE:
            if not ok:
                main_game.update()
            ok = 0
        if event.type ==  KEYDOWN:
            if (event.key == pygame.K_w or event.key == pygame.K_UP) and main_game.snake.direction.y != 1 :
                main_game.snake.direction = Vector2(0,-1)
            elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0,1)
            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1,0)
            elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1,0)
            main_game.update()
            ok = 1

    screen.fill((175,235,90))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()

