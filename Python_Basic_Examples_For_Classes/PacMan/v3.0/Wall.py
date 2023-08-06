import arcade

class Wall(arcade.Sprite):
    @classmethod
    def load_textures(cls, scale=1):
        cls.scale = scale 
        cls.textures = arcade.load_textures(
            "assets/sheets/walls_simple.png",
            [[x * 32, 0, 32, 32] for x in range(6)]
        )
    edged = False
    
    def __init__(self, walls, x, y):
        super().__init__(scale=Wall.scale)
        self.textures = Wall.textures
        self.center_x = Wall.textures[0].width * (x + 0.5) * Wall.scale
        self.center_y = Wall.textures[0].height * (y + 0.5) * Wall.scale

        self.up = walls[y - 1][x] if y > 0 else Wall.edged
        self.ri = walls[y][x + 1] if x < len(walls) - 1 else Wall.edged
        self.do = walls[y + 1][x] if y < len(walls) - 1 else Wall.edged
        self.le = walls[y][x - 1] if x > 0 else Wall.edged

        neighbours = [self.ri, self.do, self.le, self.up]
        neighbours_sum = sum(neighbours)
        subtexture = 0
        if neighbours_sum == 1:
            self.angle = neighbours.index(True) * 90
        if neighbours_sum == 2:
            if sum([self.up, self.do]) % 2 == 1:
                subtexture = 1
                # self.angle = (neighbours.index(True) if neighbours[neighbours.index(True) + 1] else neighbours.index(True, neighbours.index(True) + 1)) * 90
                self.angle = (neighbours.index(True)) * 90
            else:
                self.angle = neighbours.index(True) * 90
        if neighbours_sum == 3:
            self.angle = neighbours.index(False) * 90
        
        self.set_texture(neighbours_sum + subtexture)