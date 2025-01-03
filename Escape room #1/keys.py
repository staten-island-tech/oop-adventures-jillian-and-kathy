import pygame
import sys
import random
from first_room import first_room

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Inventory:
    def __init__(self):
        self.keys = 0

    def add_key(self):
        self.keys += 1

def draw_inventory(screen, inventory):
    font = pygame.font.Font(None, 36)
    inventory_text = f"Keys: {inventory.keys}"
    text_surface = font.render(inventory_text, True, BLACK)
    screen.blit(text_surface, (10, 10))

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Escape Room")
    clock = pygame.time.Clock()

    inventory = Inventory()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)

        draw_inventory(screen, inventory)

        # Change to the room2 screen when a key is present (for demonstration)
        if inventory.keys > 0:
            room2 = Room2(inventory)  # Pass inventory to room2
            room2.run(screen)
            break  # Exit main loop when transitioning to another room

        # Fake key collection for testing
        if random.randint(0, 100) < 2:  # Random chance to collect a key
            inventory.add_key()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()