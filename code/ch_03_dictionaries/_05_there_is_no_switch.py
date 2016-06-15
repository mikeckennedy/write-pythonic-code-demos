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
        parse_dict = {
            'w': Moves.West, 's': Moves.South, 'e': Moves.East, 'n': Moves.North,
            'nw': Moves.NorthWest, 'ne': Moves.NorthEast, 'sw': Moves.SouthWest, 'se': Moves.SouthEast
        }
        return parse_dict.get(text)


class Character:
    def __init__(self, name):
        self.name = name

    def move(self, direction: Moves):
        action_dict = {
            Moves.North: lambda: print("{} moves north with a special hesitation!".format(self.name)),
            Moves.South: lambda: print("{} is going south for winter!".format(self.name))
        }

        action = action_dict.get(
            direction,
            lambda: print("{} moves quickly to {}".format(self.name, direction)))
        action()


if __name__ == '__main__':
    main()
