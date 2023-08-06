
class Powers:
    def __init__(self, exponent):
        self.exponent = exponent

    def __iter__(self):
        self.base = 0
        return self

    def __next__(self):
        if self.base == 100:
            raise StopIteration
        self.base += 1
        return self.base ** self.exponent


squares = Powers(2)  # 4, 9, 16, 25
cubes = Powers(3)    # 8, 27, 64,
fourth = Powers(4)   # 16, 81, 256


for n in squares:
    print(n)


print("Finished!")
