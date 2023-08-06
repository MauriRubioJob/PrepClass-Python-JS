from arcade import Sprite
from random import randint


class Ball(Sprite):
    def __init__(self):
        super().__init__("crest.png", center_x=400, center_y=300)
        self.x_speed = 5
        self.y_speed = 4

        self.width *= 0.125
        self.height *= 0.125

        self.min_speed = 4
        self.max_speed = 20

    def update(self, width, height, paddles):

        # Calculate the new coordinate. Add the old position and the speed together.
        self.center_x = self.center_x + self.x_speed
        self.center_y = self.center_y + self.y_speed

        # Paddle collision
        # Check collision with a list containing the Player and the Enemy
        print(paddles[0], paddles[1])
        collisions = self.collides_with_list(paddles)
        if len(collisions) == 1:
            paddle = collisions[0]
            distance_from_middle = abs(self.center_y - paddle.center_y)
            percentage_from_middle = distance_from_middle / self.height / 2
            speed = percentage_from_middle * self.max_speed

            self.x_speed = self.x_speed * -1
            self.x_speed = self.x_speed * 1.1
            self.y_speed = max(self.min_speed, speed) * \
                1 if distance_from_middle > 0 else -1

        # Top side
        if self.top > height:
            self.y_speed = self.y_speed * -1
        # Bottom side
        if self.bottom < 0:
            self.y_speed = self.y_speed * -1

    def check_outside(self, width):
        if self.right > width + 200:
            return "right"
        elif self.left < 0 - 200:
            return "left"

    def reset(self, width, height):
        self.center_x = width / 2
        self.center_y = height / 2
        self.x_speed = self.x_speed * -1
        self.y_speed = randint(-10, 10)
