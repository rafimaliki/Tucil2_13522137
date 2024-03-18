''' File : bezier_dnc.py
Functions and procedures related to calculating Bézier curve using divide and conquer method
'''

from myclass.point import Point
from typing import List


''' Function
Removing controler points from List of points

Parameters: 
- points (List[Point]) : A list of points on the Bézier curve with its relative controlers
- num_control (int)    : Number of control points

Output:
- List[Point] : A list of points on the Bézier curve
'''
def get_points(points: List[Point], num_control: int) -> List[Point]:
    
    temp = []
    for i in range(len(points)):
        if i % (num_control-1) == 0:
            temp.append(points[i])

    return temp


''' Function
Calculate new points on Bézier's curve using mid point method

Parameters: 
- points (List[Point]) : A list of Point objects representing control points
- num_control (int)    : Number of control points

Output:
- List[Point] : A list of points on the Bézier curve with its relative controlers
'''
def calc_bezier_dnc(points: List[Point], num_control: int) -> List[Point]:

    mid_points = []
    result = []

    if len(points) > num_control:

        left = points[0:num_control]
        right = points[num_control-1:len(points)]

        result = calc_bezier_dnc(left, num_control)[:-1] + calc_bezier_dnc(right, num_control)

    else:

        if len(points) == 1:
            result = points

        else:
            for i in range(num_control-1):

                mid = points[i].midpoint(points[i+1])
                mid_points.append(mid)

            inner = calc_bezier_dnc(mid_points, num_control-1)
            result = [points[0]] + inner + [points[num_control-1]]

    return result
    