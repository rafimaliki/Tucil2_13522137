''' File : bezier_bf.py
Functions and procedures related to calculating Bézier curve using brute force method
'''

from myclass.point import Point
from typing import List
import math

''' Function
Counting how many points on the Bézier curve will be generated on the nth iteration

Parameters: 
- iter (int) : The iteration number

Output:
- int : The number of points on the Bézier curve
'''
def count_points(iter: int) -> int:

    if iter == 0:
        return 2
    else:
        return 2*count_points(iter-1) - 1
    

''' Function
Calculate the Bernstein polynomial

Parameters: 
- i (int)   : The i-th control point
- n (int)   : The number of control points
- t (float) : The t value

Output:
- float : The value of the Bernstein polynomial
'''
def bernstein_polynomial(i: int, n: int, t: float) -> float:
    
    return math.comb(n, i) * (t**i) * ((1-t)**(n-i))


'''
Calculate new points on Bézier's curve using brute force method

Parameters: 
- points (List[Point]) : A list of Point objects representing control points
- num_control (int)    : Number of control points
- iter (int)           : The iteration number

Output:
- List[Point] : A list of points on the Bézier curve
'''
def calc_bezier_bf(points: List[Point], num_control: int, iter: int) -> List[Point]:

    result = []
    num_points = count_points(iter)

    for t in range(num_points):

        x = 0
        y = 0
        
        for i in range(num_control):
            x += points[i].x * bernstein_polynomial(i, num_control-1, t/(num_points-1))
            y += points[i].y * bernstein_polynomial(i, num_control-1, t/(num_points-1))

        result.append(Point(x, y))

    return result


