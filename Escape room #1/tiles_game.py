""" import pygame
import random
import sys

def play_game1():
    print("Tiles Puzzle")

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1017
TILE_WIDTH = SCREEN_WIDTH // 4
TILE_HEIGHT = 200
FPS = 50


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TILE_COLOR = (255, 255, 255)

background_image = pygame.image.load('tiles_game.jpg')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escape Room")
clock = pygame.time.Clock()

class Tile:
    def __init__(self, column):
        self.rect = pygame.Rect(column * TILE_WIDTH, 0, TILE_WIDTH, TILE_HEIGHT)

    def move(self):
        self.rect.y += 5

    def draw(self, surface):
        pygame.draw.rect(surface, TILE_COLOR, self.rect)


tiles = []
score = 0
game_over = False
won_game = False

def reset_game():
    global tiles, score, game_over
    tiles = []
    score = 0
    game_over = False
    won_game = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = event.pos
            column = mouse_x // TILE_WIDTH
            
            for tile in tiles:
                if tile.rect.collidepoint(event.pos):
                    tiles.remove(tile)
                    score += 1
                    if score >= 20:
                        game_over = True
                        won_game = True
                    break

    if not game_over:
        if random.randint(1, 20) == 1:
            tiles.append(Tile(random.randint(0, 3)))

        for tile in tiles:
            tile.move()
            if tile.rect.top > SCREEN_HEIGHT:
                game_over = True

        screen.blit(background_image, (0, 0))
        for tile in tiles:
            tile.draw(screen)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (120, 10))

        pygame.display.flip()
        clock.tick(FPS)

    else:
        screen.fill(WHITE)
        font = pygame.font.Font(None, 74)
        if won_game:
            end_text = font.render('You Won!', True, BLACK)
            out_text = font.render('Click to go to the next room.', True, BLACK)
            screen.blit(out_text, (SCREEN_WIDTH // 2 - out_text.get_width() // 2, SCREEN_HEIGHT // 2 + 70))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    import first_room4
                    pygame.quit()
                    sys.exit()
                    break
        else:
            end_text = font.render('Game Over! Try again.', True, BLACK)
        score_text = font.render(f'Score: {score}', True, BLACK)
        restart_text = font.render('Click to Restart', True, BLACK)

        if not won_game:
            screen.blit(end_text, (SCREEN_WIDTH // 2 - end_text.get_width() // 2, SCREEN_HEIGHT // 2 - end_text.get_height()))
            screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2  + end_text.get_height()))
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + end_text.get_height() + score_text.get_height() + 10))

        pygame.display.flip()

        if not won_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    reset_game()
                    sys.exit()


if __name__ == "__main__":
    play_game1() """

import pygame
import random
import sys

def play_game1():
    print("Tiles Puzzle")

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1017
TILE_WIDTH = SCREEN_WIDTH // 4
TILE_HEIGHT = 200
FPS = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TILE_COLOR = (255, 255, 255)

background_image = pygame.image.load('tiles_game.jpg')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escape Room")
clock = pygame.time.Clock()

class Tile:
    def __init__(self, column):
        self.rect = pygame.Rect(column * TILE_WIDTH, 0, TILE_WIDTH, TILE_HEIGHT)

    def move(self):
        self.rect.y += 5

    def draw(self, surface):
        pygame.draw.rect(surface, TILE_COLOR, self.rect)

tiles = []
score = 0
game_over = False
won_game = False

def reset_game():
    global tiles, score, game_over, won_game
    tiles = []
    score = 0
    game_over = False
    won_game = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = event.pos
            column = mouse_x // TILE_WIDTH
            
            for tile in tiles:
                if tile.rect.collidepoint(event.pos):
                    tiles.remove(tile)
                    score += 1
                    if score >= 20:
                        game_over = True
                        won_game = True
                    break

    if not game_over:
        if random.randint(1, 20) == 1:
            tiles.append(Tile(random.randint(0, 3)))

        for tile in tiles:
            tile.move()
            if tile.rect.top > SCREEN_HEIGHT:
                game_over = True

        screen.blit(background_image, (0, 0))
        for tile in tiles:
            tile.draw(screen)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (120, 10))

        pygame.display.flip()
        clock.tick(FPS)

    else:
        screen.fill(WHITE)
        font = pygame.font.Font(None, 74)
        if won_game:
            end_text = font.render('You Won!', True, BLACK)
            out_text = font.render('Click to go to the next room.', True, BLACK)
            # Displaying the victory message, but not importing immediately
            screen.blit(out_text, (SCREEN_WIDTH // 2 - out_text.get_width() // 2, SCREEN_HEIGHT // 2 + 70))
            
            # Wait for user input to import first_room4.py
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Import first_room4.py when user clicks
                    import first_room4
                    pygame.quit()  # Quit the current game after importing
                    sys.exit()  # Make sure to exit after importing
                    break

        else:
            end_text = font.render('Game Over! Try again.', True, BLACK)

        score_text = font.render(f'Score: {score}', True, BLACK)
        restart_text = font.render('Click to Restart', True, BLACK)

        if not won_game:
            screen.blit(end_text, (SCREEN_WIDTH // 2 - end_text.get_width() // 2, SCREEN_HEIGHT // 2 - end_text.get_height()))
            screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 + end_text.get_height()))
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + end_text.get_height() + score_text.get_height() + 10))
        
        pygame.display.flip()

        # Check for restart on mouse click for game over
        if not won_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    reset_game()  # Restart the game
                    break

if __name__ == "__main__":
    play_game1()