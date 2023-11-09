# Geometry Calculator - Python
# https://github.com/MikeTechSecurity/
# Display the Menu: Create a function to display the options to the user.
# Calculate Area: Create separate functions to calculate the area of a circle, rectangle, and triangle.
# Get User Input: Write a function to handle user input and validate it.
# Main Program Loop: Create a loop that will keep showing the menu and asking for input until the user chooses to quit.

import math

def display_menu():
    print("Geometry Calculator")
    print("1. Calculate the Area of a Circle")
    print("2. Calculate the Area of a Rectangle")
    print("3. Calculate the Area of a Triangle")
    print("4. Quit")
    print("Enter your choice (1—4):")

def calculate_circle_area(radius):
    area = math.pi * radius * radius
    print(f"The area of the circle is: {area:.2f}")

def calculate_rectangle_area(length, width):
    area = length * width
    print(f"The area of the rectangle is: {area:.2f}")

def calculate_triangle_area(base, height):
    area = base * height * 0.5
    print(f"The area of the triangle is: {area:.2f}")

def get_positive_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input()
        
        if choice == '1':
            radius = get_positive_input("Please enter the radius of the circle: ")
            calculate_circle_area(radius)
        elif choice == '2':
            length = get_positive_input("Please enter the length of the rectangle: ")
            width = get_positive_input("Please enter the width of the rectangle: ")
            calculate_rectangle_area(length, width)
        elif choice == '3':
            base = get_positive_input("Please enter the base of the triangle: ")
            height = get_positive_input("Please enter the height of the triangle: ")
            calculate_triangle_area(base, height)
        elif choice == '4':
            print("Thank you for using the Geometry Calculator.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the program
if __name__ == "__main__":
    main()
