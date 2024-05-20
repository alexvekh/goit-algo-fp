"""Завдання 2. Рекурсія. 
Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. 
Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.

"""

import turtle
import argparse

def koch_curve(t, level, size):
    if level == 0:
        t.pensize(3)
        t.color('green')
        t.forward(size)
        t.left(180)
        t.forward(size)
        t.home
    else:
        t.color('red')
        t.forward(size)
        t.left(45)
        koch_curve(t, level - 1, size * 0.75 )
        t.left(90)
        koch_curve(t, level - 1, size * 0.75 )
        t.left(45)
        t.forward(size)

            



def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("skyblue")

    t = turtle.Turtle()
    t.pencolor("green")
    t.speed(0)
    t.penup()
    t.goto(0, -size)
    t.left(90)
    t.pendown()

   
    koch_curve(t, order, size/1.7)
    # t.right(120)

    window.mainloop()

# draw_koch_curve(7)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Recursion level')
  parser.add_argument('recursion_level', nargs='?', help='Recursion level')
  args = parser.parse_args()
  print(args)
  recursion_level = args.recursion_level
  if recursion_level:
    recursion_level = int(recursion_level)
  else:
    print("Увага!.")
    print("Буде промальовано дерево Піфагора.")
    recursion_level = int(input("Який ви бажаєте рівень рекурсії? "))

  draw_koch_curve(recursion_level)
