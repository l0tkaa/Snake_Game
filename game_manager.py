import pygame

class GameManager:
    def __init__(self, game):
        self.game = game

    
    def handle_events(self):
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
                elif event.key == pygame.K_q: #press q to quit
                    self.running = False
                elif event.key == pygame.K_w:
                    self.fps = min(self.fps + 1, 30)
                elif event.key == pygame.K_s: 
                    self.fps = max(self.fps - 1, 5)
                elif event.key == pygame.K_r: 
                    self.fps = FPS
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                    print(f"Paused: {self.paused}") #debugging 

                    

    def update(self):
        self.snake.move()

        if tuple(self.snake.body[0]) == tuple(self.food.position):
            self.food.position = self.food.spawn_food()

            base_points = 10
            self.score +=max(1, int(base_points * (self.fps / FPS)))

            print(f"🍎 Food eaten! New score: {self.score}")

        else:
            self.snake.body.pop() #remove tail to keep same size
        
        if self.snake.check_collision(): #check for collisions
            self.running = False   

    
    def draw(self):
        self.screen.fill(BLACK)

        # draw snake and food
        self.snake.draw(self.screen, GREEN)
        self.food.draw(self.screen)

        # draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10,10))

        #display PAUSED message
        if self.paused:
            paused_text = self.font.render("PAUSED", True, RED)
            text_rect = paused_text.get_rect(center = (WIDTH //2, HEIGHT // 2))
            self. screen.blit(paused_text, text_rect)


        pygame.display.flip()
