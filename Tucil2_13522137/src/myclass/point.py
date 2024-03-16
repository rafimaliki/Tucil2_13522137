''' File : point.py
defition for class Point
'''

from typing import List

class Point:

    # Constructor
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    # Print formatter
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    # Method
    def midpoint(self, other: 'Point') -> 'Point':
        '''
        Calculate the midpoint between two points

        Parameters: 
        - self (Point)
        - other (Point)

        Output:
        - Point
        '''
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)
    
    # Static method
    def get_extreme_point(points: List['Point']) -> List[float]:
        '''
        Finding the extreme values from a list of Point objects
        
        Parameters:
        - points (List[Point]): A list of points 
        
        Output:
        - List[float]: A list with length of 2 representing extreme values for all points'''

        x = []
        y = []

        for p in points:
            x.append(p.x)
            y.append(p.y)

        return [min(min(x), min(y)), max(max(x), max(y))]