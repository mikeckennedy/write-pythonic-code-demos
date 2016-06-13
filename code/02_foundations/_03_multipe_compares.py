import datetime
from enum import Enum


def main():
    d_text = input("Which direction [n,s,w,e,nw,ne,sw,se]? ")
    m = Moves.parse(d_text)

    if m is None:
        print("That's not a move!")
        return

    print(m)

    # ******** less pythonic ********
    # if m == Moves.North or m == Moves.South or m == Moves.West or m == Moves.East:
    #     print("That's a direct move.")
    # else:
    #     print("That's a diagonal move.")

    # ******** more pythonic ********
    if m in {Moves.North, Moves.South, Moves.West, Moves.East}:
        print("That's a direct move.")
    else:
        print("That's a diagonal move.")

        # direct_moves = {Moves.North, Moves.South, Moves.West, Moves.East}
        # t0 = datetime.datetime.now()
        # speed: .2 sec for multiple tests
        #        2.3 sec for basic slow in
        #        .3 sec for cached direct moves in
        # for _ in range(0, 1000000):
        #     # b = m == Moves.North or m == Moves.South or m == Moves.West or m == Moves.East
        #     b = m in direct_moves
        #     # b = m in {Moves.North, Moves.South, Moves.West, Moves.East}
        # t1 = datetime.datetime.now()
        # dt = t1 - t0
        # print("Time delta: {:,} sec".format(dt.total_seconds()))


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
        if text == 'e':
            return Moves.East
        if text == 's':
            return Moves.South
        if text == 'n':
            return Moves.North

        if text == 'nw':
            return Moves.NorthWest
        if text == 'sw':
            return Moves.SouthWest
        if text == 'ne':
            return Moves.NorthEast
        if text == 'se':
            return Moves.SouthEast

        return None


if __name__ == '__main__':
    main()





