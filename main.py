# Dalton Wright
# U3 Project 
# 11/18/24

"""
IMPORTANT
To run your code in this project,
open the Terminal and enter the following:

python main.py    then enter

Your output will be visualized in the 
Virtual Desktop
"""

import turtle
import random

Max_angle = 40
Min_angle = 15
Angle = 30
Start_length = 100
Min_length= 10
Reduction_length= 1.5
Reduction_thickness= 1.5


t = turtle.Turtle()
t.speed(0)

def draw_branches(length, thickness):
  colors = ("tomato", "dark salmon", "red")
  t.pencolor("brown")

  random_angle_left = random.randint(Min_angle, Max_angle)
  random_angle_right = random.randint(Min_angle, Max_angle)
  if length < Min_length:
    t.pensize(7)
    t.pencolor(random.choice(colors))
    t.forward(10)
    t.backward(10)
    t.pencolor("brown")
    # draw
    # backtrack
    # reset pensize
    # reset pencolor
    return
  t.pensize(thickness)
  t.forward(length)
  
  t.left(random_angle_left)
  draw_branches(length / Reduction_length, thickness / Reduction_thickness)
  
  t.right(random_angle_left + random_angle_right)
 
  draw_branches(length / Reduction_length, thickness / Reduction_thickness)
  t.left(random_angle_right)
  
  t.backward(length)
  

def draw_tree():
  t.penup()
  t.left(90)
  t.backward(Start_length)
  t.pendown()
  draw_branches(Start_length, 20)


def main():
  draw_tree()
  turtle.done()

if __name__=="__main__":
  main()