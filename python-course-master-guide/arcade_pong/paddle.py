from arcade import Sprite


class Paddle(Sprite):
    def __init__(self, image, height):
        super().__init__(image)
        self.width = 20
        self.height = 100
        self.speed = 10
    

    def update(self, height):
        # Move the paddle
        # self.center_y = self.center_y + self.speed
        self.center_y += self.speed

        # Constrain the position to the screen
        if self.bottom < 0:
            self.bottom = 0
        if self.top > height:
            self.top = height


class Player(Paddle):
    def __init__(self):
        super().__init__("images/1x1orange.png", 100)
        self.center_x = 0
        self.speed = 0
    
    def move_up(self):
        self.speed = 10
    
    def move_down(self):
        self.speed = -10
    
    def stop(self):
        self.speed = 0



class Enemy(Paddle):
    def __init__(self, width):
        super().__init__("images/1x1magenta.png", 100)
        self.center_x = width
        self.speed = 0

    def update(self, ball, height):
        # Run the update function in the Paddle class
        super().update(height)

        # Move the Enemy
        if self.center_y < ball.center_y:
            self.speed = 10
        elif self.center_y > ball.center_y:
            self.speed = -10