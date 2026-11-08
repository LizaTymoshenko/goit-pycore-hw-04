from pathlib import Path
from helpers import read_lines

def get_cats_info(path: Path) -> list[dict]:
    """Reads file with cat info and process it into list of dicts."""
    cat_list = []
    # reading file
    try:
        for line in read_lines(path):
            try:
                id, name, age = line.split(',')
            except ValueError:
                print(f"Cannot unpack line {line}, expect 3 values.")
            else:
                cat_list.append({'id': id.strip(), 'name': name.strip(), 'age': age.strip()})
    except FileNotFoundError:
        print(f"File {path} does not exist.")
    return cat_list

if __name__ == '__main__':
    cats_info = get_cats_info("path/to/cats_file.txt")
    print(cats_info)

    cats_info = get_cats_info("data/cats.txt")
    print(cats_info)

    cats_info = get_cats_info("tasks/data/cats.txt")
    print(cats_info)
