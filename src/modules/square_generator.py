# task 3. Create a class called SquareGenerator that has a method to generate squares for a given range of numbers.
# task 5. Handle the case where the end of the range is less than the start in the SquareGenerator class.
# task 6. Extract the SquareGenerator class into a separate module named square_generator.py.
# task 10. 
import abc


class SquareGenerator(abc.ABC):
    @abc.abstractmethod
    def squares_of_range(start, end):
        if end<=start: 
            return ValueError('the end of the range cannot be smaller than the start')
        return [i**2 for i in range(start, end+1)]