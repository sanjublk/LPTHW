import sys


def read_in_chunks(file):
    while True:
        data = file.read(4096)
        if not data:
            break
        yield data


def cat(path: str):
    """print the content of the file to standard output."""
    with open(path) as file:
        for data in read_in_chunks(file):
            sys.stdout.write(data)


if __name__ == "__main__":
    path = sys.argv[1]
    cat(path)
