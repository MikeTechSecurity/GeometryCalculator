# GeometryCalculator
Geometry Calculator in Python

Write a program that displays the following menu:
-------------------------------------------------
  Geometry Calculator
1. Calculate the Area of a Circle
2. Calculate the Area of a Rectangle
3. Calculate the Area of a Triangle
4. Quit
Enter your choice (1—4).
-------------------------------------------------

If the user enters 1, the program should ask for the radius of the circle and then display its area. Use the following formula to calculate the circle's area:

    area = πr²

Use 3.14159 for and the radius of the circle for r.
If the user enters 2, the program should ask for the length and width of the rectangle, and then display the
rectangle's area. Use the following formula to calculate the rectangle's area:

    area = length x width

If the user enters 3, the program should ask for the length of the triangle's base and its height, and then display its area. Use the following formula to calculate the area of the triangle:

    area = base x height x .5

If the user enters 4, the program should end.

Use a module to display the menu.  Use modules to calculate and display the areas of each shape.  The program should validate the input.  The program should continue until the user chooses the quit option on the menu.

-----------------------------------------------------------------------------------------
# Explanation of the code:

We start by importing the math module for mathematical operations like π (pi).

The display_menu() function prints the menu to the console.

There are three functions to calculate areas (calculate_circle_area, calculate_rectangle_area, and calculate_triangle_area) with the respective formulas for each geometric shape.

get_positive_input() is a utility function that asks the user for input until they provide a valid positive number. It uses a while True loop that continues to prompt the user until the correct input is received.

The main() function contains the main program loop. It calls display_menu() and then waits for the user's choice. Based on the input, it calls the appropriate area calculation function or breaks the loop if the user chooses to quit.

The if __name__ == "__main__": block checks if the script is running as the main program and if it is, it calls the main() function to start the program.

To run the program, save the code in a .py file and execute it with Python interpreter. The program will repeatedly display the menu until the user chooses the option to quit by entering 4.
-------------------------------------------------------------------------------------------
