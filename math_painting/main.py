from core.canvas import Canvas
from core.shape import Rectangle, Square
from core.color import Color


def draw_rectangle(canvas: Canvas) -> None:
    """Draw a rectangle on the canvas."""
    # Get user input dimensions
    x: int = int(input("Enter x coordinate: "))
    y: int = int(input("Enter y coordinate: "))
    width: int = int(input("Enter width: "))
    height: int = int(input("Enter height: "))

    # get user input color
    color_r: int = int(input("Enter rectable color red value: "))
    color_g: int = int(input("Enter rectable color green value: "))
    color_b: int = int(input("Enter rectable color blue value: "))
    shape_color = Color(color_r, color_g, color_b)

    user_shape = Rectangle(x, y, width, height, shape_color)
    user_shape.draw(canvas)


def draw_square(canvas: Canvas) -> None:
    """Draw a square on the canvas."""
    # Get user input dimensions
    x: int = int(input("Enter x coordinate: "))
    y: int = int(input("Enter y coordinate: "))
    side: int = int(input("Enter side length: "))

    # get user input color
    color_r: int = int(input("Enter square color red value: "))
    color_g: int = int(input("Enter square color green value: "))
    color_b: int = int(input("Enter square color blue value: "))
    shape_color = Color(color_r, color_g, color_b)

    user_shape = Square(x, y, side, shape_color)
    user_shape.draw(canvas)


if __name__ == "__main__":
    # Get user input about canvas dimensions
    canvas_width: int = int(input("Enter canvas width: "))
    canvas_height: int = int(input("Enter canvas height: "))

    # Get user input about canvas color
    while True:
        colors = {"black": Color(0, 0, 0), "white": Color(255, 255, 255)}
        canvas_color_str: str = (
            input("Enter canvas color (black or white): ").strip().lower()
        )
        if canvas_color_str not in ["black", "white"]:
            print("Invalid input. Please enter 'black' or 'white'.")
        else:
            # Create Canvas
            canvas = Canvas(canvas_width, canvas_height, colors[canvas_color_str])
            break

    # Draw shapes
    while True:
        user_input_shape: str = (
            input(
                "\nWhat would you like to draw? (rectangle or square) "
                "Enter 'q' to quit: "
            )
            .strip()
            .lower()
        )

        if user_input_shape == "q":
            filename: str = input("Enter filename: ")
            if not filename.endswith(".png"):
                filename += ".png"

            canvas.make(filename)
            print("\nDone! Your image has been saved as", filename)
            break
        if user_input_shape == "rectangle":
            draw_rectangle(canvas)
        elif user_input_shape == "square":
            draw_square(canvas)
        else:
            print("Invalid input. Please enter 'rectangle' or 'square'.")
            continue
