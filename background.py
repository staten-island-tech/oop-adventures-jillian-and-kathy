import time
import pygame
import sys


pygame.init()


screen_width = 1920
screen_height = 1017


background_image = pygame.image.load('Room_3.png')  # Add your own background image
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Room")


font = pygame.font.SysFont("Courier New", 34, bold = True, italic = True)

# Define the clickable area (e.g., a rectangle for a button or object in the room)
clickable_area1 = pygame.Rect(150, 290, 150, 220)  # Rectangle at (150, 290) with width 150 and height 220


def slow_print(text, delay=0.05):
    """Prints text to the screen slowly, character by character."""
    current_text = ""
    for char in text:
        current_text += char
        screen.blit(background_image, (0, 0))
        rendered_text = font.render(current_text, True, (255, 255, 255))
        screen.blit(rendered_text, (340, 150))
        pygame.display.flip()
        time.sleep(delay)


def main():
    quotes = [
        "Welcome to the third and final escape room.",
        "Press on objects to play the puzzles and escape.",
        "In order to make it out, find all 3 keys by completing puzzles."
    ]


    for quote in quotes:
        slow_print(quote, 0.03)  # Print each quote slowly
        time.sleep(0.5)  # Wait for 0.5 seconds before clearing the screen
        screen.blit(background_image, (0, 0))  # Clear the text by redrawing the background
        pygame.display.flip()  # Update the display


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Detect mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position
                    
                    # Check if the click is within the clickable area (rectangle)
                    if clickable_area1.collidepoint(mouse_x, mouse_y):
                        # Handle interaction (e.g., show a new message or trigger a puzzle)
                        slow_print("You clicked on the TV monitor!", 0.03)
                        time.sleep(0.5)
                        screen.blit(background_image, (0, 0))  # Redraw the background
                        pygame.draw.rect(screen, (255, 0, 0), clickable_area1, 3)  # Redraw the rectangle
                        pygame.display.flip()

        # Draw the clickable area (optional: for debugging purposes)
        pygame.draw.rect(screen, (255, 0, 0), clickable_area1, 3)  # Draw a red rectangle around the clickable area

        pygame.display.flip()  # Make sure the screen updates after each event

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
