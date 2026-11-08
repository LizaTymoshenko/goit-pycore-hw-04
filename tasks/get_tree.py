from colorama import Fore, Style
from pathlib import Path
import sys

def get_dir_structure(path: Path):
    """
    Gets full tree structure of specified directory.
    """
    try:
        assert path.exists(), f"Path {path} does not exist."
        assert path.is_dir(), f"Path {path} is not a directory."
    except AssertionError as e:
        print(Fore.RED + '[ERROR] ' + Style.RESET_ALL + str(e))
        return


    # walk the directory
    def discover_dir(path: Path, level: int) -> None:
        def get_indent(level: int) -> str:
            return level * '   '
        indent = get_indent(level)
        # print folder name 
        print(indent + Fore.BLUE + path.name + '/')
        children = sorted([c for c in path.iterdir()])
        # all chilndren printed on next level
        level += 1
        indent = get_indent(level)
        for p in children:
            if p.is_dir():
                discover_dir(p, level)
            else:
                print(indent + Fore.GREEN + p.name)

    level = 0
    discover_dir(path, level)


def main():
    # get directory name
    try:
        target_dir = sys.argv[1]
        path = Path(target_dir)
    except IndexError:
        print("Please provide a directory you want to analyze as command argument.",
              "\nExample command: uv run get_tree.py tasks/")
    else:
        get_dir_structure(path)

if __name__ == "__main__":
    main()
    
    