"""#8"""

import json
from typing import Any


class JSONConfigManager:
    """
    Менеджер конфігурації, що працює з json файлом.
    """

    def __init__(self, config_file: str) -> None:
        """
        Ініціалізує менеджер конфігурації.

        Arguments:
            config_file: Шлях до файлу json.
        """
        self.config_file: str = config_file
        self.config: dict[str, Any] = {}


    def __enter__(self) -> "JSONConfigManager":
        """
        Завантажує конфігурацію з файлу при вході у контекст.

        Returns:
            JSONConfigManager: Об'єкт менеджера конфігурації.
        """
        try:
            with open(self.config_file, 'r', encoding="utf-8") as file:
                self.config = json.load(file)
        except FileNotFoundError as e:
            print(f"Error getting data from {self.config_file}: {e}")
            self.config = {}

        return self


    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """
        Зберігає конфігурацію у файл при виході з контексту.
        """
        if exc_type:
            print(f"Exception occurred: {exc_type}, {exc_value}")
        with open(self.config_file, 'w', encoding="utf-8") as file:
            json.dump(self.config, file, ensure_ascii=False, indent=4)


    def get(self, key: str, fallback: Any=None) -> Any:
        """
        Отримує значення з конфігурації за вкладеним ключем.

        Arguments:
            key (str): Ключ у форматі "section.subsection.key".
            fallback (Any): Значення за замовчуванням, якщо ключ не знайдено.

        Returns:
            Any: Значення за ключем або fallback, якщо ключ відсутній.
        """
        if not isinstance(key, str):
            raise TypeError("'key' must be 'str'")

        keys = key.split('.')
        result = self.config
        for k in keys:
            result = result.get(k, fallback)
            if result is None:
                return fallback
        return result


    def set(self, key: str, value: Any) -> None:
        """
        Встановлює значення у конфігурації за вкладеним ключем.

        Arguments:
            key (str): Ключ у форматі "section.subsection.key".
            value (Any): Значення, яке потрібно зберегти.

        Raises:
            ValueError: Якщо key є порожнім рядком.
        """
        if not isinstance(key, str):
            raise TypeError("'key' must be 'str'")

        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            config = config.setdefault(k, {})
        config[keys[-1]] = value


if __name__ == "__main__":
    with JSONConfigManager("main_config.json") as config_manager:

        config_manager.set("user.region.country", 'Ukraine')
        config_manager.set("user.region.lang", 'ua')
        print(config_manager.get('user.region'))

        config_manager.set("user.name", "Mark")
        print(config_manager.get('region'))

        print(config_manager.get('user'))
