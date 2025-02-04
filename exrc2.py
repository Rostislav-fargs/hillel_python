"""Завдання #2"""

def read_file_lines(file_name: str) -> list:
    """
    Reads the lines from a text file.

    Arguments:
        file_name (str): The name of the text file (must end with '.txt').

    Returns:
        numbers_list (list): A list of numbers from the file.
    """

    if not isinstance(file_name, str):
        raise TypeError("The argument 'file_name' must be string")
    if not '.txt' in file_name:
        raise ValueError("The argument 'file_name' must end with '.txt'")

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            file_lines = file.readlines()

            if len(file_lines) == 1:
                numbers_list = [
                    float(num.strip(',')) if '.' in num else int(num.strip(','))
                    for num in file_lines[0].split()
                ]
            else:
                numbers_list = [
                    float(line.strip(',')) if '.' in line else int(line.strip(','))
                    for line in file_lines
                ]

    except FileNotFoundError as e:
        print("FileNotFoundError", e)
    except ValueError as e:
        print("ValueError", e)
    else:
        return numbers_list

    return None

def list_average(numbers_list: list) -> float:
    """Returns average of given numbers list."""

    return sum(numbers_list) / len(numbers_list)


def get_average_from_file(file_name: str) -> float:
    """Returns average from a text file with given file_name."""

    numbers = read_file_lines(file_name)

    if not numbers:
        print("File is empty.")
        return None

    return list_average(numbers)


if __name__ == "__main__":
    NUMBERS_FILE = "numbers.txt"
    print(get_average_from_file(NUMBERS_FILE))
