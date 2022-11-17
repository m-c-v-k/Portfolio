#! Python2


class Vector:

    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        return f"Vector{self.args}"

    def __add__(self, other):
        v = [arg1 + arg2 for arg1, arg2 in zip(self.args, other.args)]
        return self.__class__(*v)

    def __sub__(self, other):
        v = [arg1 - arg2 for arg1, arg2 in zip(self.args, other.args)]
        return self.__class__(*v)

    def __mul__(self, other):
        scalprod = sum(
            [arg1 * arg2 for arg1, arg2 in zip(self.args, other.args)])

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
