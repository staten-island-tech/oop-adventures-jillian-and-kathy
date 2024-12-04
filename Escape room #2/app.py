import time
import pygame
import sys

pygame.init()

screen_width = 1920
screen_height = 1017

background_image = pygame.image.load('image.jpg')  # Add your own background image
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Room #2")

font = pygame.font.SysFont("Courier New", 50, bold = True)

def slow_print(text, delay=0.01):
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
    quotes = [
        "Congrats! You've completed the first room, ",
        
    ]

    for quote in quotes:
        slow_print(quote, 0.01)  
        time.sleep(1)  
        screen.blit(background_image, (0, 0)) 
        pygame.display.flip()  

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


