import time
import pygame
import sys

pygame.init()

WIDTH = 1000
HEIGHT = 600
background = pygame.image.load('image.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape room #2")

font = pygame.font.Font(None, 36)

def slow_print(text, delay=0.05):
    """Prints text to the screen slowly, character by character."""
    current_text = ""
    for char in text:
        current_text += char
        screen.blit(background_image, (0, 0))
        rendered_text = font.render(current_text, True, (255, 255, 255))
        screen.blit(rendered_text, (50, 50))
        pygame.display.flip()
        time.sleep(delay)

def main():
    game = game()
    text_display = TextDisplay(game)
    quotes = [
        "Congrats! You've completed the first escape room"
    ]

    for quotes in quots:
        slow_print(quote, 0.05)
        time.sleep(1)
        screen.blit(background_image, (0, 0))
        pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                running = False
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()