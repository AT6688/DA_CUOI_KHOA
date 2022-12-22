import turtle
import time
import random

delay = 0.1

# ghi diem
score = 0
high_score = 0
food_count = 0

# khoi tao cua so
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("#B0E0E6")
wn.setup(width=700, height=700)
wn.tracer(0)

# tao tuong bao
wall = turtle.Turtle()
wall.speed(10)
wall.pensize(10)
wall.penup()
wall.goto(-300,300)
wall.pendown()
wall.color("#800000")
wall.forward(600)
wall.right(90)
wall.forward(600)
wall.right(90)
wall.forward(600)
wall.right(90)
wall.forward(600)
wall.right(90)
wall.hideturtle()

# tao dau ran
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("#191970")
head.penup()
head.goto(0,0)
head.direction = "stop"

# moi an
food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("blue")
food.penup()
food.goto(0,100)

# moi thuong
special_food = turtle.Turtle()
special_food.speed(0)
special_food.shape("circle")
special_food.color("red")
special_food.penup()
special_food.goto(1000,1000)

body = []

# But ve diem
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,310)
pen.write("Score: 0 High Score: 0", align = "center", font=("Courier",24,"normal"))

# di chuyen huong
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
    
# keyboard binding
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")
    
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+15)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-15)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-15)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+15)
        
        
# main game loop

while True:
    wn.update()
    
    # kiem tra dau ran co va cham vao tuong khong?
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        # an phan than ran
        for i in body:
            i.goto(1000,1000)
        # xoa bo than ran
        body.clear()
        
        # reset diem so
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score),align = "center", 
                  font=("Courier",24,"normal"))
        
    # khi ran an cham den moi
    if head.distance(food) < 20: # di chuyen moi den vi tri ngau nhien
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        food_count +=1
        
        # tao phan than moi
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("circle")
        new_body.color("#008000")
        new_body.penup()
        body.append(new_body)     
                                                            
        # cong diem
        score += 1
        
        if score > high_score:
            high_score = score
            
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score),align = "center", 
                  font=("Courier",24,"normal"))
        
    if food_count == 5:
        x1 = random.randint(-290,290)
        y1 = random.randint(-290,290)
        special_food.goto(x1,y1)
        food_count = 0
        
    if head.distance(special_food) < 20:
        special_food.goto(1000,1000)        
        score += 5
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score),align = "center", 
                  font=("Courier",24,"normal"))
                                                         
    # di chuyen phan duoi cuoi cung truoc theo thu tu nguoc
    for index in range(len(body)-1, 0, -1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x,y)
        
    # di chuyen cai gan dau ran vao vi tri dau ran
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)
        
    move()
    
    # kiem tra dau ran co dam vao body khong?
    for i in body:
        if i.distance(head) < 15:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            for j in body:
                j.goto(1000,1000)
        
            body.clear()
        
            score = 0

            delay = 0.1

            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score),align = "center", 
                      font=("Courier",24,"normal"))
    
    time.sleep(delay)

wn.mainloop()