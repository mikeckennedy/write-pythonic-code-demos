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

        moves_lookup = {
            'w': Moves.West, 'e': Moves.East, 's': Moves.South, 'n': Moves.North,
            'nw': Moves.NorthWest, 'ne': Moves.NorthEast, 'sw': Moves.SouthWest, 'se': Moves.SouthEast
        }
        # NOTE: Could also add methods for the keys and call them...
        return moves_lookup.get(text)


class Character:
    def __init__(self, name):
        self.name = name

    def move(self, direction: Moves):
        moves_lookup = {
            Moves.West: lambda: print("{} moves west carefully.".format(self.name)),
            Moves.East: lambda: print("{} moves east quickly.".format(self.name)),
            Moves.South: lambda: print("{} runs downward.".format(self.name)),
            Moves.North: lambda: print("{} runs up.".format(self.name)),
        }
        method = moves_lookup.get(direction, lambda: print("{} can't run that way.".format(self.name)))
        method()


if __name__ == '__main__':
    main()
