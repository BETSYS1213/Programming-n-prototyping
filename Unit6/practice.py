
import simplegui
#betsy Sumba
#CFU project 

frame = simplegui.create_frame("Thanksgiving Drawing", 600, 400)
# Draw handler function
def draw(canvas):
    # Example: Drawing a circle
    canvas.draw_circle((400, 250), 100, 10, "#b17800", "#b15000")
    canvas.draw_circle((299, 170), 99, 10, "Taupe", "#b15000")
    canvas.draw_circle((170, 260), 99, 10, "Taupe", "#b15000")
   
    #back of the drawing(tail)
    canvas.draw_circle((300, 200), 100, 10, "#da9349", "Orange")
    canvas.draw_circle((250, 200), 35, 10, "black", "grey")
    canvas.draw_circle((350, 200), 35, 10, "black", "grey")
    canvas.draw_circle((300, 400), 100, 10, "#da9349", "Orange")
    # Example: Drawing a polygon
    canvas.draw_polygon([(250, 250), (350, 250), (300, 300)], 5, "#af9549", "Yellow")
    # Example: Drawing a point
    canvas.draw_point((200, 500), "Blue")
   

# Assign draw handler to the frame
frame.set_draw_handler(draw)

# Start the frame
frame.start()
