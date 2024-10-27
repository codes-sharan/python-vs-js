class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Index out of range")

# Usage
p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1)               # Output: Point(1, 2)
print(repr(p1))        # Output: Point(1, 2)
print(p1 + p2)         # Output: Point(4, 6)
print(p1 == p2)        # Output: False
print(len(p1))         # Output: 2
print(p1[0])           # Output: 1
