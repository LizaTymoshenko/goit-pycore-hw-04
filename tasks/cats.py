from pathlib import Path

def get_cats_info(path: Path) -> list[dict]:
    """Reads file with cat info and process it into list of dicts."""
    cat_list = []
    # reading file
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            for line in file:
                line = line.rstrip('\n')
                try:
                    id, name, age = line.split(',')
                except ValueError:
                    print(f"Cannot unpack line {line}, expect 3 values.")
                else:
                    try:
                        age = int(age)
                    except ValueError:
                        print(f"Wrong value for cat's age. Id: {id}, name: {name}, age: {age}. Will add None instead.")
                        age = None
                    cat_list.append({'id': id, 'name': name, 'age': age})
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
