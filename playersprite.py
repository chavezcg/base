import pygame
import spritesheet


# create a class for the player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, screen, image, left_image_list, up_image_list):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.base_image = image
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))



        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.screen = screen
        self.screenwidth = screen.get_width()
        self.screenheight = screen.get_height()
        self.leftFacingList = left_images_list
        self.right_images = up_images_list
        self.left_images = up_images_list

    def flip_images(self, image_list):
        flipped_images = []
        for image in image_list:
            flipped_images = pygame.transform.flip(image, True, False)
            flipped_images.append(flipped_images)
        return flipped_images


    def update(self):
        self.image.set_colorkey((0, 0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.speed
            self.image = self.leftFacingList[0]

        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed

        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y + self.speed
            self.image = self.base_image

        if keys[pygame.K_UP]:
            self.rect.y = self.rect.y - self.speed
            self.image = self.up_images[0]

        if self.rect.right > self.screenwidth:
            self.rect.right = self.screenwidth

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > self.screenheight:
            self.rect.bottom = self.screenheight


