#Betsy Sumba
#1-2
#CFU 14

import simplegui
import random
#eyes
def draw_handler(canvas):
     canvas.draw_line([100, 100], [100, 10], 5, "black")
     canvas.draw_line([10, 100], [10, 10], 5, "black")
    #mouth
     canvas.draw_line([20, 125], [36, 200], 5, "black")
     canvas.draw_line([90,145], [38,200], 5, "blacl")
    

    
    

frame = simplegui.create_frame("Lines", 200, 200)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)
frame.start()
