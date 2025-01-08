import pygame
import sys
import time


class Lock():
    def __init__(self):
        pygame.init()
        self.screen_width = 1920
        self.screen_height = 1017
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Escape Room")
        
        self.background_image = pygame.image.load('lock.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))
        
        self.font = pygame.font.SysFont("Courier New", 25, bold = True)
        self.messages =  [f"It's a safe! To unlock it you have to enter a 4-digit code.",
            "Use the code you recieved from the Caesar Cipher.",
            "Make sure to enter each digit one at a time."]
        self.correct_digits = [6, 2, 1, 5]
        self.current_digit = 0
        self.guess_history = []
        self.user_input = ''
    
    def draw_screen(self):
        self.screen.blit(self.background_image,(0, 0))
        
        for i, message in enumerate(self.messages):
            text = self.font.render(message, True, (255, 255, 255))
            self.screen.blit(text, (50, 50 + i * 60))

        input_text = self.font.render(f'Current input: {self.user_input}', True, (255, 255, 0))
        self.screen.blit(input_text, (1150, 55))
        history_text = f'Code history: {self.guess_history}'
        history_rendered = self.font.render(history_text, True, (255, 255, 255))
        self.screen.blit(history_rendered, (1150, 117))
        
        pygame.display.update()
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.user_input.isdigit() and len(self.user_input) > 0:
                        guess = int(self.user_input)
                        self.guess_history.append(guess)
                        self.check_guess(guess)
                        self.user_input = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.user_input = self.user_input[:-1]
                elif event.unicode and event.unicode.isdigit():
                    self.user_input += event.unicode
                    
    def check_guess(self, guess):
        if self.current_digit < len(self.correct_digits):
            if guess == self.correct_digits[self.current_digit]:
                self.messages.append('What you entered is the correct! Enter the next digit:')
                self.current_digit += 1
                if self.current_digit >= len(self.correct_digits):
                    self.messages.append("You've unlocked the safe!")
                    import first_room3
                    first_room3.main()
            else:
                self.messages.append("That's incorrect! Try again!")
    def run(self):
        while True:
            self.handle_input()
            self.draw_screen()
if __name__ == '__main__':
    game = Lock()
    game.run()
