import random


def call_function(obj, method: str, *args):
    """
    Динамічно викликає метод об'єкту з наданими аргументами.

    Arguments:
        obj: Об'єкт, метод якого буде викликано.
        method (str): Назва методу, який буде викликано.
        *args: Аргументи, що будуть передані в метод. 

    Returns:
        Any: Поверне результат виклику методу.
    """

    if not hasattr(obj, method):
        raise AttributeError(f"Object {obj} has no method '{method}'.")

    method_to_call = getattr(obj, method)

    try:
        result = method_to_call(*args)
        return result
    except Exception as e:
        raise RuntimeError(f"An error occurred while calling the method '{method}': {e}")


# Країни та їх міста з відмітками про категорії
cities = {
    "united_states": [
        {"city": "Miami", "categories": ["beach"]},
        {"city": "New York", "categories": ["city break"]},
        {"city": "San Francisco", "categories": ["culture"]},
    ],
    "spain": [
        {"city": "Barcelona", "categories": ["city break", "beach"]},
        {"city": "Madrid", "categories": ["city break"]},
        {"city": "Seville", "categories": ["culture"]},
    ],
    "italy": [
        {"city": "Rome", "categories": ["history", "culture"]},
        {"city": "Venice", "categories": ["romantic", "waterways"]},
        {"city": "Florence", "categories": ["art", "culture"]},
    ],
}


class CityForTravel:
    """Демонстративний клас без конструктора для отримання міста заданим чином."""

    def get_city_by_country(self, country_name: str) -> str:
        """
        Повертає випадкове місто за заданою краною.
        
        Arguments:
            country_name (str): Назва країни.

        Return:
            str: Повертає назву випадкового міста з заданої країни.
        """

        result_city = (
            random.choice(cities.get(country_name.strip().lower(), {}))
            .get('city')
            .title()
        )

        return result_city

    def get_city_by_category(self, country_name: str, category_name: str) -> str:
        """
        Повертає випадкове місто за заданою країною і категорією.
        
        Arguments:
            country_name (str): Назва країни.
            category_name (str): Назва туристичної категорії.

        Return:
            str: Назва випадкового міста з наданих країни і категорії. 
        """

        result_city = (
            random.choice(
                [
                    city for city in cities[country_name.strip().lower()]
                    if category_name.strip().lower() in [
                        city_name for city_name in city.get('categories', '')
                    ]
                ]
            )
            .get('city')
            .title()
        )

        return result_city


if __name__ == "__main__":
    city = CityForTravel()

    print("Місто за заданою країною:", call_function(city, "get_city_by_country", " ItalY"))
    print(
        "Місто за заданими країною і катагерією:",
        call_function(city, "get_city_by_category", "United_states", "city break")
    )

    try:
        print(call_function(city, "spain"))
    except Exception as e:
        print(e)

    try:
        print(call_function(city, "get_city_by_category", "spain", 2))
    except Exception as e:
        print(e)
