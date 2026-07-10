import pygame
import math

font_small = pygame.font.SysFont("Arial", 28)

class SafeDisk:
    def __init__(self, cx, cy, r):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.current_angle = 0
        self.target_angle = 0
        self.color = (255, 255, 255)

    def set_target_angle(self, angle):
        self.target_angle = angle

    def set_color(self, color):
        self.color = color

    def update(self):
        if abs(self.target_angle - self.current_angle) > 1:
            self.current_angle += 3 if self.target_angle > self.current_angle else -3

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.cx, self.cy), self.r, 5)

        for i in range(10):
            angle = math.radians(i * 36 + self.current_angle)

            x1 = self.cx + (self.r - 25) * math.cos(angle)
            y1 = self.cy + (self.r - 25) * math.sin(angle)
            x2 = self.cx + self.r * math.cos(angle)
            y2 = self.cy + self.r * math.sin(angle)
            pygame.draw.line(screen, self.color, (x1, y1), (x2, y2), 4)

            tx = self.cx + (self.r - 55) * math.cos(angle)
            ty = self.cy + (self.r - 55) * math.sin(angle)
            num = font_small.render(str(i), True, self.color)
            screen.blit(num, (tx - 10, ty - 10))
