import pygame
import spritesheet


# create a class for the player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, screen, image, leftimages, upimages):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))


        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.screen = screen
        self.screenwidth = screen.get_width()
        self.screenheight = screen.get_height()
        self.leftFacingList = leftimages
        self.upFacingImages = upimages


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.speed
            self.image = self.leftFacingList[0]

        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed

        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y + self.speed

        if keys[pygame.K_UP]:
            self.rect.y = self.rect.y - self.speed

        if self.rect.right > self.screenwidth:
            self.rect.right = self.screenwidth

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > self.screenheight:
            self.rect.bottom = self.screenheight


