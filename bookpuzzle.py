import pygame
import random
import sys


class MiniPuzzleGame:
    def __init__(self, width=800, height=600, player_size=50, target_size=30, player_speed=7.3, num_targets=11, time_limit=10000):
        pygame.init()
        self.width = width
        self.height = height
        self.player_size = player_size
        self.target_size = target_size
        self.player_speed = player_speed
        self.num_targets = num_targets
        self.time_limit = time_limit
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bookpuzzle Game")
        self.font = pygame.font.Font(None, 74)
        self.timer_font = pygame.font.Font(None, 54)
        self.background_image = pygame.image.load('openbook.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        # Initialize player and targets
        self.player = pygame.Rect(self.width // 2, self.height // 2, self.player_size, self.player_size)
        self.targets = []
        for _ in range(self.num_targets):
            x = random.randint(0, self.width - self.target_size)
            y = random.randint(0, self.height - self.target_size)
            self.targets.append(pygame.Rect(x, y, self.target_size, self.target_size))

        self.game_won = False  # Add a flag to track the game state

    def reset_game(self):
        self.player.x = self.width // 2
        self.player.y = self.height // 2
        self.targets = []
        for _ in range(self.num_targets):
            x = random.randint(0, self.width - self.target_size)
            y = random.randint(0, self.height - self.target_size)
            self.targets.append(pygame.Rect(x, y, self.target_size, self.target_size))
        self.game_won = False  # Reset game won flag

    def game_loop(self, restart_game, return_to_main):
        collected_targets = 0
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()
        game_over = False
        while True:
            elapsed_time = pygame.time.get_ticks() - start_time
            remaining_time = max(0, self.time_limit - elapsed_time)
            remaining_seconds = remaining_time // 1000

            if remaining_time == 0 and collected_targets < self.num_targets:
                # The player loses if time runs out
                game_over_text = self.font.render("Time's up!", True, (255, 0, 0))
                self.screen.blit(game_over_text, (self.width // 2 - game_over_text.get_width() // 2, self.height // 2 - game_over_text.get_height() // 2))
                pygame.display.flip()
                pygame.time.wait(2000)
                restart_prompt = self.font.render("Press 'R' to restart", True, (255, 255, 255))
                self.screen.blit(restart_prompt, (self.width // 2 - restart_prompt.get_width() // 2, self.height // 2 + 50))
                pygame.display.flip()

                waiting_for_input = True
                while waiting_for_input:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                restart_game()  # Restart the puzzle
                                waiting_for_input = False
                return

            self.screen.blit(self.background_image, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.x -= self.player_speed
            if keys[pygame.K_RIGHT]:
                self.player.x += self.player_speed
            if keys[pygame.K_UP]:
                self.player.y -= self.player_speed
            if keys[pygame.K_DOWN]:
                self.player.y += self.player_speed

            for target in self.targets[:]:
                if self.player.colliderect(target):
                    self.targets.remove(target)
                    collected_targets += 1

            # After the player collects all targets
            if collected_targets == self.num_targets:
                # The player wins
                self.game_won = True  # Set the game_won flag to True
                win_text = self.font.render("You Win!", True, (0, 255, 0))
                self.screen.blit(win_text, (self.width // 2 - win_text.get_width() // 2, self.height // 2 - win_text.get_height() // 2))
                pygame.display.flip()
                pygame.time.wait(2000)
                return_to_main()  # Go back to the main screen after winning
                return

            # Only draw the player and targets if the game is not won
            if not self.game_won:
                pygame.draw.rect(self.screen, (255, 0, 0), self.player)
                for target in self.targets:
                    pygame.draw.rect(self.screen, (0, 0, 255), target)

            # Timer display
            timer_text = self.timer_font.render(f"Time: {remaining_seconds}s", True, (255, 255, 255))
            self.screen.blit(timer_text, (10, 10))

            pygame.display.flip()
            clock.tick(60)
