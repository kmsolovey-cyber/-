import pygame

font_big = pygame.font.SysFont("Arial", 36)
font_small = pygame.font.SysFont("Arial", 28)

class CodeInput:
    def __init__(self):
        self.digits = [0, 0, 0]
        self.buttons = [pygame.Rect(50 + i * 120, 80, 100, 100) for i in range(3)]
        self.check_button = pygame.Rect(50, 250, 360, 70)

    def handle_event(self, event, safe_disk):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos

            for i, rect in enumerate(self.buttons):
                if rect.collidepoint(mx, my):
                    self.digits[i] = (self.digits[i] + 1) % 10
                    safe_disk.set_target_angle(self.digits[0] * 36)

    def check_pressed(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.check_button.collidepoint(event.pos):
                return True
        return False

    def draw(self, screen):
        for i, rect in enumerate(self.buttons):
            pygame.draw.rect(screen, (70, 70, 70), rect, border_radius=10)
            num = font_big.render(str(self.digits[i]), True, (255, 255, 255))
            screen.blit(num, (rect.x + 35, rect.y + 30))

        pygame.draw.rect(screen, (0, 120, 200), self.check_button, border_radius=10)
        screen.blit(font_big.render("Проверить код", True, (255, 255, 255)),
                    (self.check_button.x + 50, self.check_button.y + 15))
