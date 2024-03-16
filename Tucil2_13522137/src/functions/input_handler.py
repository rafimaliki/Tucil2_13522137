''' File : input_handler.py
Functions and procedures related to CLI input handling
'''

from myclass.point import Point
from typing import List


''' Function
Number of points input handler function

Parameters: 
- None
Output: 
- int : degree of the Bézier Curve
'''
def input_num_control() -> int:

    print()

    while True:
        user_input = input("Banyak titik: ")
        if '.' in user_input:
            print("ERROR! input harus integer.\n")
            continue  
        try:
            num_control = int(user_input)
            if num_control <= 1:
                print("ERROR! input harus integer di atas 1.\n")
                continue
            break
        except ValueError:
            print("ERROR! input harus integer.\n")
    return num_control


''' Function
Points input handler function

Parameters: 
- num_control (int) : degree of the Bézier Curve
Output:
- List[Point] : List of Point objects
'''
def input_points(num_control: int) -> List[Point]:


    print("\nMasukkan titik dengan format <x, y>")
    print("Contoh: 0 1\n")

    points = []
    for i in range(num_control):
        while True:
            user_input = input(f"Titik ke-{i+1}: ").split()
            if len(user_input) != 2:
                print("ERROR! titik tidak valid.\n")
                continue
            try:
                point = Point(user_input[0], user_input[1])
                points.append(point)
                break
            except ValueError:
                print("ERROR! titik tidak valid.\n")
    return points


''' Function
Number of iterations input handler function

Parameters: 
- None
Output: 
- int : number of iterations
'''
def input_iterations() -> int:

    print()

    while True:
        user_input = input("Banyak iterasi: ")
        if '.' in user_input:
            print("ERROR! input harus integer.\n")
            continue  
        try:
            iterations = int(user_input)
            if iterations <= 0:
                print("ERROR! input harus integer di atas 0.\n")
                continue
            break
        except ValueError:
            print("ERROR! input harus integer.\n")
    return iterations


''' Function
Iteration index showed input handler function

Parameters: 
- None
Output: 
- int : number of iterations
'''
def input_show_iterations(max: int) -> int:

    while True:
        user_input = input("Iterasi: ")
        if '.' in user_input:
            print("ERROR! input harus integer.\n")
            continue  
        try:
            iteration = int(user_input)
            if iteration < -1 or iteration > max:
                print("ERROR! input diluar range.\n")
                continue
            break
        except ValueError:
            print("ERROR! input harus integer.\n")
    return iteration