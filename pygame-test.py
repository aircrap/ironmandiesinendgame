import pygame

# Simple Controls handler using boolean states
class Controller:
    holds = {
    pygame.K_w : False,
    pygame.K_s : False,
    pygame.K_d : False,
    pygame.K_a : False,
    }

    def check_events (self, key, eventUp):
        self.holds [key] = eventUp == pygame.KEYDOWN

    def get_hold (self, key):
        return self.holds [key]

    def get_direction_x (self):
        return self.holds [pygame.K_d] - self.holds [pygame.K_a]

    def get_direction_y (self):
        return self.holds [pygame.K_s] - self.holds [pygame.K_w]

# declare our controller
gamecon = Controller()

# basic pygame window setup, keep screen variable for rendering
pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption ("ubuntu lmao")

x = 0
y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            gamecon.check_events (event.key, event.type)

    x += gamecon.get_direction_x()
    y += gamecon.get_direction_y()

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 75)
    pygame.display.flip()

pygame.quit()
