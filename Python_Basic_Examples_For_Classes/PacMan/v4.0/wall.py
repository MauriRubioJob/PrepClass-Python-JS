import arcade

class Wall(arcade.Sprite):
    textures = None

    @classmethod
    def load_textures(cls, scale):
        # This is a horrible non-solution to scaling
        sheet = "assets/walls_complete.png" if scale == 1 else "assets/walls_complete_2x.png"
        coordinates = [[x * 32 * scale, y * 32 * scale, 32 * scale, 32 * scale] for y in range(4) for x in range(4)]
        cls.textures = arcade.load_textures(sheet, coordinates)
        cls.hashed_textures = {
            "[False, False, False, False]": cls.textures[0],
            "[False, False, False, True]": cls.textures[1],
            "[False, False, True, False]": cls.textures[2],
            "[False, True, False, False]": cls.textures[3],
            "[True, False, False, False]": cls.textures[4],
            "[False, False, True, True]": cls.textures[5],
            "[False, True, False, True]": cls.textures[6],
            "[True, False, False, True]": cls.textures[7],
            "[False, True, True, False]": cls.textures[8],
            "[True, False, True, False]": cls.textures[9],
            "[True, True, False, False]": cls.textures[10],
            "[False, True, True, True]": cls.textures[11],
            "[True, False, True, True]": cls.textures[12],
            "[True, True, False, True]": cls.textures[13],
            "[True, True, True, False]": cls.textures[14],
            "[True, True, True, True]": cls.textures[15],
        }
        cls.edged = False



    def __init__(self, grid, x, y, scale=1):
        super().__init__()

        if not Wall.textures:
            Wall.load_textures(scale)

        grid_height = len(grid)
        grid_width = len(grid[0])

        neighbours = list(map(lambda x: x == 1, [
            grid[y + 1][x] if y < grid_height - 1 else Wall.edged,
            grid[y][x + 1] if x < grid_width - 1 else Wall.edged,
            grid[y - 1][x] if y > 0 else Wall.edged,
            grid[y][x - 1] if x > 0 else Wall.edged
        ]))

        self.texture = Wall.hashed_textures[str(neighbours)]
        self.center_x = round(self.texture.width * (x + 0.5))
        self.center_y = round(self.texture.height * (y + 0.5))
