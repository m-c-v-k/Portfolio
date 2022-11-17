#! Python3

# 1.10 - The person object, experimenting
class Person:

    def __init__(self, name):
        self.__name = name
        self.__sibling = []

    def __repr__(self):
        return (f"Name:\t{self.__name}")

    def set_sibling(self, sibling):
        self.__sibling.append(sibling)

    def get_sibling(self):
        return self.__sibling


arne = Person("Arne Dalhqvist")
berith = Person("Berith Bergh")
carl = Person("Carl Qvist")

berith.set_sibling(arne)
berith.set_sibling(carl)
arne.set_sibling(berith)

print(berith.get_sibling())
