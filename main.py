import pygame
import spritesheet
import playersprite as ps
import objectsprite as os

# screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900
#hello
# loading images into pygame






# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# create a class for the player


# game class
class Game:
    i = 0

    def __init__(self):
        pygame.init()  # initialize pygame
        self.platform_name
        self.bg_music = pygame.mixer.music.load('music/bg_music.mp3')
        pygame.mixer.music.play(-1)
        self.bg_img = pygame.image.load('pictures/spacebg.jpg')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # create screen
        self.clock = pygame.time.Clock()  # create clock
        self.running = True  # game loop
        self.font = pygame.font.SysFont('comic sans', 16)  # create font
        self.i = 0
        player_spritesheet = spritesheet.SpriteSheet('pictures/Morty.jpg')
        # morty
        self.player_base_image = player_spritesheet.image_at((27, 703, 79, 113))
        self.left_facing_image1 = player_spritesheet.image_at((395, 876, 95, 109))
        self.left_facing_image2 = player_spritesheet.image_at((284, 856, 77, 108))
        self.left_facing_image3 = player_spritesheet.image_at((155, 856, 77, 109))
        self.left_facing_image4 = player_spritesheet.image_at((27, 855, 77, 110))
        self.player_base_image.convert_alpha()

        self.leftFacingList = [self.left_facing_image1, self.left_facing_image2, self.left_facing_image3, self.left_facing_image4]

        self.up_images = []
        self.player_right_image1 = player_spritesheet.image_at((28, 1042, 78, 109))
        self.player_right_image2 = player_spritesheet.image_at((157, 1042, 78, 108))
        self.player_right_image3 = player_spritesheet.image_at((286, 1042, 78, 109))
        self.player_right_image4 = player_spritesheet.image_at((415, 1042, 78, 109))
        self.up_images = [self.player_right_image1, self.player_right_image2, self.player_right_image3,
                          self.player_right_image4, self.up_images]

        self.up_facing_image1 = player_spritesheet.image_at((416, 1019, 78, 111))
        self.up_facing_image2 = player_spritesheet.image_at((287, 1021, 78, 109))
        self.up_facing_image3 = player_spritesheet.image_at((158, 1019, 78, 114))
        self.up_facing_image4 = player_spritesheet.image_at((29, 1021, 78, 109))

        self.upFacingList = [self.up_facing_image1, self.up_facing_image2,self.up_facing_image3, self.up_facing_image4]



        #create player
        self.player_group = pygame.sprite.Group()
        self.player = ps.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 79, 113, self.screen, self.player_base_image, self.leftFacingList, self.upFacingList)
        self.object_group = pygame.sprite.Group()
        self.platform = os.ObjectSprite(self.player_base_image, 200, SCREEN_HEIGHT - 20, "platform")
        self.platform2 = os.ObjectSprite(self.player_base_image, 300, SCREEN_HEIGHT - 40, "platform")
        self.platform3 = os.ObjectSprite(self.player_base_image, 400, SCREEN_HEIGHT - 60, "platform")
        self.platform4 = os.ObjectSprite(self.player_base_image, 500, SCREEN_HEIGHT - 80, "platform")
        self.platform5 = os.ObjectSprite(self.player_base_image, 600, SCREEN_HEIGHT - 100, "platform")
        self.platform6 = os.ObjectSprite(self.player_base_image, 700, SCREEN_HEIGHT - 120, "levitating platform")
        self.platform7 = os.ObjectSprite(self.player_base_image, 600, 300, "platform")
        self.platform8 = os.ObjectSprite(self.player_base_image, 500, 300, "platform")
        self.platform8.image.fill(GREEN)
        self.platform9 = os.ObjectSprite(self.player_base_image, 400, 350, "platform")
        self.platform10 = os.ObjectSprite(self.player_base_image, 300, 400, "platform")
        self.platform11 = os.ObjectSprite(self.player_base_image, 200, 450, "platform")
        self.platform12 = os.ObjectSprite(self.player_base_image, 100, 500, "platform")
        self.platform13 = os.ObjectSprite(self.player_base_image, 0, 450, "levitating platform")
        self.platform14 = os.ObjectSprite(self.player_base_image, 100, 700, "platform")
        self.door = os.ObjectSprite(self.player_base_image, 100, 570, "door")

        self.object_group.add(self.platform)
        self.object_group.add(self.platform2)
        self.object_group.add(self.platform3)
        self.object_group.add(self.platform4)
        self.object_group.add(self.platform5)
        self.object_group.add(self.platform6)
        self.object_group.add(self.platform7)
        self.object_group.add(self.platform8)
        self.object_group.add(self.platform9)
        self.object_group.add(self.platform10)
        self.object_group.add(self.platform11)
        self.object_group.add(self.platform12)
        self.object_group.add(self.platform13)
        self.object_group.add(self.platform14)
        self.object_group.add(self.door)


        #self.player = ps.Player(0, 0, 105, 109, self.screen, self.player1_img)
        #create a group for the player

        self.player_group.add(self.player)

    #def platform_change(self, self.platform_name, color, new_x, new_y):
        #self.platform_name.image.fill(color)
        #self.platform_name.rect.x = new_x
        #self.platform_name.rect.y = new_y


    def change_level(self):
        print("Change Level function is being called")
        if self.player.map_level == 2:
            print("Map level = 2")
            self.player.rect.x = 0
            self.player.rect.y = 900
            self.bg_img = pygame.image.load('pictures/desertbg.jpeg')
            self.bg_img = pygame.transform.scale(self.bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.bg_music = pygame.mixer.music.load("music/bg_musiclvl2.mp3")
            pygame.mixer.music.play(-1)
            self.platform_change(self.platform, BLUE, 300, 400)



    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.player.collisiondetection(self.object_group)
            self.update()
            self.draw()

    # Handles events in the game such as key presses and mouse clicks
    def events(self):
        for event in pygame.event.get():  # event loop
            if event.type == pygame.QUIT:  # if user clicks X button
                self.running = False

    # Updates the game state such as player position and enemy position
    # This is where the game logic goes
    def update(self):
       self.player_group.update()
       self.object_group.update()
       self.player.gravity()
       self.player.collisiondetection(self.object_group)
       if self.player.changing_level == True:
           self.change_level()


    def draw(self):
        # set background to background image and draw it
       #set screen background white
        self.screen.blit(self.bg_img, (0, 0))
        self.player_group.draw(self.screen) #draw player
        self.object_group.draw(self.screen) #draw object
        pygame.display.flip()  # update a portion of the screen

    def quit(self):
        pygame.quit()


# main

if __name__ == '__main__':
    game = Game()
    game.run()
    game.quit()

