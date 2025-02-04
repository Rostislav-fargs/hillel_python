import random
import pprint

class InsufficientResourcesException(Exception):
    """Exception raised when there are insufficient resources to perform an action in the game."""

    def __init__(self, required_resource, required_amount, current_amount, unit):
        """Initializes the InsufficientResourcesException with the given attributes."""

        super().__init__(
            f"Недостатньо ресурсу: {required_resource}."
            f"Потрібно {required_amount} {unit}, а є лише {current_amount} {unit}."
        )
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount
        self.unit = unit


def get_random_resources(unit_hierarchy: dict, start: int, end: int) -> dict:
    """
    Generates a dictionary of random resource amounts for a given unit hierarchy.
        
    Args:
        unit_hierarchy (dict): A dictionary where keys are resource names and values are lists of unit types.
        start (int): The minimum value for resource amounts.
        end (int): The maximum value for resource amounts.

    Returns:
        dict: A dictionary where the keys are resources and the values are dictionaries with `amount` and `unit`.
    """

    random_resources = {
        k : {
            "amount" : round(random.uniform(start, end), 3),
            "unit" : random.choice(v)
        }for k, v in unit_hierarchy.items()
    } 
    return random_resources


def space_engineer(game_actions: dict, player_resources: dict):
    """
    Simulates a player's attempt to perform actions in a game based on available resources.

    Args:
        game_actions (dict): A dictionary containing the game actions with their required resources and amounts.
        player_resources (dict): A dictionary containing the player's available resources and amounts.

    Prints:
        Displays the player's resources and attempts to perform the actions.
        If the player has insufficient resources, an exception is raised, and the action cannot be performed.
    """

    print("Ваші ресурси:")
    pprint.pprint(player_resources)
    
    print("-"*20, "\nВиконання операцій:")

    for action, data in game_actions.items():
        required_resource = data["required_resource"]
        required_amount = data["required_amount"]
        unit = data["unit"]
        
        current_amount = player_resources.get(required_resource, {}).get("amount", 0)
        
        try:
            if current_amount < required_amount:
                raise InsufficientResourcesException(required_resource, required_amount, current_amount, unit)
            print(f"\033[32mВиконано: {action}\033[0m")
        except InsufficientResourcesException as e:
            print(f"\033[31mНеможливо виконати '{action}': {e}\033[0m")


if __name__ == "__main__":
    # Набір ігрових подій
    game_actions = {
        "замінити кріогенну рідину" : {
            "required_resource" : "азот",
            "required_amount" : 302.8,
            "unit" : "літр"
        },
        "оновити ПЗ автопілота" : {
            "required_resource" : "носій пам'яті",
            "required_amount" : 634.801,
            "unit" : "петабайт"
        },
        "встановити додаткове освітлення" : {
            "required_resource" : "енергія",
            "required_amount" : 89,
            "unit" : "вт/год"
        }
    }
    # Ієрархія множин вимірювання
    unit_hierarchy = {
        "азот" : ["мілілітр", "літр"],
        "енергія" : ["вт/год", "кВт/год"],
        "носій пам'яті" : ["гігабайт", "петабайт"]
    }
    
    # Ініціалізація ресурсів гравця із випадковими значеннями
    player_resources = get_random_resources(0, 1000)

    # Виклик функції для імітації гри
    space_engineer(game_actions, player_resources)
