1. I need to write a code for an escape room that has slow printing text with a background image
<<<<<<< Updated upstream
This is what AI gave me:
def slow_print(text, delay=0.10):
=======
The code they gave me:
def slow_print(text, delay=0.05):
>>>>>>> Stashed changes
    current_text = ""
    for char in text:
        current_text += char
        screen.blit(background_image, (0, 0))
        rendered_text = font.render(current_text, True, (255, 255, 255))
        screen.blit(rendered_text, (50, 50))
        pygame.display.flip()
        time.sleep(delay)

<<<<<<< Updated upstream
I incorporated this slow_print function into the code so that the messages would print differently and make it more "escape room-like"



2. I need to write a code for a lock that has a four number code in python
This is what AI gave me:
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
=======


2. I need to write a code for a lock that has a four number code in python
I didnt know how to write the code for a lock that recieves user input so I used some of the code from number guessing game and got some from AI:
self.messages =  [f"It's a safe! To unlock it you have to enter a 4-digit code.",
>>>>>>> Stashed changes
            "Make sure to enter each digit one at a time."]
        self.correct_digits = [6, 2, 1, 5]
        self.current_digit = 0
        self.guess_history = []
        self.user_input = ''
<<<<<<< Updated upstream

=======
    
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
    
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream

Some properties of the number guessing game were incorporated

3. I need to write a code that imports a file into another file that includes classes in python
AI gave me:
    import tiles_game
    tiles_game.main()
so I put into this code:
=======
    def run(self):
        while True:
            self.handle_input()
            self.draw_screen()

I also changed some of the positions of the messages so it would fit better on the screen.

3. I need to write a code that imports a file into another file in python
AI gave me the code:
import (file name)
(file name).main()
which I put after:

>>>>>>> Stashed changes
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
<<<<<<< Updated upstream

    pygame.display.flip()
    import tiles_game
    tiles_game.main()
which didnt work because you would have to exit out of the page in order to go to the next part so i did this:

    running = True
    import tiles_game
    tiles_game.main()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.display.flip()
this made it go to the next page automatically after the messages were printed


4. I need to write a code that uses keys and an inventory that is able to collect one key after each 3 rooms across different files
key.py:
class Key:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Key: {self.name}"
inventory.py: 
=======


        
    pygame.display.flip()
    import tiles_game
    tiles_game.main()

which only worked when I exited out of the page, so I figured out that I had to switch it to a different place so it switches automatically:

    running = True
    import tiles_game
    tiles_game.main()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        
    pygame.display.flip()

4. how to create a class of keys in escape room game python that appends one key after each room, there are 3 rooms across different files

key.py:
class Key:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Key: {self.name}"

inventory.py:
>>>>>>> Stashed changes
from key import Key

class Inventory:
    def __init__(self, keys):
        self.keys = []

    def add_key(self, key):
        self.keys.append(key)

    def count_keys(self):
        return len(self.keys)

    def __str__(self):
        return f"Inventory: {', '.join(str(key) for key in self.keys)}"

<<<<<<< Updated upstream
first_room4.py:
=======
firstroom4.py:
>>>>>>> Stashed changes
class FirstRoom4:
    def __init__(self):
        self.key = Key("First Key")

    def enter(self, inventory):
        inventory.append(self.key)
        slow_print("You have recieved a key!", 0.05)
        pygame.time.delay(1000)
        slow_print("Now you can unlock the door to the next room.", 0.05)
        pygame.time.delay(1000)

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
def main():
    inventory = []
    first_room4 = FirstRoom4()
    first_room4.enter(inventory)
    slow_print("Your inventory contains:", 0.05)
    pygame.time.delay(1000)
    for key in inventory:
        slow_print(f"{str(key)}")
<<<<<<< Updated upstream
        pygame.time.delay(1000)

This added one key to inventory when they are done with my portion of the game
=======
        pygame.time.delay(1000)
>>>>>>> Stashed changes
