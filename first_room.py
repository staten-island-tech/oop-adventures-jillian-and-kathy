import time
import pygame
import sys

pygame.init()

screen_width = 1080
screen_height = 600

background_image = pygame.image.load('start_room_official.jpg')  # Add your own background image
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Room")

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
    quotes = [
        "Welcome to the first room!",
        
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