import pygame
import random

WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 20

pygame.display.set_caption("Snake Game")
pygame.font.init()
score_font = pygame.font.SysFont("Consolas", 20)
score = 0

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialiser pygame
pygame.init()

# Configuration de l'affichage
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Mise en place de l'horloge
clock = pygame.time.Clock()

# Initialisation du serpent et de la nourriture
snake_pos = [[WIDTH // 2, HEIGHT // 2]]
snake_speed = [0, BLOCK_SIZE]

teleport_walls = True

def generate_food():
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        food_pos = [x, y]
        if food_pos not in snake_pos:
            return food_pos

def draw_objects():
    win.fill((0, 0, 0))
    for pos in snake_pos:
        pygame.draw.rect(win, WHITE, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(win, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
    # Afficher le score
    score_text = score_font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, (10, 10))

def update_snake():
    global food_pos, score
    new_head = [snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]]

    if teleport_walls:
        # si la nouvelle position de la tête est en dehors de l'écran, la ramener de l'autre côté
        if new_head[0] >= WIDTH:
            new_head[0] = 0
        elif new_head[0] < 0:
            new_head[0] = WIDTH - BLOCK_SIZE
        if new_head[1] >= HEIGHT:
            new_head[1] = 0
        elif new_head[1] < 0:
            new_head[1] = HEIGHT - BLOCK_SIZE
    
    if new_head == food_pos:
        food_pos = generate_food() # Nouvelle nourriture
        score += 1 # Incrémenter le score lorsque la nourriture est mangée
    else:
        snake_pos.pop() # Enlève la dernière partie du serpent
    
    snake_pos.insert(0, new_head) # Ajoute la nouvelle tête à la position du serpent

def game_over():
    # fin de partie lorsque le serpent heurte les limites ou se heurte lui-même
    if teleport_walls:
        return snake_pos[0] in snake_pos[1:]
    else:
        return snake_pos[0] in snake_pos[1:] or \
            snake_pos[0][0] >= WIDTH or \
            snake_pos[0][0] < 0 or \
            snake_pos[0][1] >= HEIGHT or \
            snake_pos[0][1] < 0
   
def game_over_screen():
    global score
    win.fill((0, 0, 0))
    game_over_font = pygame.font.SysFont("consolas", 50)
    game_over_text = game_over_font.render(f"Snake - Game Over ! Score : {score}", True, WHITE)
    win.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    run() # Redémarre le jeu
                    return
                elif event.key == pygame.K_q:
                    pygame.quit() # Quitte le jeu
                    return
            
def run():
    global snake_speed, snake_pos, food_pos, score
    snake_pos = [[WIDTH // 2, HEIGHT // 2]]
    snake_speed = [0, BLOCK_SIZE]
    food_pos = generate_food()
    score = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            # lorsque HAUT est pressé mais que le serpent va vers le bas, ignorer l'entrée
            if snake_speed[1] != BLOCK_SIZE:
                snake_speed = [0, -BLOCK_SIZE]
        elif keys[pygame.K_DOWN]:
            # lorsque BAS est pressé mais que le serpent va vers le haut, ignorer l'entrée
            if snake_speed[1] != -BLOCK_SIZE:
                snake_speed = [0, BLOCK_SIZE]
        elif keys[pygame.K_LEFT]:
            # lorsque GAUCHE est pressé mais que le serpent va vers la droite, ignorer l'entrée
            if snake_speed[0] != BLOCK_SIZE:
                snake_speed = [-BLOCK_SIZE, 0]
        elif keys[pygame.K_RIGHT]:
            # lorsque DROITE est pressé mais que le serpent va vers la gauche, ignorer l'entrée
            if snake_speed[0] != -BLOCK_SIZE:
                snake_speed = [BLOCK_SIZE, 0]

        if game_over():
            game_over_screen()
            return
        
        update_snake()
        draw_objects()
        pygame.display.update()
        clock.tick(15) # Limite la vitesse du serpent à 15 FPS

if __name__ == "__main__":
    run()