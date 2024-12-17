""" import pygame
import random
import sys
import time

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

    def lock_image(self):
        return self.image

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
    main() """

""" import pygame
import random
import sys
import time

screen_width = 1920
screen_height = 1017

class Lock():
    def __init__(self, code):
        self.code = code
        self.locked = True
        self.image = pygame.image.load('lock.jpg')
        self.image = pygame.transform.scale(self.image, (screen_width, screen_height))
        if len(code) != 4 or not all(char.isdigit() for char in code):
            raise ValueError("Code must be 4 digits.")
    
    def correct_code(self, attempt):
        if attempt == self.code:
            self.locked = False
            print("Unlocking... Lock is now open!")
        else:
            print("Incorrect code, try again!")

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
    global screen, background_image, font
    
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.font.init()
    font = pygame.font.Font(None, 48)  # Provide a font for rendering text
    clock = pygame.time.Clock()

    # Load the background image
    background_image = pygame.image.load('lock.jpg')  # Ensure you have this file

    lock = Lock('6215')
    code_input = ""

    quotes = [
        "Maybe try inputting the code you got from the Caesar Cipher?"
    ]

    for quote in quotes:
        slow_print(quote, 0.05)
        time.sleep(1)
        screen.blit(background_image, (0, 0))
        pygame.display.flip()

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
        screen.blit(lock.lock_image(), (0, 0))  # Use the lock_image method
        x = screen_width // 2 - 15 + len(code_input) * 30
        y = screen_height // 2 - 50
        for i in range(len(code_input)):
            text_surface = font.render(code_input[i], True, (0, 0, 0))
            screen.blit(text_surface, (x + i * 30, y))
        pygame.display.flip()
        
        clock.tick(60)

if __name__ == "__main__":
    main() """

""" import pygame
import sys
import time

# Initialize screen dimensions
screen_width = 1920
screen_height = 1017

class Lock():
    def __init__(self, code):
        self.code = code
        self.locked = True
        self.image = pygame.image.load('lock.jpg')  # Ensure this file exists
        self.image = pygame.transform.scale(self.image, (screen_width, screen_height))
        if len(code) != 4 or not all(char.isdigit() for char in code):
            raise ValueError("Code must be a 4 digits.")
    
    def correct_code(self, attempt):
        if attempt == self.code:
            self.locked = False
            print("Unlocking... Lock is now open!")
        else:
            print("Incorrect code, try again!")

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
    global screen, background_image, font
    
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.font.init()
    font = pygame.font.Font(None, 48)  # Create a default font

    # Load the background image
    try:
        global background_image
        background_image = pygame.image.load('start_room_official.jpg')  # Ensure this file exists
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    except pygame.error as e:
        print(f"Could not load background image: {e}")
        pygame.quit()
        sys.exit()

    lock = Lock('6215')
    code_input = ""

    # Display introductory text
    quotes = [
        "Maybe try inputting the code you got from the Caesar Cipher?"
    ]
    for quote in quotes:
        slow_print(quote, 0.05)
        time.sleep(1)
        screen.blit(background_image, (0, 0))
        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    lock.correct_code(code_input)
                    code_input = ""  # Reset the input after checking the code
                elif event.key >= pygame.K_0 and event.key <= pygame.K_9:
                    digit = str(event.key - pygame.K_0)
                    code_input += digit
        
        screen.blit(background_image, (0, 0))  # Clear screen with background
        x = screen_width // 2 - 15 + len(code_input) * 30
        y = screen_height // 2 - 50
        
        # Render the current code input
        for i in range(len(code_input)):
            text_surface = font.render(code_input[i], True, (0, 0, 0))
            screen.blit(text_surface, (x + i * 30, y))
        
        pygame.display.flip()  # Update the display
        pygame.time.Clock().tick(60)  # Ensure the game runs at 60 FPS

if __name__ == "__main__":
    main() """

