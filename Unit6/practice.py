
#Betsy Sumba
#CFU 15
#1-2

import simplegui
import random

def draw_handler(canvas):
    canvas.draw_polygon([(40, 30), (54, 100),(30, 103)], 5, "black", "black")
    canvas.draw_polygon([(20,112),(120,150),(90,190)],5 , "black","black" )
    canvas.draw_polygon([(105, 40), (221,90), (110, 120)], 1, "#black","black")
       
    

frame = simplegui.create_frame("CFU15 Happy Shapes", 200, 200)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)
frame.start()
