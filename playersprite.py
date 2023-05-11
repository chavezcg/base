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
        self.image_index = 0
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.screen = screen
        self.screenwidth = screen.get_width()
        self.screenheight = screen.get_height()
        self.leftFacingList = left_image_list
        self.up_image = up_image_list
        self.left_image = left_image_list
        self.image_position = 0
        self.jump = False #boolean to check if player is jumping
        self.jump_level = 10
        self.map_level = 1
        self.changing_level = False
        self.bg_music = pygame.mixer.music.load('music/bg_music.mp3')
        pygame.mixer.music.play(-1)
        self.max_health = 100
        self.health = 100
        
    def flip_images(self, image_list):
        flipped_images = []
        for image in image_list:
            flipped_image = pygame.transform.flip(image, True, False)
            flipped_images.append(flipped_image)
        return flipped_images

    def gravity(self):
        if self.rect.y < self.screenheight - self.rect.height:
            self.rect.y += 2


    def update(self):
        self.image.set_colorkey((0, 0, 0))
        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT]:

                print(self.image_index)  # print the image index
                self.rect.x -= self.speed  # move the player left
                self.image_index = self.image_index + 1
                if self.image_index > 3:  # if the image is the last image in the list
                    self.image_index = 0  # set the image index to 0
                    # increment the image index
                self.image = self.left_image[self.image_index]

        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
            flipped_images = self.flip_images(self.left_image)
            self.image_index = self.image_index + 1
            if self.image_index > 3:
                self.image_index = 0

            self.image = flipped_images[self.image_index]

        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y + self.speed
            self.image = self.base_image

        #if keys[pygame.K_UP]:
         #   self.rect.y = self.rect.y - self.speed
          #  self.image = self.up_image[0]

        if self.jump == False:
            if keys[pygame.K_SPACE]:
                self.jump = True
        else:
            if self.jump_level >= -10:
                self.rect.y -= (self.jump_level * abs(self.jump_level)) * 0.5
                self.jump_level -= 2
            else:
                self.jump = False
                self.jump_level = 10


        if self.rect.right > self.screenwidth:
            self.rect.right = self.screenwidth

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > self.screenheight:
            self.rect.bottom = self.screenheight

    def gravity(self):
        if self.rect.y < self.screenheight - self.rect.height:  # if the player is not on the ground
            self.rect.y += 3  # add 1 to the y position of the player to simulate gravity

    def check_above_platform(self, object_rect):
        if self.rect.bottom > object_rect.top:  # if the player is below the platform and the player is above the platform rect.bottom has to be greater than the top of the platform to mean that the player is above the platform
            self.rect.bottom = object_rect.top

    def check_below_platform(self, object_rect):
        if object_rect.bottom > self.rect.top > object_rect.top and self.rect.right > object_rect.left and self.rect.left < object_rect.right:
            self.rect.top = object_rect.bottom

    def check_left_of_platform(self, object_rect):
        if self.rect.right > object_rect.left and self.rect.right < object_rect.right and self.rect.bottom > object_rect.top and self.rect.top < object_rect.bottom:
            # if the player jumps on the platform from the left side, move player to top left corner of platform
            # if self.rect.bottom < object_rect.top:
            #     self.rect.bottom = object_rect.top
            # else:
            self.rect.right = object_rect.left

    def check_right_of_platform(self, object_rect):
        if self.rect.left < object_rect.right and self.rect.left > object_rect.left and self.rect.bottom > object_rect.top and self.rect.top < object_rect.bottom:
            self.rect.left = object_rect.right

    def collisiondetection(self, object_group):
        for object in object_group:
            if self.rect.colliderect(object.rect):
                if object.name == "platform" or object.name == "levitating platform" or object.name == "moving platform":
                    self.health = self.health - 20
                    if self.check_above_platform(object.rect):
                        return
                    elif self.check_below_platform(object.rect):
                        return
                    elif self.check_left_of_platform(object.rect):
                        return
                    elif self.check_right_of_platform(object.rect):
                        return

                elif object.name == "coin":
                    object_group.remove(object)
                elif object.name == "door":
                    # if player is inside the door, move to next level
                    if self.rect.x > object.rect.x and self.rect.x < object.rect.x + object.rect.width and self.rect.y > object.rect.y and self.rect.y < object.rect.y + object.rect.height:
                        self.map_level += 1
                        self.changing_level = True