

class NameEntry:
    def __init__():



def enter_name(self):
        """Ask the player for a name after the game is over."""
        name = ""
        font = pygame.font.SysFont("Arial", 32)
        input_active = True

        while input_active:
            self.screen.fill(BLACK)
            prompt_text = font.render("Enter your name (or press Enter for Guest):", True, WHITE)
            name_text = font.render(name or "Guest", True, GREEN)
            self.screen.blit(prompt_text, (WIDTH // 6, HEIGHT // 3))
            self.screen.blit(name_text, (WIDTH// 2 - 50, HEIGHT//2))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1] #delete last character
                    else:
                        name += event.unicode #add typed character

        name = name.strip() if name.strip() else "Guest"