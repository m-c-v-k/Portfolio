#! Python3


class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x},{self.y}.{self.z})"

    def __add__(self, other):
        self.x2 = self.x + other.x
        self.y2 = self.y + other.y
        self.z2 = self.z + other.z
        return self.__class__(self.x2, self.y2, self.z2)

    def __sub__(self, other):
        self.x2 = self.x - other.x
        self.y2 = self.y - other.y
        self.z2 = self.z - other.z
        return self.__class__(self.x2, self.y2, self.z2)

    def __mul__(self, other):
        scalprod = self.x * other.x + self.y * other.y + self.z * other.z
        return scalprod


v1 = Vector(1, 1, 5.1)
v2 = Vector(2, 2, 5.1)
v3 = v1 + v2
v4 = v1 - v2
v5 = v3 * v2

print(v1)
print(v2)
print(v2)
print(v4)
print(v5)
