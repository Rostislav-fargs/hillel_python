"""Завдання #3"""

import random


class GameEventException(Exception):
    """Game event info"""
    def __init__(self, event_type: str, details: dict):
        super().__init__(f"Подія: {event_type}")
        self.event_type = event_type
        self.details = details

    def get_details(self):
        """Return game events details"""
        key, value = next(iter(self.details.items()))
        return {"action": key, "result": value}


def space_engineer():
    """Simulate game"""
    print("Ви інженер на космічному кораблі.")
    try:
        event = random.choice(list(game_events.keys()))
        print(f"Аварія: {event}!\nВаріанти дій для усунення:")

        action_list = list(game_events[event].keys())
        for index, action in enumerate(action_list, start=1):
            print(f"{index} - {action.capitalize()}")

        action_number = int(input("Виконати дію(номер): "))-1

        if action_number in range(len(action_list)):
            chosen_action = action_list[action_number]
            raise GameEventException(event, {chosen_action:game_events[event][chosen_action]})

    except GameEventException as e:
        event_details = e.get_details()
        print(f"{e}.\nВиконані дії: {event_details['action'].capitalize()}.")
        print(f"Результат: {event_details['result'].capitalize()}")


game_events = {
    "пожежа": {
        "спробувати загасити вогонь": "вогонь поширюється швидше, і знищує важливі компоненти",
        "відкрити люк для вентиляції": "пожежа охоплює всю зону, що призводить до вибуху",
        "вимкнути програмне забезпечення" : "гра вимкнена, крісло більше не палає"
    },
    "розгерметизація": {
        "пошук місця з пошкодженнями": "втрачається більше повітря через відкриті люки",
        "закрити всі люки": "це не допоможе — система вентиляції виявилася пошкоджена",
        "перевірити герметичність шлюзів" : "клапан закручено, чай більше не тече з термосу"
    }
}

if __name__ == "__main__":
    space_engineer()
    