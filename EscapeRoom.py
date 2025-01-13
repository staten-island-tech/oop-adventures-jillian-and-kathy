import time
import pygame
import sys
import importlib

pygame.init()

screen_width = 1920
screen_height = 1017

background_image = pygame.image.load('escape-room.jpg')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Room")

font = pygame.font.SysFont("Courier New", 25, bold = True, italic = True)

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
        "Welcome to the Neon Nexus, a sprawling megacity where neon lights flicker against the backdrop of rain-soaked streets.",
        "You and your team are a group of underground hackers who have stumbled upon a corporation's dark secrets.",
        "The megacorp has caught wind of your investigation and has locked you inside their secure facility.",
        "Your mission is to escape from three high-security rooms before the corporate enforcers arrive to silence you permanently.",
        "Time to get started! (X out of the room)",
    ]

    for quote in quotes:
        slow_print(quote, 0.05)  # Print each quote slowly
        time.sleep(1)  # Wait for 3 seconds before clearing the screen
        screen.blit(background_image, (0, 0))  # Clear the text by redrawing the background
        pygame.display.flip()  # Update the display

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    import first_room
    first_room.main()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

