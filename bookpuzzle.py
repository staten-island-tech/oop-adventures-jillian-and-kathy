import pygame
import random
import sys

class MiniPuzzleGame:
    def __init__(self, width=800, height=600, player_size=50, target_size=30, player_speed=7.2, num_targets=11, time_limit=10000):
        
        pygame.init()
        
        self.width = width
        self.height = height
        self.player_size = player_size
        self.target_size = target_size
        self.player_speed = player_speed
        self.num_targets = num_targets
        self.time_limit = time_limit
        
        self.background_image = pygame.image.load('openbook.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        # Initialize screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bookpuzzle Game")
        
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
        self.timer_font = pygame.font.Font(None, 54)
    
    def reset_game(self):
        """Reset game state for a new game"""
        self.player.x = self.width // 2
        self.player.y = self.height // 2
        self.targets = []
        for _ in range(self.num_targets):
            x = random.randint(0, self.width - self.target_size)
            y = random.randint(0, self.height - self.target_size)
            self.targets.append(pygame.Rect(x, y, self.target_size, self.target_size))
    
    def game_loop(self):
        """Main game loop"""
        while True:
            self.start_game()  # Start the game each time the user restarts
            
    def start_game(self):
        collected_targets = 0
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()  # Get the start time
        game_over = False  # Flag to track if the game is over (either win or time's up)
        
        while True:
            elapsed_time = pygame.time.get_ticks() - start_time  # Calculate elapsed time
            remaining_time = max(0, self.time_limit - elapsed_time)  # Remaining time (cannot be negative)

            # Calculate the remaining seconds to display in the timer
            remaining_seconds = remaining_time // 1000  # Convert milliseconds to seconds

            # Check if time is up (after 10 seconds) and the game hasn't been won yet
            if remaining_time == 0 and not game_over:
                if collected_targets < self.num_targets:
                    game_over_text = self.font.render("Time's up!", True, (255, 0, 0))
                    self.screen.blit(game_over_text, (self.width // 2 - game_over_text.get_width() // 2, self.height // 2 - game_over_text.get_height() // 2))
                    pygame.display.flip()
                    pygame.time.wait(2000)  # Wait before restarting
                    self.ask_restart()
                    return

            self.screen.blit(self.background_image, (0, 0))

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

            # Draw player and remaining targets
            pygame.draw.rect(self.screen, self.RED, self.player)
            for target in self.targets:
                pygame.draw.rect(self.screen, self.BLUE, target)

            # Check for win condition
            if collected_targets == self.num_targets:
                win_text = self.font.render("You Win!", True, (0, 255, 0))
                self.screen.blit(win_text, (self.width // 2 - win_text.get_width() // 2, self.height // 2 - win_text.get_height() // 2))
                game_over = True  # Set the game_over flag to True
                pygame.display.flip()
                pygame.time.wait(2000)  # Show the win message for 2 seconds
                self.screen.blit(self.background_image, (0, 0))
                pygame.draw.rect(self.screen, (255, 0, 0), self.clickable_TV, 3)
                pygame.draw.rect(self.screen, (255, 0, 0), self.clickable_plate, 3)
                pygame.draw.rect(self.screen, (255, 0, 0), self.clickable_book, 3)
                pygame.display.flip()

            # Draw the countdown timer in the top-left corner
            timer_text = self.timer_font.render(f"Time: {remaining_seconds}s", True, (255, 255, 255))
            self.screen.blit(timer_text, (10, 10))  # Position it at (10, 10)

            pygame.display.flip()
            clock.tick(60)

    def ask_restart(self):
        """Ask the player if they want to restart the game"""
        restart_text = self.font.render("Press 'R' to Restart", True, (255, 255, 255))
        self.screen.blit(restart_text, (self.width // 2 - restart_text.get_width() // 2, self.height // 2 + 50))
        pygame.display.flip()
        
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()  # Reset the game state
                        waiting_for_input = False  # Exit the loop to start a new game