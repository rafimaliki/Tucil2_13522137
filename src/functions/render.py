''' File : render.py
Functions and procedures related to matplotlib
'''

from myclass.point import Point
from typing import List
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure


''' Procedure
Rendering points on plot

Parameters: 
- points (List[Point]) : A list of Point objects
- color (String)       : color and shape of point
'''
def render_points(ax: Axes, points: List[Point], color: str):

    for point in points:
        ax.plot(point.x, point.y, color)  
        ax.annotate(f'({point.x:.1f}, {point.y:.1f})', 
                    xy=(point.x, point.y),  
                    xytext=(10, 10),  
                    textcoords='offset pixels',
                    fontsize=7)


''' Procedure
Rendering lines on plot connecting two adjecent points on the list

Parameters: 
- points (List[Point]) : A list of Point objects
- color (String)       : color and type of lines
'''
def render_lines(ax: Axes, points: List[Point], color: str):

    for i in range(len(points) - 1):
        ax.plot([points[i].x, points[i + 1].x], [points[i].y, points[i + 1].y], color) 


''' Procedure
Draw graph on the plot

Parameters:  
- fig (Figure)                             : The Figure object to render axes on
- ax1, ax2 (Axes)                          : The AxesSubplot object to render points/lines on
- extreme (List[float])                    : A list of float representing extreme values
- points_dc, points_bf (List[List[Point]]) : A list of list of Point objects
- control_points (list[Point])             : A list of Point objects
- iter (int)                               : iteration number
'''
def draw_graph(fig: Figure, ax1: Axes, ax2: Axes, extreme: List[float], points_dnc: List[Point], points_bf: List[Point], control_points: List[Point], iter: int):
    # Warning if too many points
    if iter > 10:
        print(f"WARNING! Terlalu banyak titik ({len(points_dnc)}), matplotlib mungkin akan freeze")

    # Clear the plot
    ax1.cla()
    ax2.cla()

    plt.draw()

    fig.suptitle(f"Iterasi ke-{iter}")

    # Set plot title
    ax1.set_title(f"Divide and Conquer")
    ax2.set_title(f"Bruteforce")

    # Set axis view limit
    ax1.set_xlim(round(extreme[0]-1), round(extreme[1]+1))  
    ax1.set_ylim(round(extreme[0]-1), round(extreme[1]+1)) 

    ax2.set_xlim(round(extreme[0]-1), round(extreme[1]+1))  
    ax2.set_ylim(round(extreme[0]-1), round(extreme[1]+1)) 

    # Render control points
    render_lines(ax1, control_points, "b--")
    render_points(ax1, control_points, "bs")

    render_lines(ax2, control_points, "b--")
    render_points(ax2, control_points, "bs")

    # Render lines that builds the curve
    render_lines(ax1, points_dnc, "r-") 
    render_lines(ax2, points_bf, "r-") 


''' Procedure
Animate drawing graph from each iteration

Parameters:  
- fig (Figure)                             : The Figure object to render axes on
- ax1, ax2 (Axes)                          : The AxesSubplot object to render points/lines on
- extreme (List[float])                    : A list of float representing extreme values
- points_dc, points_bf (List[List[Point]]) : A list of list of Point objects
- control_points (list[Point])             : A list of Point objects
- delay (float)                            : delay time
'''
def animate_points(fig: Figure, ax1: Axes, ax2: Axes, extreme: List[float], points_dnc: List[List[Point]], points_bf: List[List[Point]], control_points: List[Point], delay: float):

    print("\nMenampilkan graf..")

    for i in range(len(points_dnc)):

        draw_graph(fig, ax1, ax2, extreme, points_dnc[i], points_bf[i], control_points, i)

        plt.pause(delay)
