import time
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
        "You have recieved a key!",
        "Now you can unlock the door to the next room."
        
    ]

    for quote in quotes:
        slow_print(quote, 0.05)
        time.sleep(1)
        screen.blit(background_image, (0, 0))
        pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()