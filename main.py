
import pygame

WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_HEIGHT = 80
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialization
pygame.init()

# load image (background, enemy, buttons)
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))
# ...(to be done)


# set the title
pygame.display.set_caption("My first game")
clock = pygame.time.Clock()

class Game:
    def __init__(self):
        # window
        self.image = pygame.Surface((50,40))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()

        # hp
        self.hp = 7
        self.max_hp = 10
        pass

    def game_run(self):
        # game loop
        run = True
        while run:
            # event loop
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                      

            # draw background
            # ...(to be done)

            # draw enemy and health bar
            # ...(to be done)

            # draw menu (and buttons)
            # (... to be done)


            # draw time
            # ...(to be done)

    pygame.display.update()

if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()

pygame.quit()


