# task 1. Write a Python program that generates a list of squares of numbers from 1 to 10 using list comprehensions.ares)
squares = [i**2 for i in range(1,11)]

# task 2. Expand the previous program by defining a function that takes a range of numbers as input and returns a list of 
# squares for that range. e_squares(start,end))
def squares_of_range(input_range):
    range_squares = [i**2 for i in input_range]

# task 3. Create a class called SquareGenerator that has a method to generate squares for a given range of numbers.
class SquareGenerator:
    def squares_of_range(input_range):
        generate_squares = [i**2 for i in input_range]