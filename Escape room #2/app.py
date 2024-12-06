import time
import pygame
import sys

pygame.init()

screen_width = 1920
screen_height = 1017

background_image = pygame.image.load('image.jpg')  # Add your own background image
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Room #2")

font = pygame.font.SysFont("Courier New", 50, bold = True)

clickable_area1 = pygame.Rect(1300, 700, 150, 220)
clickable_area2 = pygame.Rect(600, 700, 100, 80)


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
        "Welcome to the second room,"
        "you only have x minutes to find all of the keys and escape"
        
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


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos() 
                    if clickable_area1.collidepoint(mouse_x, mouse_y):
                        slow_print("You've found a safe!", 0.03)
                        time.sleep(0.5)
                        screen.blit(background_image, (0, 0))  
                        pygame.draw.rect(screen, (255,255, 255), clickable_area1, 3) 
                        pygame.display.flip()


                    elif clickable_area2.collidepoint(mouse_x, mouse_y):
                        slow_print("You've found a paper!", 0.03)
                        time.sleep(0.5)
                        screen.blit(background_image, (0, 0))  
                        pygame.draw.rect(screen, (255, 255, 255), clickable_area2, 3)  
                        pygame.display.flip()
        screen.blit(background_image, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), clickable_area1, 3) 
        pygame.draw.rect(screen, (255, 255, 255), clickable_area2, 3) 
        pygame.display.flip()


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

 




    


    