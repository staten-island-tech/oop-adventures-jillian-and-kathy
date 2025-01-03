""" import time
import pygame
import sys

pygame.init()

screen_width = 1920
screen_height = 1017

background_image = pygame.image.load('start_room_official.jpg')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Room")

font = pygame.font.SysFont("Courier New", 30, bold = True, italic = True)
clickable_area1 = pygame.Rect(760, 760, 300, 190)

def slow_print(text, delay=0.05):
    current_text = ""
    for char in text:
        current_text += char
        screen.blit(background_image, (0, 0))
        rendered_text = font.render(current_text, True, (255, 255, 255))
        screen.blit(rendered_text, (50, 50))
        pygame.display.flip()
        time.sleep(delay)

def main():
    quotes = [
        "Welcome to the first room!",
        "To escape the room, find all 3 keys by completing puzzles.",
        "I wonder what would happen if you clicked on the rug?"
        
    ]

    for quote in quotes:
        slow_print(quote, 0.05)
        time.sleep(1)
        screen.blit(background_image, (0, 0))
        pygame.display.flip()

import pygame
import sys

class First_room:
    def __init__(self, inventory):
        self.inventory = inventory

    def run(self, screen):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw_inventory(screen)

            pygame.display.flip()
            clock.tick(30)

    def draw_inventory(self, screen):
        font = pygame.font.Font(None, 36)
        inventory_text = f"Keys: {self.inventory.keys}"
        text_surface = font.render(inventory_text, True, (0, 0, 0))
        screen.blit(text_surface, (10, 10))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if clickable_area1.collidepoint(mouse_x, mouse_y):
                        slow_print("You've found something under the rug!", 0.03)
                        time.sleep(2)
                        screen.blit(background_image, (0, 0))
                        pygame.draw.rect(screen, (255, 0, 0), clickable_area1, 3)
                        pygame.display.flip()
                        import first_puzzle
                        first_puzzle.main()
        pygame.draw.rect(screen, (255, 0, 0), clickable_area1, 2)
        
        pygame.display.flip()


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() """

import time
import pygame
import sys

pygame.init()

# Constants
screen_width = 1920
screen_height = 1017
background_image = pygame.image.load('start_room_official.jpg')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Room")

font = pygame.font.SysFont("Courier New", 30, bold=True, italic=True)
clickable_area1 = pygame.Rect(760, 760, 300, 190)

# Slow print function
def slow_print(text, delay=0.05):
    current_text = ""
    for char in text:
        current_text += char
        screen.blit(background_image, (0, 0))
        rendered_text = font.render(current_text, True, (255, 255, 255))
        screen.blit(rendered_text, (50, 50))
        pygame.display.flip()
        time.sleep(delay)

# Inventory Class
class Inventory:
    def __init__(self):
        self.keys = 0  # Assuming keys are counted as integers

# First Room Class
class FirstRoom:
    def __init__(self, inventory):
        self.inventory = inventory

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if clickable_area1.collidepoint(mouse_x, mouse_y):
                            slow_print("You've found something under the rug!", 0.03)
                            time.sleep(2)
                            # Update the screen after the slow print operation
                            screen.blit(background_image, (0, 0))
                            pygame.draw.rect(screen, (255, 0, 0), clickable_area1, 3)
                            pygame.display.flip()
                            # For the example, you could call another function here
                            # For example, if you want to go to a puzzle: 
                            import first_puzzle
                            first_puzzle.main()  # Make sure `first_puzzle.py` exists and implements a `main` function

            # Draw the clickable area
            pygame.draw.rect(screen, (255, 0, 0), clickable_area1, 2)
            self.draw_inventory(screen)
            pygame.display.flip()
            clock.tick(30)

    def draw_inventory(self, screen):
        font = pygame.font.Font(None, 36)
        inventory_text = f"Keys: {self.inventory.keys}"
        text_surface = font.render(inventory_text, True, (0, 0, 0))
        screen.blit(text_surface, (10, 10))

def main():
    # Create inventory
    inventory = Inventory()

    # Display introductory quotes
    quotes = [
        "Welcome to the first room!",
        "To escape the room, find all 3 keys by completing puzzles.",
        "I wonder what would happen if you clicked on the rug?"
    ]

    for quote in quotes:
        slow_print(quote, 0.05)
        time.sleep(1)
        screen.blit(background_image, (0, 0))
        pygame.display.flip()

    # Initiate the first room
    first_room = FirstRoom(inventory)
    first_room.run()

if __name__ == "__main__":
    main()
