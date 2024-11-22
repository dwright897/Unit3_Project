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

Start_length = 100
Min_length= 10
Reduction_length= 1.5
Reduction_thickness= 1.5


t = turtle.Turtle()
t.speed(6)

def draw_branches(length, thickness):
  colors = ("tomato", "dark salmon", "red", "orange", "peru", "wheat")
  t.pencolor("brown")
  num_branch = random.randint(1,2)
  

  random_angle_left = random.randint(Min_angle, Max_angle)
  random_angle_right = random.randint(Min_angle, Max_angle)
  if length < Min_length:
    t.pensize(10)
    t.pencolor(random.choice(colors))
    t.forward(15)
    t.backward(15)
    t.pencolor("brown")
    t.pensize(thickness)
    return
  t.pensize(thickness)
  t.forward(length)
  if num_branch == 2:
    t.left(random_angle_left)
    draw_branches(length / Reduction_length, thickness / Reduction_thickness)

    t.right(random_angle_left + random_angle_right)
    draw_branches(length / Reduction_length, thickness / Reduction_thickness)
    t.left(random_angle_right)

    t.backward(length)

  elif num_branch ==1:
    side = random.randint(1,2)
    if side == 1:
      t.left(random_angle_left)
      draw_branches(length / Reduction_length, thickness / Reduction_thickness)
      t.right(random_angle_left)
      t.backward(length)
    else:
      t.right(random_angle_right)
      draw_branches(length / Reduction_length, thickness / Reduction_thickness)
      t.left(random_angle_right)
      t.backward(length)
  else:
    t.backward(length)
  
    



def draw_tree():
  t.penup()
  t.left(90)
  t.backward(Start_length-30)
  t.pendown()
  draw_branches(Start_length, 20)


def main():
  draw_tree()
  turtle.done()

if __name__=="__main__":
  main()