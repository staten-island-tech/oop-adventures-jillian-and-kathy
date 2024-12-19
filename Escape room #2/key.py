import pygame
import sys
import time

class Key():
    def __init__(self):
        pygame.init()
        self.screen_width = 1920
        self.screen_height = 1017
        self.background_image = pygame.image.load('key.jpg')  # Add your own background image
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Key")
        self.font = pygame.font.SysFont("Courier New", 50, bold = True)
        self.clickable_area1 = pygame.Rect(1300, 700, 150, 220)
    def slow_print(self, text, delay=0.01):
        """Prints text to the screen slowly, character by character."""
        current_text = ""
        for char in text:
            current_text += char
            self.screen.blit(self.background_image, (0, 0))
            self.rendered_text = self.font.render(current_text, True, (255, 255, 255))
            self.screen.blit(rendered_text, (50, 50))
            pygame.display.flip()
            time.sleep(delay)
    def main(self):
        quotes = [
            "Congrats! You've opened the safe, it looks like theres a key inside...click on it to equip it"
        ]

        for quote in quotes:
            self.slow_print(quote, 0.01)  
            time.sleep(1)  
            self.screen.blit(background_image, (0, 0)) 
            pygame.display.flip()  

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = pygame.mouse.get_pos() 
                        if self.clickable_area1.collidepoint(mouse_x, mouse_y):
                            self.slow_print("You've equipped a key", 0.03)
                            time.sleep(0.5)
                            self.screen.blit(background_image, (0, 0))  
                            pygame.draw.rect(screen, (255,255, 255), self.clickable_area1, 3) 
                            pygame.display.flip()
                self.screen.blit(self.background_image, (0, 0))
                pygame.draw.rect(self.screen, (255, 255, 255), self.clickable_area1, 3)
                pygame.display.flip()
            pygame.quit()
            sys.exit()
if __name__ == '__main__':
    game = Key()
    game.main()

