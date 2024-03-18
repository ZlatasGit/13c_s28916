# task 3. Create a class called SquareGenerator that has a method to generate squares for a given range of numbers.
# task 5. Handle the case where the end of the range is less than the start in the SquareGenerator class.
# task 6. Extract the SquareGenerator class into a separate module named square_generator.py.
class SquareGenerator:
    def squares_of_range(start, end):
        if end<start: 
            raise ValueError('the end of the range cannot be smaller than the start')
        generate_squares = [i**2 for i in range(start, end+1)]