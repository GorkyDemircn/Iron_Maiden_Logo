import turtle as tur

def call_background(scr):
    scr.bgpic('Add the path of the image:')
    
def screen_adjustment():
    scr = tur.Screen()
    scr.bgcolor('black')
    tur.title('Iron Maiden')
    tur.speed(6)
    tur.penup()
    tur.shape("turtle")
    tur.goto(-650, 100)
    tur.pen(pencolor='Gold', fillcolor='' , pensize=4)
    
    #Displaying the screen at the front.
    rootwindow = scr.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
    #Displaying the screen at the front.
    
    #To make the screen fullscreen.
    screenTk = scr.getcanvas().winfo_toplevel()
    screenTk.attributes("-fullscreen", True)
    #To make the screen fullscreen.
    
    tur.pendown()  
    return scr
    
def letter_i():
    tur.begin_fill()
    tur.fd(20)
    tur.rt(90)
    tur.fd(150)
    tur.lt(-90)
    tur.fd(20)
    tur.rt(90)
    tur.fd(150)
    tur.end_fill()
    
def letter_r():
    tur.penup()
    tur.goto(-610, 98)
    tur.pendown()
    tur.begin_fill()
    tur.rt(90)
    tur.fd(20)
    tur.rt(90)
    tur.fd(10)
    tur.rt(-130)
    tur.fd(30)
    tur.rt(90)
    tur.fd(75)
    tur.lt(-90)
    tur.fd(38)
    tur.lt(95)
    tur.fd(78)
    tur.lt(-90)
    tur.fd(20)
    tur.rt(90)
    tur.fd(120)
    tur.rt(225)
    tur.fd(90)
    tur.rt(90)
    tur.fd(20)
    tur.rt(90)
    tur.fd(145.6)
    tur.end_fill()
    
def letter_r_inside():
    tur.penup()
    tur.goto(-585, 60)
    tur.pendown()
    tur.begin_fill()
    tur.rt(50.2)
    tur.fd(22)
    tur.rt(75.2)
    tur.fd(26)
    tur.rt(144.5)
    tur.fd(36)
    
    tur.end_fill()
    
def letter_o():
    tur.penup()
    tur.goto(-450, 98)
    tur.pendown()
    tur.begin_fill()
    tur.rt(-45)
    tur.fd(105)
    tur.rt(-90.5)
    tur.fd(50)
    tur.rt(-45)
    tur.fd(70)
    tur.rt(-44.5)
    tur.fd(50)
    tur.rt(-86.5)
    tur.fd(98)
    tur.end_fill()
    
def letter_o_inside():
    tur.penup()
    tur.goto(-452, 78)
    tur.pendown()
    tur.begin_fill()
    tur.rt(-93.5)
    tur.fd(75)
    tur.rt(-90)
    tur.fd(30)
    tur.lt(45)
    tur.fd(60)
    tur.rt(-45)
    tur.fd(30)
    tur.rt(-88)
    tur.fd(73)
  
    tur.end_fill()
    
def letter_n():
    tur.penup()
    tur.goto(-372, 98)
    tur.pendown()
    tur.begin_fill()
    tur.rt(133.5)
    tur.fd(20)
    tur.rt(62.5)
    tur.fd(40)
    tur.rt(-152.5)
    tur.fd(35)
    tur.rt(90)
    tur.fd(20)
    tur.rt(89.7)
    tur.fd(170)
    tur.rt(145.5)
    tur.fd(35)
    tur.rt(34.5)
    tur.fd(35)
    tur.lt(35)
    tur.fd(35)
    tur.lt(144.5)
    tur.fd(50)
    tur.rt(90.5)
    tur.fd(20)
    tur.rt(88.8)
    tur.fd(109)
    tur.rt(-53.5)
    tur.fd(32)
    tur.rt(144.5)
    tur.fd(30)
    
    tur.end_fill()
    
def letter_m():
    tur.penup()
    tur.goto(330, 98)
    tur.pendown()
    tur.begin_fill()
    tur.rt(0)
    tur.fd(20)
    tur.rt(62.5)
    tur.fd(25)
    tur.rt(-120.5)
    tur.fd(25.5)
    tur.rt(98.5)
    tur.fd(20)
    tur.rt(48.5)
    tur.fd(170)
    tur.rt(145.5)
    tur.fd(35)
    tur.rt(34.5)
    tur.fd(70)
    tur.rt(-145.5)
    tur.fd(25.5)
    tur.rt(120.5)
    tur.fd(25.5)
    tur.rt(-154.5)
    tur.fd(70)
    tur.rt(89.5)
    tur.fd(20)
    tur.rt(90.2)
    tur.fd(134.5)
    tur.rt(-53.5)
    tur.fd(32)
    tur.rt(143.5)
    tur.fd(35)
    
    tur.end_fill()
    
