# Christin Kere
# UWYO COSC 1010
# Submission Date: 11/4/24
# Lab 08
# Lab Section: 14
# Sources, people worked with, help given to: Danny's PPT, Youtube
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def convert_to_number(value):
    if value.isdigit() or (value[0]=='-' and value[1:].isdigit()):
        return int(value)
    if value.count('.')==1 and value.replace('.','',1).isdigit() and value.count('-')<=1:
        return float(value)
    return False

print(convert_to_number("123"))
print(convert_to_number("123.4"))
print(convert_to_number("123.45.67"))
print(convert_to_number("abc"))
print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def slope_intercept(m,b,lower_bound, upper_bound):
    if not (isinstance(lower_bound, int) and isinstance(upper_bound, int)):
        return False
    if lower_bound>upper_bound:
        return False
    y_values = [(m*x+b) for x in range(lower_bound, upper_bound +1)]
    return y_values
print(slope_intercept(2,3,0,5))
print(slope_intercept(1.5,-2,-2,2))
print(slope_intercept(1,0,5,3))
print(slope_intercept(1,1,"a",4))
print("*" * 75)
# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def get_user_input():
    while True:
        m_input = input("Enter the slope (m) or type 'exit' to quit: ")
        if m_input.lower()=='exit':
            break
        b_input = input("Enter the y-intercept (b): ")
        lower_bound_input = input("Enter the lower X bound: ")
        upper_bound_input = input("Enter the upper X bound")
        m = convert_to_number(m_input)
        b = convert_to_number(b_input)
        lower_bound = convert_to_number(lower_bound_input)
        upper_bound = convert_to_number(upper_bound_input)
        if m is False or b is False or lower_bound is False or upper_bound is False:
            print("Invalid input. Please enter valid integers or floats for m and b, and integers for the bounds.")
            continue
        result = slope_intercept(m,b,lower_bound,upper_bound)
        if result is False:
            print("Invaid bounds. Make sure the lower bound is less than or equal to the upper bound. ")
        else:
            print(f"Calculate y-values: {result}")
get_user_input

import math
def safe_sqrt(value):
        """Returns the square root of a number if non-negatuve; returns None if negative."""
        if value<0:
            return None
        return math.sqrt(value)
def quadratic_formula(a,b,c):
    """Solves the quadratic equation ax^2+bx+c=0 and returns the roots."""
    discriminant=b**2 - 4*a*c
    sqrt_discriminant=safe_sqrt(discriminant)
    if sqrt_discriminant is None:
        return None 
    root1=(-b + sqrt_discriminant) / (2*a)
    root2=(-b - sqrt_discriminant) / (2*a)
    return (root1,root2)
print(quadratic_formula(1,-3,2))
print(quadratic_formula(1,2,1))
print(quadratic_formula(1,0,-4))
print(quadratic_formula(1,0,4))

def get_quadratic_input():
    while True:
        a_input = input("Enter the coefficicent a, or type 'exit' to quit: ")
        if a_input.lower()=='exit':
            break
        b_input= input("Enter the coefficient b: ")
        c_input= input("Enter the coefficient c: ")
        a= convert_to_number(a_input)
        b=convert_to_number(b_input)
        c=convert_to_number(c_input)

        if a is False or b is False or c is False or a==0:
            print("Invalid input. Please enter valid numbers, and 'a' must not be zero. ")
            continue 
        result=quadratic_formula(a,b,c)
        if result is None:
            print("No real roots.")
        else:
            print(f"The roots of the equation are: {result[0]:.2f}")
        get_quadratic_input