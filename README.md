# python-oop-projects
Python tutorials and small OOP projects

Follow along the Udemy course [Intermediate to Advanced Python with 10 OOP Projects](https://www.udemy.com/course/the-python-pro-course).

## Application # 1 - [Geometry Game](./geometry_game/)
The game is about users guessing points inside a rectangle and the area of a rectangle. Rectangles have coordinates for their lower-left and upper-right corners and points also have coordinates.

#### Example:
```
Rectangle coordinates: 9 , 1 and 17 , 18
Guess X: _1_
Guess Y: _2_
Guess rectangle area: _12_
Your point was inside the rectangle:  False
Your areas was off by:  124.0
```

## Application # 2 - [Flatmates Bill](./flatmates_bill/)
The app gets as input the amount of a bill for a particular period
and the days that each of the flatmates stayed in the house for that period and returns how much each flatmate has to pay. It also generates a PDF report stating the names of the flatmates, the period, and how much each of them had to pay.

### Example:
```
Enter the bill period: _Dec 2023_
Enter the bill amount: _2345_

Enter the name of the first flatmate: _Kris_
Enter the number of days Kris stayed in the house: _25_

Enter the name of the second flatmate: _Leeloo_
Enter the number of days Leeloo stayed in the house: _31_

Kris pays: 1046.875
Leeloo pays: 1298.125

All righty! Here is your PDF report: Dec 2023-report.pdf
```

## Application # 3 - [Math Painting](./math_painting/)
The app lets the user provide the start coordinates of geometrical shapes such as
squares and rectangles, their dimensions, and their colors, and the program produces an image file canvas with all the geometrical shapes drawn in it.

### Example:
```
Enter canvas width: _100_
Enter canvas height: _100_
Enter canvas color (black or white): _black_

What would you like to draw? (rectangle or square) Enter 'q' to quit: square
Enter x coordinate: _0_
Enter y coordinate: _0_
Enter side length: _35_
Enter square color red value: _213_
Enter square color green value: _43_
Enter square color blue value: _12_

What would you like to draw? (rectangle or square) Enter 'q' to quit: q
Enter filename: _myart_
```

![math_painting_example](math_painting/files/example.png)
