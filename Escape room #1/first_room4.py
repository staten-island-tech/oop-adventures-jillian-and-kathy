import time
import pygame
import sys
from key import Key

pygame.init()

screen_width = 1920
screen_height = 1017

background_image = pygame.image.load('start_room_official.jpg')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Room")

font = pygame.font.SysFont("Courier New", 30, bold = True, italic = True)

def slow_print(text, delay=0.05):
    current_text = ""
    for char in text:
        current_text += char
        screen.blit(background_image, (0, 0))
        rendered_text = font.render(current_text, True, (255, 255, 255))
        screen.blit(rendered_text, (50, 50))
        pygame.display.flip()
        time.sleep(delay)

class FirstRoom4:
    def __init__(self):
        self.key = Key("First Key")

    def enter(self, inventory):
        inventory.append(self.key)
        slow_print("You have recieved a key!", 0.05)
        pygame.time.delay(1000)
        slow_print("Now you can unlock the door to the next room.", 0.05)
        pygame.time.delay(1000)

def main():
    inventory = []
    first_room4 = FirstRoom4()
    first_room4.enter(inventory)
    slow_print("Your inventory contains:", 0.05)
    pygame.time.delay(1000)
    for key in inventory:
        slow_print(f"{str(key)}")
        pygame.time.delay(1000)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background_image, (0, 0))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()