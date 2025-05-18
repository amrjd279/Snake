import pygame
import sys
import random

class Block:
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos

class Food:
    def __init__(self):
        x = random.randint(0, NB_COL - 1)
        y = random.randint(0, NB_ROW - 1)
        self.block = Block(x, y)

    def draw_food(self, screen):
        rect = pygame.Rect(self.block.x * CELL_SIZE, self.block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (72, 212, 98), rect)

class Snake:
    def __init__(self):
        self.body = [Block(2, 6), Block(3, 6), Block(4, 6)]
        self.direction = "RIGHT"

    def draw_snake(self, screen):
        for block in self.body:
            x_coord = block.x * CELL_SIZE
            y_coord = block.y * CELL_SIZE
            block_rect = pygame.Rect(x_coord, y_coord, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (83, 177, 253), block_rect)

    def move_snake(self):
        snake_block_count = len(self.body)
        old_head = self.body[snake_block_count - 1]

        if self.direction == "RIGHT":
            new_head = Block(old_head.x + 1, old_head.y)
        elif self.direction == "LEFT":
            new_head = Block(old_head.x - 1, old_head.y)
        elif self.direction == "TOP":
            new_head = Block(old_head.x, old_head.y - 1)
        else:
            new_head = Block(old_head.x, old_head.y + 1)

        self.body.append(new_head)
        self.body.pop(0)

    def check_collision(self):
        head = self.body[-1]
        # Wall collision
        if (head.x >= NB_COL or head.x < 0 or head.y >= NB_ROW or head.y < 0):
            return True
        # Self collision
        for block in self.body[:-1]:
            if block.x == head.x and block.y == head.y:
                return True
        return False

    def check_food_collision(self, food):
        head = self.body[-1]
        if head.x == food.block.x and head.y == food.block.y:
            self.body.insert(0, Block(-1, -1))  # Add dummy block that will be removed
            return True
        return False

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def update(self):
        self.snake.move_snake()
        if self.snake.check_collision():
            self.game_over()
        if self.snake.check_food_collision(self.food):
            self.score += 1
            self.food = Food()

    def draw(self, screen):
        self.snake.draw_snake(screen)
        self.food.draw_food(screen)
        # Draw score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {self.score}', True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

    def game_over(self):
        global game_on
        game_on = False

pygame.init()

NB_COL = 10
NB_ROW = 15
CELL_SIZE = 40

pygame.display.set_caption("Snake Game - Sidiki")
screen = pygame.display.set_mode(size=(NB_COL * CELL_SIZE, NB_ROW * CELL_SIZE))
timer = pygame.time.Clock()

game_on = True
game = Game()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 400)

def show_grid():
    for i in range(0, NB_COL):
        for j in range(0, NB_ROW):
            rect = pygame.Rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (0, 0, 0), rect, width=1)

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game.snake.direction != "DOWN":
                    game.snake.direction = "TOP"
            elif event.key == pygame.K_DOWN:
                if game.snake.direction != "TOP":
                    game.snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT:
                if game.snake.direction != "RIGHT":
                    game.snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                if game.snake.direction != "LEFT":
                    game.snake.direction = "RIGHT"

    screen.fill((255, 255, 255))
    show_grid()
    game.draw(screen)
    pygame.display.update()
    timer.tick(60)

pygame.quit()