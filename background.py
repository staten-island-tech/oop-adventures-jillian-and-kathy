import time
import pygame
import sys

pygame.init()


screen_width = 1920
screen_height = 1017


background_image = pygame.image.load('Room_3.png')  # Add your own background image
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

book_image = pygame.image.load('openbook.jpg')  # Add your own background image
book_image = pygame.transform.scale(book_image, (screen_width, screen_height))

camera_image = pygame.image.load('surveillance monitor.jpg')  # Add your own background image
camera_image = pygame.transform.scale(camera_image, (screen_width, screen_height))

plate_image = pygame.image.load('emptyplate.jpg')  # Add your own background image
plate_image = pygame.transform.scale(plate_image, (screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Room")


font = pygame.font.SysFont("Courier New", 34, bold = True, italic = True)

# Define the clickable area (e.g., a rectangle for a button or object in the room)
clickable_TV = pygame.Rect(150, 290, 150, 220)  # Rectangle at (150, 290) with width 150 and height 220
clickable_plate = pygame.Rect(898, 590, 100, 60)  # Rectangle at (898, 570) with width 100 and height 50
clickable_book = pygame.Rect(1060, 280, 95, 120)  # Rectangle at (898, 570) with width 100 and height 50

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
    
    def slow_print(self, text, delay=0.05):
        """Prints text to the screen slowly, character by character."""
        current_text = ""
        for char in text:
            current_text += char
            screen.blit(background_image, (0, 0))
            rendered_text = font.render(current_text, True, (255, 255, 255))
            screen.blit(rendered_text, (340, 150))
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
            self.slow_print(quote, 0.03)  # Print each quote slowly
            time.sleep(0.5)  # Wait for 0.5 seconds before clearing the screen
            self.screen.blit(self.background_image, (0, 0))  # Clear the text by redrawing the background
            pygame.display.flip()  # Update the display


        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Detect mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position
                        
                        # Check if the click is within the clickable area 1(rectangle)
                        if clickable_TV.collidepoint(mouse_x, mouse_y):
                            # Handle interaction (e.g., show a new message or trigger a puzzle)
                            self.slow_print("You found the camera TV monitor!", 0.03)
                            time.sleep(0.5)
                            self.slow_print("Complete this puzzle for the key and your next hint.", 0.03)
                            time.sleep(0.5)
                            self.slow_print("It looks like they went to get a book.", 0.03)
                            time.sleep(0.5)
                            screen.blit(camera_image, (0, 0))  # Redraw the background
                            pygame.display.flip()

                        # Check if the click is within the clickable area 2(rectangle)
                        if clickable_plate.collidepoint(mouse_x, mouse_y):
                            # Handle interaction (e.g., show a new message or trigger a puzzle)
                            self.slow_print("You found the food plate!", 0.03)
                            time.sleep(0.5)
                            self.slow_print("Complete the puzzle for the key and a hint.", 0.03)
                            time.sleep(0.5)
                            self.slow_print("Check the cameras to see who was here.", 0.03)
                            time.sleep(0.5)
                            screen.blit(plate_image, (0, 0))  # Redraw the background
                            pygame.display.flip()

                        # Check if the click is within the clickable area 3(rectangle)
                        if clickable_book.collidepoint(mouse_x, mouse_y):
                            # Handle interaction (e.g., show a new message or trigger a puzzle)
                            self.slow_print("You found the bookshelf!", 0.03)
                            time.sleep(0.5)
                            self.slow_print("Complete the final puzzle for the last key to escape.", 0.03)
                            time.sleep(0.5)
                            screen.blit(book_image, (0, 0))  # Redraw the background
                            pygame.display.flip()
                            from bookpuzzle import WordleGame 

            # Draw the clickable area (optional: for debugging purposes)
            pygame.draw.rect(screen, (255, 0, 0), clickable_TV, 3)  # Draw a red rectangle around the clickable area 1

            # Draw the clickable area (optional: for debugging purposes)
            pygame.draw.rect(screen, (255, 0, 0), clickable_plate, 3)  # Draw a red rectangle around the clickable area 2

            # Draw the clickable area (optional: for debugging purposes)
            pygame.draw.rect(screen, (255, 0, 0), clickable_book, 3)  # Draw a red rectangle around the clickable area 2

            pygame.display.flip()  # Make sure the screen updates after each event

        pygame.quit()
        sys.exit()



if __name__ == "__main__":
    game = mainground(screen, background_image, font, clickable_TV, clickable_plate, clickable_book, camera_image, plate_image, book_image)
    game.main()