from enum import StrEnum


def main():
    while True:
        d_text = input("Which direction [n,s,w,e,nw,ne,sw,se]? ")
        m = Moves.parse(d_text)

        if m is None:
            print("That's not a move, goodbye!")
            break

        print(m)

        # ******** less pythonic ********
        if m == Moves.North or m == Moves.South or m == Moves.West or m == Moves.East:
            print("That's a direct move.")
        else:
            print("That's a diagonal move.")


class Moves(StrEnum):
    West = "West"
    North = "North"
    East = "East"
    South = "South"
    NorthEast = "NorthEast"
    SouthEast = "SouthEast"
    NorthWest = "NorthWest"
    SouthWest = "SouthWest"

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