""" import time
import pygame
import sys

pygame.init()

screen_width = 1920
screen_height = 1017

lock_image = pygame.image.load('lock.jpg')
lock_image = pygame.transform.scale(lock_image, (screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Text Input")

font = pygame.font.SysFont("Courier New", 30, bold = True, italic = True)

def slow_print(text, delay=0.05):
    current_text = ""
    for char in text:
        current_text += char
        screen.blit(lock_image, (0, 0))
        rendered_text = font.render(current_text, True, (255, 255, 255))
        screen.blit(rendered_text, (50, 50))
        pygame.display.flip()
        time.sleep(delay)

class Lock:
    def __init__(self, code):
        if len(code) != 4 or not all(char.isdigit() for char in code):
            raise ValueError("Code must be a 4 digits.")
        
        self.code = code
        self.locked = True
        self.image = pygame.image.load('lock.jpg')  # Ensure this file exists
        self.image = pygame.transform.scale(self.image, (screen_width, screen_height))
    
    def correct_code(self, attempt):
        if attempt == self.code:
            self.locked = False
            print("Unlocking... Lock is now open!")
        else:
            print("Incorrect code, try again!")

def main():
    # Display intro quote
    quotes = ["Maybe try inputting the code you got from the Caesar Cipher?"]
    for quote in quotes:
        slow_print(quote, 0.05)
        time.sleep(1)
        screen.blit(lock_image, (0, 0))
        pygame.display.flip()
    input_text = ''
    clock = pygame.time.Clock()

    # Initialize Lock and input variables
    lock = Lock("6125")  # Example code
    code_input = ""

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    lock.correct_code(code_input)
                    code_input = ""  # Reset the input after checking the code
                elif event.key == pygame.K_BACKSPACE:
                    code_input = code_input[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    digit = str(event.key - pygame.K_0)
                    code_input += digit
                else:
                    print("Invalid")

        # Clear screen with background
        screen.blit(lock_image, (0, 0))

        # Render the current code input
        x = screen_width // 2 - 15 * 2
        y = screen_height // 2 - 50
        for i in range(len(code_input)):
            text_surface = font.render(digit, True, (255, 255, 255))
            screen.blit(text_surface, (x + i * 30, y))

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Ensure the game runs at 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() """

import pygame
import sys


class Lock():
    def __init__(self):
        pygame.init()
        self.screen_width = 1920
        self.screen_height = 1017
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.messages =  [f"It's a safe! To unlock it you have to enter a 4-digit code."]
        pygame.display.set_caption("Escape Room")
        self.background_image = pygame.image.load('lock.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))
        self.font = pygame.font.SysFont("Courier New", 25, bold = True)
        self.correct_digits = [6, 2, 1, 5]
        self.current_digit = 0
        self.guess_history = []
        self.user_input = ''
    def draw_screen(self):
        self.screen.blit(self.background_image,(0, 0))
        for i, message in enumerate(self.messages):
            text = self.font.render(message, True, (255, 255, 255))
            self.screen.blit(text, (50, 50 + i * 60))
        """ digit_message = f'Guess the digit {self.current_digit + 1}: (Guess a number from 1-9)'
        digit_text = self.font.render(digit_message, True, (255, 255, 255))
        self.screen.blit(digit_text, (600, 100))
        input_text = self.font.render(self.user_input, True, (255, 255, 0))
        self.screen.blit(input_text, (1350, 100))
        history_text = f'Guess history: {self.guess_history}'
        history_rendered = self.font.render(history_text, True, (255, 255, 255))
        self.screen.blit(history_rendered, (600, 125))
        pygame.display.update() """
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.user_input.isdigit() and self.user_input != '':
                        guess = int(self.user_input)
                        self.guess_history.append(guess)
                        self.check_guess(guess)
                        self.user_input = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.user_input = self.user_input[:-1]
                else:
                    self.user_input += event.unicode
    def check_guess(self, guess):
        if guess == self.correct_digits[self.current_digit]:
            self.messages.append('What you entered is the correct code! Now the safe is unlocking...')
            self.current_digit += 1
            if self.current_digit >= len(self.correct_digits):
                self.messages.append("You've unlocked the safe!")
        else:
            if guess < self.correct_digits[self.current_digit]:
                self.messages.append("That's incorrect! Try again!")
            else:
                self.messages.append("That's incorrect! Try again!")
    def run(self):
        while True:
            self.handle_input()
            self.draw_screen()
if __name__ == '__main__':
    game = Lock()
    game.run()
