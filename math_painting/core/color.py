"""
Manage color in GRB format.
"""


class Color:
    """
    Class for managing color in GRB format.
    """

    def __init__(self, red: int = 255, green: int = 255, blue: int = 255):
        """
        Initialize a Color object.

        Args:
            red (int): The red component of the color. Defaults to 255.
            green (int): The green component of the color. Defaults to 255.
            blue (int): The blue component of the color. Defaults to 255.

        """
        if not 0 <= red <= 255:
            raise ValueError(f"Red must be within 0-255 limit, but is {red}")
        if not 0 <= green <= 255:
            raise ValueError(f"Green must be within 0-255 limit, but is {green}")
        if not 0 <= blue <= 255:
            raise ValueError(f"Blue must be within 0-255 limit, but is {blue}")

        self.red: int = red
        self.green: int = green
        self.blue: int = blue
