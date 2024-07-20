import os


def main():
    root_dir = '/Users/mkennedy/github/talk-python/courses/jumpstart-demos/transcripts'

    files = get_files(root_dir)
    print("Found these files")
    for f in files:
        print(f)
    print('done')


def get_files(folder):
    for item in os.listdir(folder):

        full_item = os.path.join(folder, item)
        # print(full_item)
        if os.path.isfile(full_item):
            yield full_item
        elif os.path.isdir(full_item):
            # for f in get_files(full_item):
            #     yield f
            yield from get_files(full_item)


if __name__ == '__main__':
    main()