def letter_a():
    tur.penup()
    tur.goto(425, 82)
    tur.pendown()
    tur.begin_fill()
    tur.rt(30)
    tur.fd(20)
    tur.rt(-90)
    tur.fd(30)
    tur.lt(-60.5)
    tur.fd(25)
    tur.rt(89.5)
    tur.fd(120)
    tur.lt(-90.5)
    tur.fd(25)
    tur.lt(-65.5)
    tur.fd(35)
    tur.rt(-130.5)
    tur.fd(35)
    tur.rt(120)
    tur.fd(20)
    tur.rt(58.5)
    tur.fd(25)
    tur.lt(75.5)
    tur.fd(25)
    tur.rt(71.8)
    tur.fd(48.5)
    
    
    tur.end_fill()
    
def letter_a_inside():
    tur.penup()
    tur.goto(465, 60)
    tur.pendown()
    tur.begin_fill()
    tur.rt(160.2)
    tur.fd(36)
    tur.rt(140.5)
    tur.fd(23)
    tur.rt(73.5)
    tur.fd(22)
    
    tur.end_fill()
    
def letter_i_right():
    tur.penup()
    tur.goto(495, 98)
    tur.pendown()
    tur.begin_fill()
    tur.rt(55.5)
    tur.fd(20)
    tur.rt(90)
    tur.fd(150)
    tur.lt(-90)
    tur.fd(20)
    tur.rt(90)
    tur.fd(150)
    
    tur.end_fill()
    
def letter_d():
    tur.penup()
    tur.goto(540, 98)
    tur.pendown()
    tur.begin_fill()
    tur.rt(90)
    tur.fd(20)
    tur.rt(65.5)
    tur.fd(120)
    tur.rt(80.4) #78.5
    tur.fd(70)
    tur.setheading(180)
    tur.heading()
    tur.fd(20)
    tur.rt(90)
    tur.fd(148)
    tur.setheading(0)
    tur.heading()
    tur.fd(10)
    tur.end_fill()
    tur.setheading(-90)
    tur.heading()
    
    tur.end_fill()
    
def letter_d_inside():
    tur.penup()
    tur.goto(542, 85)
    tur.pendown()
    tur.begin_fill()
    tur.fd(120)
    tur.lt(90)
    tur.fd(10)
    tur.lt(35.5)
    tur.fd(50)
    tur.rt(-78.5)
    tur.fd(100)
    tur.setheading(180)
    tur.heading()
    tur.fd(8)
    tur.end_fill()
    tur.setheading(0)
    tur.heading()
    
def letter_e():
    tur.penup()
    tur.goto(650, 98)
    tur.pendown()
    tur.begin_fill()
    tur.fd(40)
    tur.rt(90)
    tur.fd(20)
    tur.rt(90)
    tur.fd(40)
    tur.lt(90)
    tur.fd(40)
    tur.lt(90)
    tur.fd(40)
    tur.rt(90)
    tur.fd(20)
    tur.rt(90)
    tur.fd(40)
    tur.lt(90)
    tur.fd(50)
    tur.lt(90)
    tur.fd(40)
    tur.rt(90)
    tur.fd(20)
    tur.rt(90)
    tur.fd(40)
    tur.rt(45.8)
    tur.fd(32)
    tur.setheading(90)
    tur.heading()
    tur.fd(127)
    tur.setheading(0)
    tur.heading()
    tur.fd(30)
    tur.end_fill()
    tur.setheading(0)
    tur.heading()
    
def letter_n_right():
    tur.penup()
    tur.goto(735, 98)
    tur.pendown()
    tur.begin_fill()
    
    tur.fd(20)
    tur.rt(60.5)
    tur.fd(40)
    tur.rt(-150.5)
    tur.fd(35)
    tur.rt(90)
    tur.fd(20)
    tur.rt(89.9)
    tur.fd(170)
    tur.rt(145.5)
    tur.fd(35)
    tur.rt(34.5)
    tur.fd(35)
    tur.lt(35)
    tur.fd(35)
    tur.lt(144.5)
    tur.fd(50)
    tur.rt(90.5)
    tur.fd(20)
    tur.rt(89.5)
    tur.fd(109)
    tur.rt(-53.5)
    tur.fd(30.9)
    tur.rt(144.5)
    tur.fd(26)
    
    tur.end_fill()
    tur.setheading(0)
    tur.heading()
    
def call_all_functions():
    screen_adjustment()
    letter_i()
    letter_r()
    letter_r_inside()
    letter_o()
    letter_o_inside()
    letter_n()
    call_background(screen_adjustment())
    letter_m()
    letter_a()
    letter_a_inside()  
    letter_i_right()
    letter_d()
    letter_d_inside()
    letter_e()
    letter_n_right()
            
call_all_functions()
tur.hideturtle()
tur.exitonclick()
