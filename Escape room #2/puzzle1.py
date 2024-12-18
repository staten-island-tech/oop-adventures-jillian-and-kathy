import pygame
import sys

class Puzzle1():
    def __init__(self):
        pygame.init()
        self.screen_width = 1920
        self.screen_height = 1017
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.messages =  ['This is a safe, to open it you have to get the four-digit code right. I wonder whats inside Hint: use your resources to make this process faster']
        self.background_image = pygame.image.load('output.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))
        self.font = pygame.font.SysFont("Courier New", 20, bold = True)
        self.correct_digits = [1, 2, 2, 9]
        self.current_digit = 0
        self.guess_history = []
        self.user_input = ''
        self.game_over = False
    def draw_screen(self):
        self.screen.blit(self.background_image,(0, 0))
        for i, message in enumerate(self.messages):
            text = self.font.render(message, True, (255, 255, 255))
            self.screen.blit(text, (50, 50 + i * 60))
        digit_message = f'Guess the digit {self.current_digit + 1}: (Guess a number from 1-9)'
        digit_text = self.font.render(digit_message, True, (255, 255, 255))
        self.screen.blit(digit_text, (600, 100))
        input_text = self.font.render(self.user_input, True, (255, 255, 0))
        self.screen.blit(input_text, (1350, 100))
        history_text = f'Guess history: {self.guess_history}'
        history_rendered = self.font.render(history_text, True, (255, 255, 255))
        self.screen.blit(history_rendered, (600, 125))
        pygame.display.update()
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
            self.messages.append('Your guess is correct!')
            self.current_digit += 1
            if self.current_digit >= len(self.correct_digits):
                self.messages.append("You've opened the safe!")
                self.game_over == True
        else:
            if guess < self.correct_digits[self.current_digit]:
                self.messages.append('Your guess is too low! Try again!')
            else:
                self.messages.append('Your guess is too high! Try again!')
    def run(self):
        while True:
            self.handle_input()
            self.draw_screen()
            if self.game_over:
                pygame.time.delay(2000)
                break
    pygame.quit()
    

if __name__ == '__main__':
    game = Puzzle1()
    game.run()
    

    """ def get_all_digits():
        for i in range(4):
            print(f'Guess the digit {i + 1}:  (hint: use your resources)')
            guess = int(input("Guess a number from 1-10: "))
            while guess != correct_digits[i]:       
                digit_history.append(guess)
                print (f'Guess history for digit {i + 1}: {digit_history}')
                if guess == correct_digits[i]:
                    print('Your guess is correct!')
                elif guess <  correct_digits[i]:
                    print('Your guess is too low! Try again!')
                    guess = int((input('Guess again: ')))
                    print(f'Guess history: {history}')
                elif guess >  correct_digits[i]:
                    print('Your guess is too high! Try again!')
                    guess = int((input('Guess again: ')))
                    print(f'Guess history: {history}')
                else:
                    print('Error. Try again!')
                if guess ==  correct_digits[i]:
                    print('Your guess is correct!')
    get_all_digits()  
 """



























