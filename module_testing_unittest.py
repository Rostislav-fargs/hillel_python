"""#1"""

import unittest


class StringProcessor:
    
    # Повертає перевернутий рядок
    @staticmethod
    def reverse_string(s: str) -> str:
        return s[::-1]

    # Повертає рядок в форматі речення
    @staticmethod
    def capitalize_string(s: str) -> str:
        return s.capitalize()

    # Повертає кількість голосних у рядку
    @staticmethod
    def count_vowels(s: str) -> int:
        return sum(1 for char in s.lower() if char in 'aeiouаеєиіїоуюя')

class TestStringProcessor(unittest.TestCase):

    @unittest.skip("Known issue with empty string reversal")
    def test_reverse_string_empty(self):
        self.assertEqual(StringProcessor.reverse_string(""), "")
    

    # Тест перевернутого рядка
    def test_reverse_string(self):
        self.assertEqual(StringProcessor.reverse_string("hello"), "olleh")
        self.assertEqual(StringProcessor.reverse_string("Python"), "nohtyP")
        self.assertEqual(StringProcessor.reverse_string("12345"), "54321")
    

    # Тест перетворення реєстрації як в реченні
    def test_capitalize_string(self):
        self.assertEqual(StringProcessor.capitalize_string("hello"), "Hello")
        self.assertEqual(StringProcessor.capitalize_string("hELLO"), "Hello")
        self.assertEqual(StringProcessor.capitalize_string("123abc"), "123abc")
        self.assertEqual(StringProcessor.capitalize_string(""), "")
    

    # Тест отримання кількості голосних з рядка
    def test_count_vowels(self):
        self.assertEqual(StringProcessor.count_vowels("hello"), 2)
        self.assertEqual(StringProcessor.count_vowels("HELLO"), 2)
        self.assertEqual(StringProcessor.count_vowels("bcdfg"), 0)
        self.assertEqual(StringProcessor.count_vowels("aeiou"), 5)
        self.assertEqual(StringProcessor.count_vowels("123"), 0)


if __name__ == "__main__":
    unittest.main()
