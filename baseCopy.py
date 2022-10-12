import pygame

# screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# game class
class Game:
    def __init__(self):
        pygame.init() # initialize pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # create screen
        self.clock = pygame.time.Clock() # create clock
        self.running = True # game loop
        self.font = pygame.font.SysFont('comic sans', 16) # create font

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()

            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get(): # event loop
            if event.type == pygame.QUIT: # if user clicks X button
                self.running = False

    def update(self):
        self.screen.fill(RED)
        pygame.display.flip()

    def draw(self):
        self.screen.fill(BLACK) # fill screen with black
        pygame.display.flip() # update a portion of the screen

    def quit(self):
        pygame.quit()


# main
if __name__ == '__main__':
    game = Game()
    game.run()
    game.quit()