import arcade

class Wall(arcade.Sprite):
    @classmethod
    def load_textures(cls, scale=1):
        cls.scale = scale
        cls.textures = [
            [
                arcade.load_texture("assets/wall_zero.png", scale=scale)
            ], [
                arcade.load_texture("assets/wall_one.png", scale=scale)
            ], [
                arcade.load_texture("assets/wall_two.png", scale=scale),
                arcade.load_texture("assets/wall_two_0.png", scale=scale),
                arcade.load_texture("assets/wall_two_1.png", scale=scale)
            ], [
                arcade.load_texture("assets/wall_three_00.png", scale=scale),
                arcade.load_texture("assets/wall_three_01.png", scale=scale),
                arcade.load_texture("assets/wall_three_10.png", scale=scale),
                arcade.load_texture("assets/wall_three_11.png", scale=scale)
            ], [
                arcade.load_texture("assets/wall_four_0000.png", scale=scale),
                arcade.load_texture("assets/wall_four_1000.png", scale=scale),
                arcade.load_texture("assets/wall_four_1010.png", scale=scale),
                arcade.load_texture("assets/wall_four_1100.png", scale=scale),
                arcade.load_texture("assets/wall_four_1110.png", scale=scale),
                arcade.load_texture("assets/wall_four_1111.png", scale=scale)
            ]
        ]
    edged = False
    def __init__(self, walls, x, y):
        super().__init__()
        self.center_x = Wall.textures[0][0].width * (x + 0.5)
        self.center_y = Wall.textures[0][0].height * (y + 0.5)

        self.up = walls[y - 1][x] if y > 0 else Wall.edged
        self.ri = walls[y][x + 1] if x < len(walls) - 1 else Wall.edged
        self.do = walls[y + 1][x] if y < len(walls) - 1 else Wall.edged
        self.le = walls[y][x - 1] if x > 0 else Wall.edged
        self.uple = walls[y - 1][x - 1] if y > 0 and x > 0 else Wall.edged
        self.upri = walls[y - 1][x + 1] if y > 0 and x < len(walls) - 1 else Wall.edged
        self.dole = walls[y + 1][x - 1] if y < len(walls) - 1 and x > 0 else Wall.edged
        self.dori = walls[y + 1][x + 1] if y < len(walls) - 1 and x < len(walls) - 1 else Wall.edged

        neighbours = [self.ri, self.do, self.le, self.up]
        corners = [self.dori, self.dole, self.uple, self.upri]
        sum_neighbours = sum(neighbours)
        sum_corners = sum(corners)
        
        subtexture = 0

        if sum_neighbours == 1:
            self.angle = neighbours.index(True) * 90
        if sum_neighbours == 2:
            if sum([self.up, self.do]) % 2 == 1:
                subtexture = 1
                self.angle = (neighbours.index(True) if neighbours[neighbours.index(True) + 1] else neighbours.index(True, neighbours.index(True) + 1)) * 90
            else:
                self.angle = neighbours.index(True) * 90
        if sum_neighbours == 3:
            self.angle = neighbours.index(False) * 90
        
        self.texture = Wall.textures[sum_neighbours][subtexture]

