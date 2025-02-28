"""#7.2"""

import pytest

from file_processor import FileProcessor


# Тест запису до тимчасового файлу
def test_file_write_read(tmpdir):
    file = tmpdir.join("testfile.txt")
    FileProcessor.write_to_file(file, "Hello, World!")
    content = FileProcessor.read_from_file(file)
    assert content == "Hello, World!"


# Тест запису та читання різних даних у тимчасовому файлі
@pytest.mark.parametrize("data", [
    "",  # порожній рядок
    "Тестові дані\nЩе один рядок",  # кілька рядків
    "A" * 10**2  # 1 мільйон символів
])
def test_file_write_read_various_data(tmpdir, data):
    file = tmpdir.join("testfile.txt")
    FileProcessor.write_to_file(file, data)
    assert FileProcessor.read_from_file(file) == data


# Тест читання неіснуючого файлу
def test_read_nonexistent_file():
    with pytest.raises(FileNotFoundError, match="Файл .* не знайдено"):
        FileProcessor.read_from_file("nonexistent.txt")
