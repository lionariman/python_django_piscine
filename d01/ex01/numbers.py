def open_file(file_name: str) -> str:
    with open(file_name) as openedFile:
        data: str = openedFile.read().rstrip()
    return data

def split_str(data: str, delimiter: str) -> list:
    spld: list = data.split(delimiter)
    return spld

def print_elems(elems: list):
    for i in range(len(elems)):
        print(elems[i])

def main():
    file_name: str = "numbers.txt"
    data: str = open_file(file_name)
    spld: list = split_str(data, ",")
    print_elems(spld)

if __name__ == "__main__":
    main()