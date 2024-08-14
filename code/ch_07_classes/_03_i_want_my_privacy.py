class PetSnake:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self._protected_val = 2
        self.__pvt = True

    def __str__(self):
        return (f"Pet: {self.name} age: {self.age}, "
                f"protection level: {self._protected_val}, "
                f"private: {self.__pvt}")

    def something(self):
        ...


print("Here is my pet snake:")
py = PetSnake("Slide", 6)
print(py.age)
print(py.name)
# print(py._protected_val) # recommended against
# print(py.__pvt) # bang, crash, pow, **! # Never access this outside of the class.
print(py)
print(dir(py))

#
#
#
#
#
#
#
#
#
#
#


# # py.__name = py.__name.upper()
# print(dir(py))
# # print("She is named {} and {} years old.".format(py.__name, py.__age))
# print(py._protected_val)
