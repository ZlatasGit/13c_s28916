from .square_generator import SquareGenerator
# task 8. Inheritance
class CubicGenerator(SquareGenerator):
    
    def squares_of_range(start, end):
        if end<=start: 
            return ValueError('the end of the range cannot be smaller than the start')
        return [i**3 for i in range(start, end+1)]
