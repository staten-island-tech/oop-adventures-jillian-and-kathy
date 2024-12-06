import time
import pygame
import sys

screen_width = 1920
screen_height = 1017

class book():
    background_book = pygame.image.load('openbook.jpg')  # Add your own background image
    pygame.transform.scale(background_book, (screen_width, screen_height))

def main():
    quotes = [
        "Welcome to the third and final escape room.",
        "Press on objects to play the puzzles and escape.",
        "In order to make it out, find all 3 keys by completing puzzles.",
        "Who was here last? I think they left something."
    ]


    for quote in quotes:
        pygame.display.flip()  # Update the display


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()  # Make sure the screen updates after each event

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
    