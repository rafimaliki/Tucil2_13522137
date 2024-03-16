''' File: main.py
'''

from functions.render import *
from functions.bezier_dnc import *
from functions.bezier_bf import *
from functions.input_handler import *
import matplotlib.pyplot as plt
import time, sys

# Create a figure and axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.5)) 

# Label the axes
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')

ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')

# Label the window
plt.get_current_fig_manager().set_window_title('Bézier Curve - 13522137')

# User input handler
num_control = input_num_control()
points = input_points(num_control)
iterations = input_iterations()

# Initializations
builder = points.copy() # A list of points on the Bézier curve with its relative controlers
control_points = points.copy() # A list of Bézier curve's controler points
extreme_point = Point.get_extreme_point(points)

# Initialize nth iteration points with 0th iteration points
nth_iteration_points_dnc = [[control_points[0], control_points[num_control-1]]]
nth_iteration_points_bf = [[control_points[0], control_points[num_control-1]]]

# Delay for each iterations rendering
delay = 1


''' Bezier calculations using divide and conquer '''

succeses_iterations = 0
start_time = time.time()

for i in range(1, iterations+1):

    ''' Bezier calculations with iteration, able to handle larger iterations '''

    temp_builder = [builder[0]]

    for j in range(0, len(builder)-1, num_control-1):

        partial_builder = calc_bezier_dnc(builder[j:j+num_control], num_control)
        temp_builder.extend(partial_builder[1:])
    
    builder = temp_builder
    points = get_points(builder, num_control)
    nth_iteration_points_dnc.append(points)

    succeses_iterations += 1

  
    ''' Bezier calculations with recursion, prone to RecursionError '''

    # try:
    #     builder = calc_bezier_dnc(builder, num_control)
    #     points = get_points(builder, num_control)
    #     nth_iteration_points.append(points)

    #     succeses_iterations += 1

    # except RecursionError:
    #     print(f"\nTerjadi RecursionError pada iterasi ke-{i}. Terlalu banyak kontroler point ({len(builder)} elemen).")
    #     break

calc_time_dnc = round((time.time()-start_time)*1000)

''' End of Bezier calculations using divide and conquer '''


''' Bezier calculations using bruteforce '''

start_time = time.time()

for i in range(1, iterations+1):
    nth_iteration_points_bf.append(calc_bezier_bf(control_points, num_control, i))

calc_time_bf = round((time.time()-start_time)*1000)

''' End of Bezier calculations using bruteforce '''


print("\nSelesai! ")
print(f"Waktu kalkulasi dnc : {calc_time_dnc}ms")
print(f"Waktu kalkulasi bf  : {calc_time_bf}ms")

# Render result with delay for each iterations
animate_points(fig, ax1, ax2, extreme_point, nth_iteration_points_dnc, nth_iteration_points_bf, control_points, delay)

print(f"\nPilih iterasi (0-{succeses_iterations}) atau (-1) untuk exit: \n")
while True:

    show = input_show_iterations(succeses_iterations)

    if (show == -1):
        print("\nEXIT!\n")
        sys.exit()
    else:
        draw_graph(fig, ax1, ax2, extreme_point, nth_iteration_points_dnc[show], nth_iteration_points_bf[show], control_points, show)
        

# Show the plot
plt.show()