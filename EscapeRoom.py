import time
import pygame
import sys

pygame.init()

screen_width = 1080
screen_height = 675

background_image = pygame.image.load('escape-room.jpg')  # Add your own background image
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Room")

font = pygame.font.Font(None, 36)

def wrap_text(text, font, max_width):
    """Wrap text to fit within a specified width."""
    words = text.split(' ')
    lines = []
    current_line = ""
    
    for word in words:
        # Check if adding the word would exceed the max width
        test_line = current_line + word + ' '
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)  # Append current line to lines
            current_line = word + ' '  # Start a new line with the current word
            
    if current_line:  # Add any remaining text
        lines.append(current_line)
        
    return lines

def slow_print(text, delay=0.1):
    """Prints text to the console slowly, character by character."""
    current_text = ""
    for char in text:
        current_text += char
        screen.blit(background_image, (0, 0))
        rendered_text = font.render(current_text, True, (255, 255, 255))
        screen.blit(rendered_text, (50, 50))
        pygame.display.flip()
        time.sleep(delay)

def main():
    intro_text = (
        "Welcome to the Neon Nexus, a sprawling megacity where neon lights flicker against the backdrop of rain-soaked streets."
        " You and your team are a group of underground hackers who have stumbled upon a corporation's dark secrets."
        " The megacorp has caught wind of your investigation and has locked you inside their secure facility."
        " Your mission is to escape from three high-security rooms before the corporate enforcers arrive to silence you permanently."
        " Time to get started!")

    slow_print(intro_text, 0.1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

