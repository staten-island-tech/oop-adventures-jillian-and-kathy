import time
import pygame
import sys


class WordleGame:
    def __init__(self, word, hint):
        self.word = word
        self.hint = hint
        self.guess_history = []
        self.infinite = True
        self.double = []
        self.current_guess = ""

    def make_guess(self, enter):
        """Method to handle a single guess."""
        self.guess_history.append(enter)
        self.current_guess = ""

        if enter == self.word:
            self.infinite = False
            return f"The word is {self.word.upper()}! Congrats!!!"
        elif len(enter) != len(self.word):
            return "Must be a 5-letter word"
        else:
            feedback = ""
            for letter in range(len(enter)):
                if enter[letter] == self.word[letter]:
                    feedback += f"{enter[letter]} is correct and in the right spot.\n"
                    self.double.append(enter[letter])
                elif enter[letter] in self.word and enter[letter] not in self.double:
                    feedback += f"{enter[letter]} is either not in the word or is in the wrong spot. Figure it out!\n"
                    self.double.append(enter[letter])
                elif enter[letter] not in self.word or enter[letter] in self.double:
                    feedback += f"{enter[letter]} is either not in the word or is in the wrong spot. Figure it out!\n"
            return feedback

    def display_hint(self):
        return f"Here is a hint: {self.hint}"

    def play_game(self, screen, font, game_instance, word, hint, book_image):
        """Method to play the Wordle game within Pygame."""
        hint_text = self.display_hint()
        feedback_text = ""
        current_input = ""

        while self.infinite:
            self.screen.blit(self.background_image, (0, 0))
            game_instance.draw_text(screen, hint_text, 20, 20, font, (0, 0, 0))  # Display the hint
            game_instance.draw_text(screen, feedback_text, 20, 100, font, (0, 0, 0))  # Display feedback

            # Input box for entering guesses
            game_instance.draw_text(screen, current_input, 20, 200, font, (0, 0, 255))  # Show current input

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.infinite = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Enter key is pressed
                        if len(current_input) == 5:
                            feedback_text = self.make_guess(current_input)
                            current_input = ""  # Reset the input field
                    elif event.key == pygame.K_BACKSPACE:  # Backspace key
                        current_input = current_input[:-1]
                    else:
                        if len(current_input) < 5:  # Limit input length to 5 characters
                            current_input += event.unicode

            pygame.display.flip()
            pygame.time.Clock().tick(30)  # Control the frame rate

""" class WordleGame:
    def __init__(self, word, hint):
        self.word = word
        self.hint = hint
        self.guess_history = []
        self.infinite = True
        self.double = []

    def make_guess(self, enter):
        self.guess_history.append(enter)
        print("Your guesses: ", self.guess_history)

        if enter == self.word:
            self.infinite = False
            print("The word is", self.word.upper() + "! Congrats!!!")
        elif len(enter) != len(self.word):
            print("Must be a 5-letter word")
        else:
            for letter in range(len(enter)):
                if enter[letter] == self.word[letter]:
                    print(enter[letter], "is correct and in the right spot.")
                    self.double.append(enter[letter])
                elif enter[letter] in self.word and enter[letter] not in self.double:
                    print(enter[letter], "is either not in the word or is in the wrong spot. Figure it out!")
                    self.double.append(enter[letter])
                elif enter[letter] not in self.word or enter[letter] in self.double:
                    print(enter[letter], "is either not in the word or is in the wrong spot. Figure it out!")

    def display_hint(self):
        print("Here is a hint:", self.hint)

    def play_game(self):
        print("Your final puzzle is a Wordle")
        self.display_hint()

        while self.infinite:
            enter = input("Enter your 5 letter guess: ")
            self.make_guess(enter)

game = WordleGame(word="debug", hint="Related to fixing code")
game.play_game() """


""" word = "debug"
guesshistory = []
infinite = True
print("Your final puzzle is a Wordle")
print("Here is a hint:", "Related to fixing code")
while infinite == True:
    enter = input("Enter your 5 letter guess: ")
    guesshistory.append(enter)
    double = []
    print("Your guesses: ", guesshistory)
    if enter == word:
        infinite = False
        print("The word is DEBUG! Congrats!!!")
    elif len(enter) != len(word):
        print("Must be 5 letter word")
    elif len(enter) == len(word):
        for letter in range(len(enter)):
            if enter[letter] == word[letter]:
                print(enter[letter], "is correct and in the right spot.")
                double.append(enter[letter])
            elif enter[letter] in word and enter[letter] not in double:
                print(enter[letter], "is either not in the word or is in the wrong spot. Figure it out!")
                double.append(enter[letter])
            elif enter[letter] not in word or enter[letter] in double:
                print(enter[letter], "is either not in the word or is in the wrong spot. Figure it out!") """