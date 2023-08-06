import arcade
from random import randint, choice

RIGHT = 1
UP = 2
LEFT = 3
DOWN = 4

class Ghost(arcade.AnimatedWalkingSprite):
    def __init__(self, scale, dimension, colour="red"):
        super().__init__(scale=scale)
        self.scale = scale

        offset = 0
        if colour == "orange":
            offset = 64
        elif colour == "pink":
            offset = 128
        elif colour == "cyan":
            offset = 192

        # all_textures = arcade.load_textures("assets/sheets/actors.png", ((0 + offset, 0, 32, 32), (32 + offset, 0, 32, 32), (0 + offset, 32, 32, 32), (32 + offset, 32, 32, 32),(0 + offset, 64, 32, 32), (32 + offset, 64, 32, 32),(0 + offset, 96, 32, 32), (32 + offset, 96, 32, 32)))

        all_textures = []
        texture = "assets/sheets/actors.png"
        coordinates = ((0 + offset, 0, 32, 32), (32 + offset, 0, 32, 32), (0 + offset, 32, 32, 32), (32 + offset, 32, 32, 32),(0 + offset, 64, 32, 32), (32 + offset, 64, 32, 32), (0 + offset, 96, 32, 32), (32 + offset, 96, 32, 32))
        for coord in coordinates:
            all_textures.append(arcade.load_texture(texture, coord[0], coord[1], coord[2], coord[3]))


        self.walk_right_textures = [all_textures[0], all_textures[1]]
        self.walk_down_textures = [all_textures[2], all_textures[3]]
        self.walk_left_textures = [all_textures[4], all_textures[5]]
        self.walk_up_textures = [all_textures[6], all_textures[7]]
        self.stand_left_textures = [all_textures[4]]
        self.stand_right_textures = [all_textures[0]]

        if colour == "red":
            self.center_x = 32 * scale * 1.5
            self.center_y = 32 * scale * 1.5
        elif colour == "orange":
            self.center_x = 32 * scale * (dimension - 1.5)
            self.center_y = 32 * scale * 1.5
        elif colour == "pink":
            self.center_x = 32 * scale * 1.5
            self.center_y = 32 * scale * (dimension - 1.5)
        elif colour == "cyan":
            self.center_x = 32 * scale * (dimension - 1.5)
            self.center_y = 32 * scale * (dimension - 1.5)
        
        self.speed = 4

        self.direction = None

        self.vulnerable = False
        self.vulnerable_textures = [
            arcade.load_texture("assets/sheets/actors.png", 384, 0, 32, 32),
            arcade.load_texture("assets/sheets/actors.png", 416, 0, 32, 32),
            arcade.load_texture("assets/sheets/actors.png", 384, 32, 32, 32),
            arcade.load_texture("assets/sheets/actors.png", 416, 32, 32, 32),
        ]
    
    def update(self, width, height, walls, wall_booleans):
        # print(self.direction)

        if self.left >= width:
            self.right = 0
        elif self.right <= 0:
            self.left = width

        if self.bottom >= height:
            self.top = 0
        elif self.top <= 0:
            self.bottom = height
        
        if self.top % (32 * self.scale) == 0 and self.left % (32 * self.scale) == 0 or self.direction == None:
            # print("In a square")
            
            # print(self.center_x)
            # print(self.left)
            x = int(self.center_x // (32 * self.scale))
            y = int(self.center_y // (32 * self.scale))
            # print(x)
            # print(y)

            # print(wall_booleans)
            # neighbours = [
            #     wall_booleans[y][x + 1] if x < len(wall_booleans) - 1 else False,
            #     wall_booleans[y - 1][x] if y > 0 and x < len(wall_booleans) else False,
            #     wall_booleans[y][x - 1] if x > 0 else False,
            #     wall_booleans[y + 1][x] if y < len(wall_booleans) - 1 and x < len(wall_booleans) else False
            # ]
            # neighbours_sum = sum(neighbours)

            # print(neighbours)
            # print("{} {}".format(x, y))

            size = len(wall_booleans)
            neighbours = [
                RIGHT if x < size - 1 and y < size and not wall_booleans[y][x + 1] else False,
                UP if y > 0 and x < size and not wall_booleans[y - 1][x] else False,
                LEFT if x > 0 and y < size and not wall_booleans[y][x - 1] else False,
                DOWN if y < size - 1 and x < size and not wall_booleans[y + 1][x] else False
            ]
            #neighbours_sum = sum(neighbours)
            # print(neighbours)
            empties = [x for x in neighbours if x != False]
            # print(empties)
            # print(empties.count(self.direction))

            if len(empties) > 2 or len(empties) == 2 and not empties.count(self.direction) == 1:
                # print("Picking random")
                random = choice(empties)
                # print(random)
                self.direction = random

            # empties = []
            # for neighbour in neighbours:
            #     if 

            # empties = [x for y in [RIGHT, UP, LEFT, DOWN] if neighbours.index(y) else False]


            # if neighbours_sum >= 2:
            #     random = randint(0, 3)
            #     print("Picked " + str(random))
            #     if random == 0:
            #         self.change_x = 0
            #         self.change_y = self.speed
            #     elif random == 1:
            #         self.change_x = self.speed
            #         self.change_y = 0
            #     elif random == 2:
            #         self.change_x = 0
            #         self.change_y = -self.speed
            #     else:
            #         self.change_x = -self.speed
            #         self.change_y = 0
        
        if arcade.check_for_collision_with_list(self, walls):
            self.direction = None
        
        
        if self.direction == RIGHT:
            self.center_x += self.speed
        elif self.direction == LEFT:
            self.center_x -= self.speed
        elif self.direction == UP:
            self.center_y -= self.speed
        elif self.direction == DOWN:
            self.center_y += self.speed


    def make_vulnerable(self):
        self.vulnerable = True
        self.walk_down_textures = self.vulnerable_textures
        self.walk_left_textures = self.vulnerable_textures
        self.walk_right_textures = self.vulnerable_textures
        self.walk_up_textures = self.vulnerable_textures
        self.stand_left_textures = self.vulnerable_textures
        self.stand_right_textures = self.vulnerable_textures
        