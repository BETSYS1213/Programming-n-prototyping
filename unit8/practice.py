
#Betsy Sumba
#Project
#1-2
#1/17/2025
 
import simplegui 
#frame
frame = simplegui.create_frame("My Adventure Game", 600, 400)
frame.start()
#north
def go_north():
    print("You go north!")
frame.add_button("Go North!", go_north, 150)
def update_room_description(description):
    frame.set_label(description)
    
def go_sorth():
    print("You go north!")
    frame.add_button
frame.add_button("Go North!", go_north, 150)
def update_room_desuription(description):
    frame.set_lable

#west
def go_west():
    print("you go west ")
    frame.add_button
frame.add_button("Go west!", go_north, 150)   
def update_room_desuription(description):
          frame.set_lable                                                                                                                              
#east           
def go_east():
    print("You go east")
    frame.add_button
frame.add_button("Go east!" , go_east, 150)    
def update_room_desuription(description):
    frame.set_lable
    
def random():
    if random.randint(1,3)== 1: #33% chance
        print("You foud a hidden treasure!")
    else:
        print("Nothing happens.")
        
inventory = []
def find_sword():
    inventory.append("sword")
    print("You have found a sword")
    
#inventory    
def display_inventory():
    inventory_label.set_text("Inventory: " + ", ".join(inventory))

health = 100         
#fighting a monter
def fight_monster():
    global health
    health -= 10
    print("You fought a monster! Health is now", health)
    
frame.add_button("fight Monster" , fight_monster, 150)


