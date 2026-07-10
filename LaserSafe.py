import pygame
from CodeInput import CodeInput
from SafeDisk import SafeDisk
from SafeLogic import SafeLogic

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Лазерный Сейф — Pygame")

clock = pygame.time.Clock()

# модули
code_input = CodeInput()
safe_disk = SafeDisk(550, 250, 150)
safe_logic = SafeLogic()

running = True
while running:
    screen.fill((25, 25, 25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        code_input.handle_event(event, safe_disk)

        if code_input.check_pressed(event):
            safe_disk.set_color(safe_logic.check(code_input.digits))

    safe_disk.update()
    safe_disk.draw(screen)
    code_input.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
