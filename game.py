import turtle
import random

t = turtle.Turtle()
e = turtle.Turtle()
l = turtle.Turtle()

e.color("red")
l.color("blue")

print("Race the red turtle and reach the finish line first.")
l.up()
l.left(90)
l.forward(250)
l.down()
l.right(90)
l.forward(400)
l.backward(800)
t.up()
t.backward(50)
t.down()
t.left(90)
e.left(90)

def collision():
  if abs(t.xcor() - e.xcor()) < 20:
    if abs(t.ycor() - e.ycor()) < 20:
      print("collision")

def check_win():
  if t.ycor() > l.ycor():
    print("You won")
    repeat=input("Would you like to try again?")
    if repeat == "yes":
      print("Continue game")

    else:
      print("Thank you for playing")

  elif e.ycor() > l.ycor():
    print("You lost. Try again")
    repeat=input("Would you like to try again?")
    if repeat == "yes":
      print("Continue game")
      
    else:
      print("Thank you for playing")

def move_enemy():
  e.forward(random.randint(0, 50))

while True:
  check_win()
  
  movement = input("Enter WASD to move or enter quit to quit game: ")
  speed=random.randint(0,50)
  if movement == "W":
    t.forward(speed)

  elif movement == "S":
    t.backward(speed)

  elif movement == "A":
    t.left(90)

  elif movement == "D":
    t.right(90)

  elif movement == "quit":
    break
    
  else:
    print("Invalid input.")

  move_enemy()
  collision()

  print(t.xcor(), t.ycor())

print("Thank you for playing this game.")