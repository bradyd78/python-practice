from turtle import Screen, Turtle
from random import randint

# Grid and boundary setup
GRID_SIZE = 22
BOUNDARY = GRID_SIZE * 8

# Screen setup
screen = Screen()
screen.bgcolor("green")
screen.title("1 Minute Snake Game")
screen.tracer(0)

# Draw boundary
border = Turtle()
border.hideturtle()
border.speed(0)
border.color("white")
border.pensize(5)
border.up()
border.goto(-BOUNDARY, BOUNDARY)
border.down()
for _ in range(4):
    border.forward(BOUNDARY * 2)
    border.right(90)

# Food setup
food = Turtle()
food.shape("circle")
food.color("red")
food.up()
food.speed(0)

def place_food():
    x = randint(-BOUNDARY + GRID_SIZE, BOUNDARY - GRID_SIZE) // GRID_SIZE * GRID_SIZE
    y = randint(-BOUNDARY + GRID_SIZE, BOUNDARY - GRID_SIZE) // GRID_SIZE * GRID_SIZE
    food.goto(x, y)

place_food()

# Score display
score = 0
score_display = Turtle()
score_display.hideturtle()
score_display.up()
score_display.color("white")
score_display.goto(0, BOUNDARY + 20)
score_display.write(f"Score: {score}", align="center", font=("Arial", 20, "bold"))

# Snake setup
snake = []
head = Turtle()
head.shape("square")
head.color("cyan")
head.up()
head.speed(0)
snake.append(head)

for i in range(2):
    body = head.clone()
    body.color("white")
    body.goto(head.xcor() + (i + 1) * GRID_SIZE, head.ycor())
    snake.append(body)

# Movement direction
direction = [-1, 0]  # Initially moving left

# Movement function
def move():
    global score
    screen.update()

    # Move snake
    last = snake.pop()
    first = snake[0]
    first.color("white")
    last.goto(first.xcor() + direction[0] * GRID_SIZE, first.ycor() + direction[1] * GRID_SIZE)
    last.color("cyan")
    snake.insert(0, last)

    # Check food collision
    if snake[0].distance(food) < GRID_SIZE:
        place_food()
        new_segment = snake[-1].clone()
        new_segment.color("white")
        snake.append(new_segment)
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 20, "bold"))

    # Check wall collision
    if not (-BOUNDARY < snake[0].xcor() < BOUNDARY and -BOUNDARY < snake[0].ycor() < BOUNDARY):
        score_display.goto(0, 0)
        score_display.write("Game Over!", align="center", font=("Arial", 24, "bold"))
        return

    screen.ontimer(move, 150)

# Direction controls
def up():
    global direction
    if direction[1] != -1:
        direction = [0, 1]

def down():
    global direction
    if direction[1] != 1:
        direction = [0, -1]

def left():
    global direction
    if direction[0] != 1:
        direction = [-1, 0]

def right():
    global direction
    if direction[0] != -1:
        direction = [1, 0]

# Key bindings
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

# Start game
move()
screen.mainloop()
