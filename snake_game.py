import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Skjermoppsett
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")  # Endret bakgrunnsfarge til svart for mer moderne følelse
window.setup(width=600, height=600)
window.tracer(0)

# Slangehode
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lime")  # Endret farge til en mer moderne grønn
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Mat
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")  # Endret fargen på maten til rød
food.penup()
food.goto(0, 100)

segments = []

# Pen (Score display)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")  # Fargen på score display er satt til hvit
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Funksjoner for at hodet skal bevege seg
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

# Funksjoner for å endre retning
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

# Funksjon for å håndtere lukking av vinduet
def on_close():
    turtle.bye()

window._root.protocol("WM_DELETE_WINDOW", on_close)

# Tastaturkontroller
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

# Start funksjon for å starte spillet på nytt
def start_game():
    global score, high_score
    score = 0
    high_score = 0
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "bold"))

# Vise startmelding
pen.clear()
pen.write("Press any key to start!", align="center", font=("Arial", 24, "bold"))
window.listen()
window.onkeypress(start_game, "space")

# Hoved spillets løkke
while True:
    try:
        window.update()

        # Sjekker om slangen treffer rammen på skjermen
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)  # Flytt segmentene utenfor skjermen
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "normal"))

        # Sjekker når slangen treffer maten
        if head.distance(food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            # Legger til et nytt segment når slangen spiser maten
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

            delay = max(0.05, delay - 0.001)  # Reduserer delayen for å gjøre spillet raskere

            score += 10
            if score > high_score:
                high_score = score

            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "normal"))

        # Beveger segmentene bakover i rekkefølge
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        # Sjekker om slangen krasjer med seg selv
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                for segment in segments:
                    segment.goto(1000, 1000)  # Flytt segmentene utenfor skjermen
                segments.clear()
                score = 0
                delay = 0.1
                pen.clear()
                pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "normal"))

        time.sleep(delay)

    except turtle.Terminator:
        break

window.mainloop()
