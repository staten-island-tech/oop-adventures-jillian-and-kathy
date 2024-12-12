import pygame
import random
import sys

screen_width = 1920
screen_height = 1017


class Lock():
    def __init__(self, code):
        self.code = code
        self.locked = True
        self.image = pygame.image.load('lock.jpg')
        self.image = pygame.transform.scale(self.image, (screen_width, screen_height))
        if len(code) != 4 or not all(char.isdigit() for char in code):
            raise ValueError("Code must be a 4 digits.")
    
    def correct_code(self, attempt):
        if attempt == self.code:
            self.locked = False
            print("Unlocking...Lock is now open!")
        else:
            print("Incorrect code, try again!")

    def __str__(self):
        if self.locked:
            return self.lock_image()
        else:
            return "Lock is now open."

    def lock_image(self):
        return self.image

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
            "Maybe try inputting the code you got from the Caesar Cipher?"
    ]

    for quote in quotes:
        slow_print(quote, 0.05)
        time.sleep(1)
        screen.blit(background_image, (0, 0))
        pygame.display.flip()


def main():
    pygame.init()
    screen_width, screen_height = 1920, 1017
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    lock = Lock('6215')
    code_input = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    lock.correct_code(code_input)
                    code_input = ""
                elif event.key >= pygame.K_0 and event.key <= pygame.K_9:
                    digit = str(event.key - pygame.K_0)
                    code_input += digit
        screen.fill((255, 255, 255))
        screen.blit(lock.image, (0, 0))
        x = screen_width // 2 - 15 + len(code_input) * 30
        y = screen_height // 2 - 50
        for i in range(len(code_input)):
            text_surface = font.render(code_input[i], True, (0, 0, 0))
            screen.blit(text_surface, (x + i * 30, y))
        pygame.display.flip()
        
        clock.tick(60)

if __name__ == "__main__":
    main()