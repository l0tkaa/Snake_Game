import pygame
from snake import Snake
from food import Food
from score_manager import ScoreManager
from name_entry import NameEntry
from settings import WIDTH, HEIGHT, FPS, WHITE, GREEN, RED, BLACK

class GameManager:
    def __init__(self, screen, clock, default_fps):
        """Initialize GameManager and store all game components."""
        self.screen = screen
        self.clock = clock
        self.default_fps = default_fps

        # ✅ Owns game elements
        self.snake = Snake()
        self.food = Food()
        self.running = True
        self.paused = False
        self.fps = self.default_fps
        self.score = 0
        self.score_manager = ScoreManager()
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 24)

    def run_game_loop(self):
        """Main game loop."""

        self.show_start_screen()

        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        
        self.show_death_screen()

        # ✅ Handle game over and name entry
        self.get_player_name()
        self.display_high_scores_screen()
       
        #wait for user input before closing
        self.wait_for_exit()

    def handle_events(self):
        """Handles user input (key presses, quitting, pausing, etc.)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != "DOWN":
                    self.snake.direction = "UP"
                elif event.key == pygame.K_DOWN and self.snake.direction != "UP":
                    self.snake.direction = "DOWN"
                elif event.key == pygame.K_LEFT and self.snake.direction != "RIGHT":
                    self.snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and self.snake.direction != "LEFT":
                    self.snake.direction = "RIGHT"
                elif event.key == pygame.K_q:
                    self.running = False
                elif event.key == pygame.K_w:
                    self.fps = min(self.fps + 1, 30)
                elif event.key == pygame.K_s:
                    self.fps = max(self.fps - 1, 5)
                elif event.key == pygame.K_r:
                    self.fps = self.default_fps
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_k:
                    print("Instant death triggered!")
                    self.running = False

    def update(self):
        """Handles game logic updates (movement, collision, scoring)."""
        if self.paused:
            return  # Skip updates if paused

        self.snake.move()

        # Check if snake eats food
        if tuple(self.snake.body[0]) == tuple(self.food.position):
            self.food.position = self.food.spawn_food()
            self.score += max(1, int(10 * (self.fps / self.default_fps)))

        else:
            self.snake.body.pop()

        # Check for self-collision
        if self.snake.check_collision():
            self.running = False  # End the game

    def draw(self):
        """Handles drawing all game elements."""
        self.screen.fill(BLACK)
        self.snake.draw(self.screen, GREEN)
        self.food.draw(self.screen)

        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        # Display PAUSED message
        if self.paused:
            paused_text = self.font.render("PAUSED", True, RED)
            text_rect = paused_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self.screen.blit(paused_text, text_rect)

        pygame.display.flip()

    def get_player_name(self):
        """Ask for the player's name and save their score."""
        name_entry = NameEntry(self.screen, self.font)
        player_name = name_entry.get_name()
        self.score_manager.add_score(player_name, self.score)
    
    def display_high_scores_screen(self):
        self.screen.fill((0,0,0))
        title_text = self.font.render("HIGH SCORES", True, (255,255,255))
        self.screen.blit(title_text, (WIDTH//4, 50))

        self.score_manager.high_scores = self.score_manager.load_high_scores()

        #get top scores
        scores = self.score_manager.high_scores[:5]
        for i, (name, score) in enumerate(scores):
            score_text = self.font.render(f"{i+1}. {name} - {score}", True, (0,255,0))
            self.screen.blit(score_text, (WIDTH //4, 100 + i * 40))
        
        pygame.display.flip()
    
    def restart_game(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.fps = self.default_fps
        self.running = True

        self.run_game_loop()


    def wait_for_exit(self):
        waiting = True
        while waiting: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    elif event.key == pygame.K_r:
                        self.restart_game()
                        waiting = False
    
    def show_start_screen(self):
        """Display a start screen with instructions before starting the game."""
        self.screen.fill((0, 0, 0))  # Clear screen

        # Title
        title_text = self.font.render("SNAKE GAME", True, (0, 255, 0))
        title_rect = title_text.get_rect(center=(WIDTH // 2, 50))
        self.screen.blit(title_text, title_rect)

        # Instructions (centered)
        instructions = [
            "Press S key to start",
            "CONTROLS:",
            "Move Up    - Arrow Up",
            "Move Down  - Arrow Down",
            "Move Left  - Arrow Left",
            "Move Right - Arrow Right",
            "Speed Up   - W",
            "Slow Down  - S",
            "Pause      - SPACE",
            "Quit       - Q, ESC",
            "Restart    - R (after death)"
        ]

        line_spacing = 25

        # Display instructions dynamically
        for i, line in enumerate(instructions):
            text = self.font.render(line, True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH // 2, 120 + i * line_spacing))  # ✅ Center text
            self.screen.blit(text, text_rect)

        pygame.display.flip()  # Refresh screen

        # Wait for key press to start
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        waiting = False  # Start game when a key is pressed

    def show_death_screen(self):
        self.screen.fill((0,0,0)) #clear screen

        death_image = pygame.image.load("assets/images/you_died.png")

        death_image = pygame.transform.scale(death_image, (600,600))

        image_rect = death_image.get_rect(center = (WIDTH //2, HEIGHT // 2))

        self.screen.blit(death_image, image_rect)

        pygame.display.flip()

        pygame.time.delay(2000)

