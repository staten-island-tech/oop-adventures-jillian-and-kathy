import time
import pygame
import sys

pygame.init()

screen_width = 1920
screen_height = 1017

background_image = pygame.image.load('start_room_official.jpg')  # Add your own background image
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Room")

font = pygame.font.SysFont("Courier New", 30, bold = True, italic = True)

puzzle_button_rect = pygame.Rect(600, 400, 200, 100)
button_clicked = False

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

def reveal_message():
    secret_message = "You've found something!"
    slow_print(secret_message)

def main():
    quotes = [
        "Welcome to the first room!",
        "Good luck!"
        
    ]

    for quote in quotes:
        slow_print(quote, 0.05)  # Print each quote slowly
        time.sleep(1)  # Wait for 3 seconds before clearing the screen
        screen.blit(background_image, (0, 0))  # Clear the text by redrawing the background
        pygame.display.flip()  # Update the display

    running = True
    while running:
        screen.blit(background_image, (0, 0))
        if not button_clicked:
            pygame.draw.rect(screen, (0, 255, 0), puzzle_button_rect)
            button_text = font.render("Click Me!", True, (255, 255, 255))
            screen.blit(button_text, (puzzle_button_rect.x + 50, puzzle_button_rect.y + 35))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if puzzle_button_rect.collidepoint(event.pos):
                        button_clicked = True
                        reveal_message()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()