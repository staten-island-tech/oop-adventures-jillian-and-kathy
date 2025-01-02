import pygame
import random
import sys

class MiniPuzzleGame:
    def __init__(self, width=800, height=600, player_size=50, target_size=30, player_speed=5, num_targets=5, time_limit=10000):
        # Initialize Pygame
        pygame.init()
        
        # Game settings
        self.width = width
        self.height = height
        self.player_size = player_size
        self.target_size = target_size
        self.player_speed = player_speed
        self.num_targets = num_targets
        self.time_limit = time_limit  # 10 seconds time limit in milliseconds
        
        # Load the background image (open book)
        self.background_image = pygame.image.load('openbook.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        # Initialize screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Minipuzzle Game")
        
        # Colors
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        
        # Initialize player and targets
        self.player = pygame.Rect(self.width // 2, self.height // 2, self.player_size, self.player_size)
        self.targets = []

        for _ in range(self.num_targets):
            x = random.randint(0, self.width - self.target_size)
            y = random.randint(0, self.height - self.target_size)
            self.targets.append(pygame.Rect(x, y, self.target_size, self.target_size))
        
        self.font = pygame.font.Font(None, 74)
    
    def game_loop(self):
        collected_targets = 0
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()  # Get the start time

        while True:
            elapsed_time = pygame.time.get_ticks() - start_time  # Calculate elapsed time

            # Check if time is up (after 10 seconds)
            if elapsed_time > self.time_limit:
                game_over_text = self.font.render("Time's up!", True, (255, 0, 0))
                self.screen.blit(game_over_text, (self.width // 2 - game_over_text.get_width() // 2, self.height // 2 - game_over_text.get_height() // 2))
                pygame.display.flip()
                pygame.time.wait(2000)  # Show the "Time's up!" message for 2 seconds
                pygame.quit()
                sys.exit()

            self.screen.blit(self.background_image, (0, 0))  # Use the open book as the background

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Get keys pressed
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.x -= self.player_speed
            if keys[pygame.K_RIGHT]:
                self.player.x += self.player_speed
            if keys[pygame.K_UP]:
                self.player.y -= self.player_speed
            if keys[pygame.K_DOWN]:
                self.player.y += self.player_speed

            # Check for collision with targets
            for target in self.targets[:]:
                if self.player.colliderect(target):
                    self.targets.remove(target)  # Remove the collected target
                    collected_targets += 1  # Increase collected targets count

            # Draw player and targets
            pygame.draw.rect(self.screen, self.RED, self.player)
            for target in self.targets:
                pygame.draw.rect(self.screen, self.BLUE, target)

            # Check for win condition
            if collected_targets == self.num_targets:
                win_text = self.font.render("You Win!", True, (0, 255, 0))
                self.screen.blit(win_text, (self.width // 2 - win_text.get_width() // 2, self.height // 2 - win_text.get_height() // 2))

            pygame.display.flip()
            clock.tick(60)