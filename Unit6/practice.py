
#Betsy Sumba
#12/11/2024
#CFU 16
#1-2

import simplegui
def draw_handler(canvas):
    canvas.draw_circle((100, 95), 80, 3, "Black", "pink")
    #eyes
    canvas.draw_circle((65, 90), 25, 3, "black", "white")
    canvas.draw_circle((140,90), 25, 3, "black" , "white")
    canvas.draw_circle((70,90),10,3, "black", "black")
    canvas.draw_circle((131,90),10,3,"black" , "black")
    #mouth
    canvas.draw_circle((100,150), 5, 3, "black", "black")
    canvas.draw_circle((120,142), 5, 3, "black", "black")
    canvas.draw_circle((85,142), 4, 3, "black" , "black")
    
    
   
frame = simplegui.create_frame("CFU16 Happy circles", 200, 200)
frame.set_canvas_background("white")
frame.set_draw_handler(draw_handler)
frame.start()
