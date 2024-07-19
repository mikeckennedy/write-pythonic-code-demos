import random
import typing
from typing import Optional


def main():
    print(say_hello())
    print(say_hello("Michael"))

    m = Motorcycle("KTM Enduro", 690)
    print(m)

    m2 = Motorcycle.create_random('Amazon bike')
    print(m2)

    m3 = Motorcycle.create_random('Amazon bike')
    print(m2.compare_things(m))


def say_hello(name: Optional[str] = None) -> int:
    msg = "Hello World!"
    if name:
        msg = f"Hello there {name}!"
    print(msg)

    return len(msg)


class Motorcycle:

    def __init__(self, model: str, engine_size: float):
        self.model = model
        self.engine_size = engine_size

    def __str__(self) -> str:
        return str(self.__dict__)

    @classmethod
    def create_random(cls, model: str) -> typing.Self:
        size = random.randint(50, 700)
        return Motorcycle(model, size)

    def compare_things(self, other: typing.Self) -> bool:
        return self.model == other.model


if __name__ == '__main__':
    main()
