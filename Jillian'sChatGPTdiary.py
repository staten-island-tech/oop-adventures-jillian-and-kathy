1. I need to write a code for an escape room that has slow printing text with a background image
This is what AI gave me:
def slow_print(text, delay=0.10):
    current_text = ""
    for char in text:
        current_text += char
        screen.blit(background_image, (0, 0))
        rendered_text = font.render(current_text, True, (255, 255, 255))
        screen.blit(rendered_text, (50, 50))
        pygame.display.flip()
        time.sleep(delay)

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
            "Make sure to enter each digit one at a time."]
        self.correct_digits = [6, 2, 1, 5]
        self.current_digit = 0
        self.guess_history = []
        self.user_input = ''

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

Some properties of the number guessing game were incorporated

3. I need to write a code that imports a file into another file that includes classes in python
AI gave me:
    import tiles_game
    tiles_game.main()
so I put into this code:
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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

first_room4.py:
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

This added one key to inventory when they are done with my portion of the game