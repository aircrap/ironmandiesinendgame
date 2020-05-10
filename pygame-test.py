import pygame

def clamp (val, low, high):
    return max (low, min (val, high))

# Stores x and y position of the player
# get_rect and get_point are for easy data use
class Player:
    x = 0.0
    y = 0.0

    def get_rect (self):
        return (int (self.x), int (self.y), 200, 200)

    def get_point (self):
        return (int (self.x), int (self.y))


# Simple Controls handler using boolean states
class Controller:
    holds = {
    pygame.K_w : False,
    pygame.K_s : False,
    pygame.K_d : False,
    pygame.K_a : False,
    }

    def __init__ (self, player):
        self.player = player

    def check_events (self, key, eventUp):
        self.holds [key] = eventUp == pygame.KEYDOWN

    def get_hold (self, key) -> bool:
        return self.holds [key]

    def get_direction_x (self) -> int:
        return self.holds [pygame.K_d] - self.holds [pygame.K_a]

    def get_direction_y (self) -> int:
        return self.holds [pygame.K_s] - self.holds [pygame.K_w]

    def move_player (self, deltaTime):
        self.player.x += gamecon.get_direction_x() * deltaTime
        self.player.y += gamecon.get_direction_y() * deltaTime


# declare a default player
player = Player()

# declare our controller controlling the player
gamecon = Controller (player)

# basic pygame window setup, keep screen variable for rendering
pygame.init()
screen = pygame.display.set_mode([1280, 720])
pygame.display.set_caption ("ubuntu lmao")

#ironman_jpeg = pygame.image.load ("ironman.jpeg")

# clock keeps the framerate at 60FPS while making sure the game runs
# at a constant speed
clock = pygame.time.Clock()
running = True
while running:
    deltaTime = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            gamecon.check_events (event.key, event.type)
        elif event.type == pygame.KEYUP:
            gamecon.check_events (event.key, event.type)

    gamecon.move_player (deltaTime)

    screen.fill ((255, 255, 255))
    pygame.draw.circle (screen, (0, 0, 255), player.get_point(), 75)
    #screen.blit (ironman_jpeg, player.get_rect())

    pygame.display.flip()

pygame.quit()
