class Rectangle:
    """
    Represents a rectangle with width and height.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width: int | float, height: int | float):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        if (
            isinstance(width, (int, float)) and 
            isinstance(height, (int, float)) and 
            width > 0 and 
            height > 0
        ):
            self.width = width
            self.height = height
        else:
            if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
                raise TypeError("width and heigh must be int or float")
            elif width > 0 or height > 0:
                raise ValueError("width and heigh must be more than 0")

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float | int: The area of the rectangle.
        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculate the parimeter of the rectangle.

        Returns:
            float | int: The perimeter of the rectangle.
        """
        return self.height + self.width

    def is_square(self) -> bool:
        """
        Checks if the rectangle is a square.

        Rerurns:
            bool: True if the rectangle square, else False 
        """
        return True if self.height == self.width else False

    def resize(self, new_width: int | float, new_height: int | float):
        """
        Resizes the rectangle.

        Args:
            new_width (int | float): The new width of the rectangle. 
            new_height (int | float): The new height of the rectangle. 
        """
        if (
            isinstance(new_width, (int, float)) and 
            isinstance(new_height, (int, float)) and 
            new_width > 0 and 
            new_height > 0
        ):
            self.width = new_width
            self.height = new_height
        else:
            if not isinstance(new_width, (int, float)) or not isinstance(new_height, (int, float)):
                raise TypeError("new_width and new_height must be int or float")
            elif new_width <= 0 or new_height <= 0:
                raise ValueError("new_width and new_height must be more than 0")
    

if __name__ == "__main__":
    # Демонстрація роботи з класом та методами
    my_rectangle = Rectangle(3, 7)

    print(f"Площа прямокутника: {my_rectangle.area()}")
    print(f"Периметр прямокутника: {my_rectangle.perimeter()}")
    print(f"Це квадрат: {my_rectangle.is_square()}")
    my_rectangle.resize(10, 10)
    print(f"Це квадрат: {my_rectangle.is_square()}")

    #Демонстрація помилок
    try:
        test_rectange = Rectangle(1, '')
    except TypeError as e:
        print(f"Type error: {e}")

    try:
        my_rectangle.resize(-2, 11)
    except ValueError as e:
        print(f"Value error: {e}")
