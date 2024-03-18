import math

# task 1. Write a Python program that generates a list of squares of numbers from 1 to 10 using list comprehensions.ares)
squares = [i**2 for i in range(1,11)]
print(squares)

# task 2. Expand the previous program by defining a function that takes a range of numbers as input and returns a list of 
# squares for that range. e_squares(start,end))
def squares_of_range(start, end):
    range_squares = [i**2 for i in range(start, end+1)]



# task 4. Utilize the math library to calculate the squareroot of each number in the generated list from the previous task.
roots = [math.sqrt(i) for i in squares]
print(roots)



