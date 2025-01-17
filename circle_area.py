from math import pi


def calculate_circle_area(radius: float) -> float:
    """
    Calculates the area of the circle by radius

    Parametrs:
    radius: int | float
        The radius of the circle. Must be a non-negetive integer or float.

    Returns:
        float: The area of the circle. 
    """

    if isinstance(radius, float) and radius >= 0:
        return pi * radius**2

    
if __name__ == "__main__":
    circle_radius = float(input("Введіть радіус кола: "))
    print(calculate_circle_area(circle_radius))
