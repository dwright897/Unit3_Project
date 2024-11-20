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

Max_angle = 30
Min_angle = 10
Angle = 30
Start_length = 50
Min_length= 5
Reduction_length= 1.5
Reduction_thickness= 1.5

t = turtle.Turtle()
t.speed(0)

def draw_branches(length, thickness):
  #random_angle_left = random.randint(Min_angle, Max_angle)
  #random_angle_right = random.randint(Min_angle, Max_angle)
  if length < Min_length:
    return
  #t.pensize(thickness)
  '''if length > Start_length/2:
    t.pencolor("brown")
  else:
    t.pencolor("green")'''
  
  t.forward(length)
  
  t.left(Angle)
  draw_branches(length / Reduction_length, thickness / Reduction_thickness)
  
  #t.right(random_angle_left + random_angle_right)
  t.right(Angle*2)
  draw_branches(length / Reduction_length, thickness / Reduction_thickness)
  t.left(Angle)
  t.backward(length)
  

def draw_tree():
  t.left(90)
  draw_branches(Start_length, 10)


def main():
  draw_tree()
  turtle.done()

if __name__=="__main__":
  main()