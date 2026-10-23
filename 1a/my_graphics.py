import turtle

def draw_sun(t, x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(1)
    t.pendown()
    t.color("orange", "yellow")
    t.begin_fill()
    #for _ in range(18):
      #  t.forward(80)
      #  t.left(100)
   # t.end_fill()
    for i in range(36):
        t.forward(150)
        t.left(170)
    t.end_fill()

def draw_wav(t, x, y, color):
    t.penup()
    t.goto(x, y)
    t.setheading(-90)
    t.color(color)
    t.width(3)
    t.pendown()
    for _ in range(20):
        t.circle(40, 180)
        t.left(180)
def draw_waves(t, x, y, color):
    t.up()
    t.goto(x, y)
    t.setheading(-45)
    t.color(color)
    t.down()
    for _ in range(18):
        t.circle(20, 90)
        t.circle(-20, 90)
def draw_bird(t, x, y, size=1.0, color="black"):
    t.penup()
    t.goto(x, y)
    t.setheading(60) # Повертаємо голову вгору для початку крила
    t.color(color)
    t.pendown()
    
    # Ліве крило (дуга)
    t.circle(-50 * size, 120)
    
    # Праве крило (дуга в інший бік)
    t.setheading(120)
    t.circle(-50 * size, 120)
    
    t.hideturtle()
def draw_custom_ship(t, x, y, size=1.0, p_color="orange"):
    # Тіло корабля (завжди коричневе)
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.color("brown")
    t.pendown()
    t.begin_fill()
    t.forward(200 * size)
    t.goto(x + 170 * size, y - 40 * size)
    t.goto(x + 30 * size, y - 40 * size)
    t.goto(x, y)
    t.end_fill()
    
    # Щогла
    t.penup()
    t.goto(x + 100 * size, y)
    t.pendown()
    t.goto(x + 100 * size, y + 200 * size)
    
    # ПАРУС (тепер колір залежить від нашої змінної p_color)
    t.color(p_color) 
    t.begin_fill()
    t.goto(x + 200 * size, y + 20 * size)
    t.goto(x + 100 * size, y + 20 * size)
    t.goto(x + 100 * size, y + 200 * size)
    t.end_fill()
def draw_whale(t, x, y, size=1.0, color="blue"):
    t.penup()
    t.goto(x, y)
    t.setheading(-90)  
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    
    t.begin_fill()
    # 1. Тіло (радіус множимо на size)
    t.circle(80 * size, -180) 
    
    # 2. Живіт (довжину множимо на size)
    t.left(90)
    t.forward(160 * size) 
    t.end_fill()
    
    # 3. Хвіст (координати точок теж множимо на size)
    t.penup()
    t.goto(x + 160 * size, y) 
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.goto(x + 190 * size, y + 30 * size)
    t.goto(x + 190 * size, y - 30 * size)
    t.goto(x + 160 * size, y)
    t.end_fill()
    
    # 4. Око (зміщення ока теж залежить від розміру)
    t.penup()
    t.goto(x + 30 * size, y + 45 * size)
    t.dot(12 * size, "white") 
    t.dot(6 * size, "black")  
    t.hideturtle()

