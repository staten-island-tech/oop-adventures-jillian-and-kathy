import time
import pygame
import sys


class Paper():
    def __init__(self):
        pygame.init()
        self.screen_width = 1920
        self.screen_height = 1017
        self.background_image = pygame.image.load('Your paragraph text.png')  
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.font = pygame.font.SysFont("Courier New", 30, bold = True)
    def slow_print(self, text, delay=0.01):
        """Prints text to the screen slowly, character by character."""
        self.current_text = ""
        for char in text:
            self.current_text += char
            self.screen.blit(self.background_image, (0, 0))
            self.rendered_text = self.font.render(self.current_text, True, (209, 209, 209))
            self.screen.blit(self.rendered_text, (50, 50))
            self.game_over = False
            pygame.display.flip()
            time.sleep(delay)
    def main(self):
        quotes = [
            "Looks like it's a document. Maybe you could use this for something..."
            "Click on the 'X' to exit"
        ]

        for quote in quotes:
            self.slow_print(quote, 0.001)  
            time.sleep(1)  
            self.screen.blit(self.background_image, (0, 0)) 
            pygame.display.flip()  

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.screen.blit(self.background_image, (0, 0))  
                    pygame.display.flip()
if __name__ == "__main__":
    game = Paper()
    game.main()