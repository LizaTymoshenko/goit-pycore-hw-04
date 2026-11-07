from pathlib import Path

def total_salary(path: Path) -> tuple:
    """Get salaries of all workers and calculate total and average salary"""
    salaries = []
    # read salaries from the file
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            for line in file:
                name, salary = line.split(',')
                try:
                    salaries.append(int(salary))
                except ValueError:
                    print(f"Cannot convert salary of {name} with value {salary}, type {type(salary)} to integer. Skipping.")
    except FileNotFoundError as e:
        print(f"There's no file {path}")
        return (0,0)
    # calculate total and mean salary
    return (sum(salaries), sum(salaries) / len(salaries))


if __name__ == '__main__':
    total, average = total_salary("path/to/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    total, average = total_salary("data/salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    total, average = total_salary("tasks/data/salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

