import turtle

# Ініціалізація екрану та черепашки
wn = turtle.Screen()
wn.title("Turtle Keyboard Control")
wn.bgcolor("white")

# Створення черепашки
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)


# Функції для переміщення черепашки
def move_right():
    t.setheading(0)  # Встановлюємо напрям вправо (0 градусів)
    t.forward(20)  # Рухаємось вперед на 20 пікселів


def move_left():
    t.setheading(180)  # Встановлюємо напрям вліво (180 градусів)
    t.forward(20)  # Рухаємось вперед на 20 пікселів


def move_up():
    t.setheading(90)  # Встановлюємо напрям вгору (90 градусів)
    t.forward(20)  # Рухаємось вперед на 20 пікселів


def move_down():
    t.setheading(270)  # Встановлюємо напрям вниз (270 градусів)
    t.forward(20)  # Рухаємось вперед на 20 пікселів


# Призначення клавіш-стрілок для функцій
wn.listen()
wn.onkey(move_right, "Right")
wn.onkey(move_left, "Left")
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")

# Основний цикл програми
wn.mainloop()
