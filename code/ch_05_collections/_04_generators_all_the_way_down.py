from pathlib import Path
from typing import Iterator


def main():
    root_dir = Path('/Users/michaelkennedy/Desktop/pythonic-course/transcripts/')
    # Let's list the files in that folder using generators.
    print("Searching for files in dir:")
    for file in get_files(root_dir):
        print(file.as_posix())


def get_files(folder: Path) -> Iterator[Path]:
    for item in sorted(folder.iterdir(), key=lambda f: f.as_posix()):
        if item.is_dir():
            yield from get_files(item)
        elif item.is_file():
            yield item


if __name__ == '__main__':
    main()
