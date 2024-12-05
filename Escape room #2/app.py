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
                pygame.quit()
                sys.exit()
if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos() 
                    if clickable_area1.collidepoint(mouse_x, mouse_y):
                        slow_print("You clicked on the TV monitor!", 0.03)
                        time.sleep(0.5)
                        screen.blit(background_image, (0, 0))  
                        pygame.draw.rect(screen, (255, 0, 0), clickable_area1, 3) 
                        pygame.display.flip()


                    if clickable_area2.collidepoint(mouse_x, mouse_y):
                        slow_print("You clicked on the food plate!", 0.03)
                        time.sleep(0.5)
                        screen.blit(background_image, (0, 0))  
                        pygame.draw.rect(screen, (255, 0, 0), clickable_area2, 3)  
                        pygame.display.flip()
pygame.draw.rect(screen, (255, 0, 0), clickable_area1, 3) 
pygame.draw.rect(screen, (255, 0, 0), clickable_area2, 3) 
pygame.display.flip()




if __name__ == "__main__":
    main()

 

#first puzzle
""" class safe_puzzle():
    def guess_code():
        first_digit = 1
        second_digit = 2
        third_digit = 2
        fourth_digit = 9
        first = ("Guess the first digit: ")
        if 'first' == first_digit:
            print('Correct!')
            if 'first' < first_digit:
                print('Incorrect! Guess higher.')
                if 'first' > first_digit:
                    print('Incorrect! Guess lower.')
                    second = ("Guess the second digit: ")
                    if 'second' == second_digit:
                        print('Correct')
                        if 'second' < second_digit:
                            print('Incorrect! Guess higher.')
                            if 'second' > sceond_digit:
                                print('Incorrect! Guess lower.')
                                if 'third' == third_digit:
                                    print('Correct')
                                    if 'third' < third_digit:
                                        print('Incorrect! Guess higher.')
                                        if 'third' > third_digit:
                                            print('Incorrect! Guess lower.')
                                            if 'fourth' == fourth_digit:
                                                print('Correct')
                                                if 'fourth' < fourth_digit:
                                                    print('Incorrect! Guess higher.')
                                                    if 'fourth' > fourth_digit:
                                                        print('Incorrect! Guess lower.')
    guess_code() """


    


    