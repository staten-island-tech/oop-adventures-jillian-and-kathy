import pygame
import sys

pygame.init()
screen_width = 1920
screen_height = 1017
background_image = pygame.image.load('output.jpg')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("safe")
font = pygame.font.SysFont("Courier New", 50, bold = True)

def slow_print(text, delay=0.01):
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
        "This is a safe, to open it you have to get the four-digit code right. I wonder whats inside?"
        
        
    ]

    for quote in quotes:
        slow_print(quote, 0.01)  
        time.sleep(1)  
        screen.blit(background_image, (0, 0)) 
        pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False









""" digit1 = 1
digit2 = 2
digit3 = 2
digit4 = 9 
class puzzle1():
    print('This is a safe, to open it you have to get the four-digit code right. I wonder whats inside?')
    def get_all_digits():
        correct_digits = [digit1, digit2, digit3, digit4]
        for i in range(4):
            print(f'Guess the digit {i + 1}:  (hint: use your resources)')
            guess = int(input("Guess a number from 1-10: "))
            digit_history = []
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


























