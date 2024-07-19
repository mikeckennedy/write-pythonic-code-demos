# Basic types
import typing
from typing import Optional, Union

i: int = 1
f: float = 2.17273
c: complex = complex(f, i)
txt: str = "abc"
b: bytes = b"bytes string"
truth: bool = True
unknown: typing.Any = "What is this?"

# More about the numbers
# Leverages the "numerical tower" in Python typing
x: complex = i
print(x)
x = f
print(x)
x = c
print(x)
print(i, f, c)
print(txt)

# Optional
txt_maybe: Optional[str] = "Some string"
print(txt_maybe)
txt_maybe = None
print(txt_maybe)

txt1: Union[str, None] = "Style 1"
txt2: Optional[str] = "Style 2, Michael's Fav!"
txt3: str | None = "Style 3"

something: int | str | list = 1

# Collections

# typing.List[int] = [1, 2, 3]

numbers: list[int] = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# numbers: list[str] = []

for n in numbers:
    print(n * n, end=', ')

data: dict[str, str] = {'name': "Full name", "email": "me@me.com"}
data2: dict[str, int] = {'low': 10, "high": 100}

v = data['email']
print()
print(v)

s: set[int] = {1, 1, 2, 3, 5}

t: tuple[int, int, int, list[str]] = (1, 2, 3, ["hi", "Hello typing!"])
