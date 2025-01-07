import time
import pygame
import sys
from bookpuzzle import MiniPuzzleGame

pygame.init()

screen_width = 1920
screen_height = 1017

background_image = pygame.image.load('Room_3.png')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

book_image = pygame.image.load('openbook.jpg')
book_image = pygame.transform.scale(book_image, (screen_width, screen_height))

camera_image = pygame.image.load('surveillance monitor.jpg')
camera_image = pygame.transform.scale(camera_image, (screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Room")

font = pygame.font.SysFont("Courier New", 34, bold=True, italic=True)

clickable_TV = pygame.Rect(150, 290, 150, 220)
clickable_book = pygame.Rect(1060, 280, 95, 120)


class mainground:
    def __init__(self, screen, background_image, font, clickable_TV, clickable_book, camera_image, book_image):
        self.screen = screen
        self.background_image = background_image
        self.font = font
        self.clickable_TV = clickable_TV
        self.clickable_book = clickable_book
        self.camera_image = camera_image
        self.book_image = book_image
        self.is_playing_puzzle = False  # Flag to track if a puzzle is being played
        self.intro_shown = False  # Flag to track if the intro has been shown

    def draw_text(self, screen, text, x, y, font, color):
        """Method to render and draw text on the screen"""
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

    def slow_print(self, text, delay=0.05):
        """Prints text to the screen slowly, character by character."""
        current_text = ""
        for char in text:
            current_text += char
            self.screen.blit(self.background_image, (0, 0))
            self.draw_text(self.screen, current_text, 340, 150, self.font, (255, 255, 255))
            pygame.display.flip()
            time.sleep(delay)

    def return_to_main(self):
        """Return to the main game view after finishing a puzzle."""
        self.is_playing_puzzle = False
        if not self.intro_shown:
            self.main()  # Only show the intro if it hasn't been shown already
        else:
            self.screen.blit(self.background_image, (0, 0))
            pygame.display.flip()

    def restart_puzzle(self):
        """Restart the mini puzzle (called when the player loses)."""
        mini_game = MiniPuzzleGame(width=1920, height=1017, player_size=50, target_size=30, player_speed=7.2, num_targets=11)
        mini_game.game_loop(self.restart_puzzle, self.return_to_main)  # Restart the puzzle on loss, return to main on win

    def main(self):
        quotes = [
            "Welcome to the third and final escape room.",
            "Press on objects to play the puzzles and escape.",
            "In order to make it out, find all 3 keys by completing puzzles.",
            "Who was here last? I think they left something."
        ]

        if not self.intro_shown:
            for quote in quotes:
                self.slow_print(quote, 0.03)
                time.sleep(0.5)
                self.screen.blit(self.background_image, (0, 0))
                pygame.display.flip()

            self.intro_shown = True  # Mark that the intro has been shown

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = pygame.mouse.get_pos()

                        if self.clickable_TV.collidepoint(mouse_x, mouse_y):
                            self.slow_print("You found the camera TV monitor!", 0.03)
                            time.sleep(0.5)
                            self.slow_print("Complete this puzzle for the key and your next hint.", 0.03)
                            time.sleep(0.5)
                            self.slow_print("It looks like they went to get a book.", 0.03)
                            time.sleep(0.5)
                            self.screen.blit(self.background_image, (0, 0))
                            self.screen.blit(self.camera_image, (0, 0))
                            pygame.display.flip()

                        if self.clickable_book.collidepoint(mouse_x, mouse_y):
                            self.slow_print("You found the bookshelf!", 0.03)
                            time.sleep(0.5)
                            self.slow_print("Complete the final puzzle for the last key to escape.", 0.03)
                            time.sleep(0.5)
                            self.screen.blit(self.background_image, (0, 0))
                            self.screen.blit(self.book_image, (0, 0))
                            pygame.display.flip()
                            self.slow_print("Collect all 11 blue squares in TEN SECONDS using arrow keys to move on.", 0.03)
                            time.sleep(0.5)
                            # Start the MiniPuzzleGame after clicking the book
                            mini_game = MiniPuzzleGame(width=1920, height=1017, player_size=50, target_size=30, player_speed=7.2, num_targets=11)
                            mini_game.game_loop(self.restart_puzzle, self.return_to_main)  # Pass both callbacks here
                            self.slow_print("You gained 1 escape key!", 0.03)
                            time.sleep(0.5)
                            pygame.display.flip()

            if not self.is_playing_puzzle:
                self.screen.blit(self.background_image, (0, 0))
                pygame.draw.rect(self.screen, (255, 0, 0), self.clickable_TV, 3)
                pygame.draw.rect(self.screen, (255, 0, 0), self.clickable_book, 3)
                pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = mainground(screen, background_image, font, clickable_TV, clickable_book, camera_image, book_image)
    game.main()