from pathlib import Path

def read_lines(path: Path):
    with open(path, 'r', encoding='UTF-8') as file:
        for line in file:
            yield line.strip()