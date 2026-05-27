import turtle
import time
import random

# ================= SCREEN SETUP =================
wn = turtle.Screen()
wn.title("🔥 Advanced Snake Game")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

# ================= BORDER =================
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-350, -350)
border.pensize(5)
border.pendown()

for _ in range(4):
    border.forward(700)
    border.left(90)

border.hideturtle()

# ================= SNAKE HEAD =================
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lime")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# ================= FOOD =================
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# ================= SCORE BOARD =================
score = 0
high_score = 0
level = 1
delay = 0.1

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)

pen.write(
    f"Score: {score}   High Score: {high_score}   Level: {level}",
    align="center",
    font=("Arial", 20, "bold")
)

# ================= SNAKE BODY =================
segments = []

# ================= MOVEMENT FUNCTIONS =================
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# ================= KEYBOARD CONTROLS =================
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# ================= GAME LOOP =================
while True:

    wn.update()

    # ===== BORDER COLLISION =====
    if (
        head.xcor() > 340 or
        head.xcor() < -340 or
        head.ycor() > 340 or
        head.ycor() < -340
    ):

        time.sleep(1)

        head.goto(0, 0)
        head.direction = "Stop"

        # Remove body
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        delay = 0.1
        score = 0
        level = 1

        pen.clear()
        pen.write(
            f"Score: {score}   High Score: {high_score}   Level: {level}",
            align="center",
            font=("Arial", 20, "bold")
        )

    # ===== FOOD COLLISION =====
    if head.distance(food) < 20:

        # Move food
        x = random.randint(-320, 320)
        y = random.randint(-320, 320)
        food.goto(x, y)

        # Add new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")

        # Random body color
        colors = ["green", "yellow", "cyan", "orange"]
        new_segment.color(random.choice(colors))

        new_segment.penup()
        segments.append(new_segment)

        # Score increase
        score += 10

        # High score update
        if score > high_score:
            high_score = score

        # ===== LEVEL SYSTEM =====
        level = score // 50 + 1

        # Increase speed
        if delay > 0.03:
            delay -= 0.002

        pen.clear()
        pen.write(
            f"Score: {score}   High Score: {high_score}   Level: {level}",
            align="center",
            font=("Arial", 20, "bold")
        )

    # ===== MOVE BODY =====
    for index in range(len(segments)-1, 0, -1):

        x = segments[index-1].xcor()
        y = segments[index-1].ycor()

        segments[index].goto(x, y)

    if len(segments) > 0:

        x = head.xcor()
        y = head.ycor()

        segments[0].goto(x, y)

    move()

    # ===== BODY COLLISION =====
    for segment in segments:

        if segment.distance(head) < 20:

            time.sleep(1)

            head.goto(0, 0)
            head.direction = "Stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score = 0
            level = 1
            delay = 0.1

            pen.clear()
            pen.write(
                f"Score: {score}   High Score: {high_score}   Level: {level}",
                align="center",
                font=("Arial", 20, "bold")
            )

    time.sleep(delay)

wn.mainloop()