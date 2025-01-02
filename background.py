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

plate_image = pygame.image.load('emptyplate.jpg')
plate_image = pygame.transform.scale(plate_image, (screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Room")

font = pygame.font.SysFont("Courier New", 34, bold=True, italic=True)

clickable_TV = pygame.Rect(150, 290, 150, 220)
clickable_plate = pygame.Rect(898, 590, 100, 60)
clickable_book = pygame.Rect(1060, 280, 95, 120)


class mainground:
    def __init__(self, screen, background_image, font, clickable_TV, clickable_plate, clickable_book, camera_image, plate_image, book_image):
        self.screen = screen
        self.background_image = background_image
        self.font = font
        self.clickable_TV = clickable_TV
        self.clickable_plate = clickable_plate
        self.clickable_book = clickable_book
        self.camera_image = camera_image
        self.plate_image = plate_image
        self.book_image = book_image

    def draw_text(self, screen, text, x, y, font, color):
        """Method to render and draw text on the screen"""
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

    def slow_print(self, text, delay=0.05):
        """Prints text to the screen slowly, character by character."""
        current_text = ""
        for char in text:
            current_text += char
            self.screen.blit(self.background_image, (0, 0))  # Keep the background image consistent
            self.draw_text(self.screen, current_text, 340, 150, self.font, (255, 255, 255))  # Display the current text
            pygame.display.flip()
            time.sleep(delay)

    def main(self):
        quotes = [
            "Welcome to the third and final escape room.",
            "Press on objects to play the puzzles and escape.",
            "In order to make it out, find all 3 keys by completing puzzles.",
            "Who was here last? I think they left something."
        ]

        for quote in quotes:
            self.slow_print(quote, 0.03)
            time.sleep(0.5)
            self.screen.blit(self.background_image, (0, 0))  # Clear the text by redrawing the background
            pygame.display.flip()

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
                            self.screen.blit(self.background_image, (0, 0))  # Redraw background
                            self.screen.blit(self.camera_image, (0, 0))  # Show camera image
                            pygame.display.flip()

                        if self.clickable_plate.collidepoint(mouse_x, mouse_y):
                            self.slow_print("You found the food plate!", 0.03)
                            time.sleep(0.5)
                            self.slow_print("Complete the puzzle for the key and a hint.", 0.03)
                            time.sleep(0.5)
                            self.slow_print("Check the cameras to see who was here.", 0.03)
                            time.sleep(0.5)
                            self.screen.blit(self.background_image, (0, 0))  # Redraw background
                            self.screen.blit(self.plate_image, (0, 0))  # Show plate image
                            pygame.display.flip()

                        if self.clickable_book.collidepoint(mouse_x, mouse_y):
                            self.slow_print("You found the bookshelf!", 0.03)
                            time.sleep(0.5)
                            self.slow_print("Complete the final puzzle for the last key to escape.", 0.03)
                            time.sleep(0.5)
                            self.screen.blit(self.background_image, (0, 0))  # Redraw background
                            self.screen.blit(self.book_image, (0, 0))  # Show book image
                            pygame.display.flip()

                            # Start the MiniPuzzleGame after clicking the book
                            mini_game = MiniPuzzleGame(width=1920, height=1017, player_size=50, target_size=30, player_speed=5, num_targets=5)
                            mini_game.game_loop()  # Start the mini game

            pygame.draw.rect(self.screen, (255, 0, 0), self.clickable_TV, 3)
            pygame.draw.rect(self.screen, (255, 0, 0), self.clickable_plate, 3)
            pygame.draw.rect(self.screen, (255, 0, 0), self.clickable_book, 3)

            pygame.display.flip()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = mainground(screen, background_image, font, clickable_TV, clickable_plate, clickable_book, camera_image, plate_image, book_image)
    game.main()