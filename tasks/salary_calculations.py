from pathlib import Path
from helpers import read_lines

def total_salary(path: Path) -> tuple:
    """Get salaries of all workers and calculate total and average salary"""
    salaries = []
    # read salaries from the file
    try:
        for line in read_lines(path):
            try:
                name, salary = line.split(',')
            except ValueError:
                print(f"Wrong line format: {line}. Skipping.")
                continue
            try:
                salaries.append(int(salary))
            except ValueError:
                print(f"Cannot convert salary of {name} with value {salary}, type {type(salary)} to integer. Skipping.")
    except FileNotFoundError as e:
        print(f"There's no file {path}")
        return (0,0)
    # calculate total and mean salary
    if not salaries:
        print(f"File {path} is empty.")
        return (0,0)
    return (sum(salaries), sum(salaries) / len(salaries))


if __name__ == '__main__':
    total, average = total_salary("path/to/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    total, average = total_salary("data/salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    total, average = total_salary("tasks/data/salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    total, average = total_salary("tasks/data/salaries_empty.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

