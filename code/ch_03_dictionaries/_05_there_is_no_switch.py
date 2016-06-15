from enum import Enum


def main():
    d_text = input("Which direction [n,s,w,e,nw,ne,sw,se]? ")
    m = Moves.parse(d_text)

    print("You chose: {}".format(m))

    squirrel = Character("Chippy")
    squirrel.move(m)


class Moves(Enum):
    West = 1
    North = 2
    East = 3
    South = 4
    NorthEast = 5
    SouthEast = 6
    NorthWest = 7
    SouthWest = 8

    @staticmethod
    def parse(text: str):
        if not text:
            return None

        text = text.strip().lower()
        if text == 'w':
            return Moves.West
        if text == 's':
            return Moves.South
        if text == 'e':
            return Moves.East
        if text == 'n':
            return Moves.North

        if text == 'sw':
            return Moves.SouthWest
        if text == 'nw':
            return Moves.NorthWest
        if text == 'se':
            return Moves.SouthEast
        if text == 'ne':
            return Moves.NorthEast

        return None


class Character:
    def __init__(self, name):
        self.name = name

    def move(self, direction: Moves):
        print("{} moves {}".format(self.name, direction))


if __name__ == '__main__':
    main()
