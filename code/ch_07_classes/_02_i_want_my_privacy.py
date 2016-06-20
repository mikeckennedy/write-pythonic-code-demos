class PetSnake:
    def __init__(self, name, age):
        self.__age = age
        self.__name = name
        self._protected_val = 2
        self.normal = True

    def __str__(self):
        return "Pet: {} age: {}, protection level: {}".format(
            self.__name, self.__age, self._protected_val)


print("Here is my pet snake:")
py = PetSnake("Slide", 6)
# py.__name = py.__name.upper()
print(py)
print(dir(py))
# print("She is named {} and {} years old.".format(py.__name, py.__age))
print(py._protected_val)
