#Betsy Sumba
#1-2
#1/2/2025
#CFU Review + build in formating funtions

box ="cat"

def formating(box):
    userInput = int(input("choice?(1,2,34,5,6,7,8,9)"))
    if userInput == 1:
        #capitaliza 
        box = box.capitalizel()
        print(box)
    elif userInput == 2:
        #find and returrn the position of a value in thr string
        box = box.find("i")
        print(box)
    elif userInput == 3:
        # return try if the varr is a number
        box = box.isdigit()
        print(box)
    elif userInput == 4:
        #output the var all lowercrase
        box = box.lower
        print(box)
    elif userInput == 5:
        #rep
        print(box.replace("o","a"))
    elif userInput == 6:
        # output all upper case
        box = box.upper()
        print(box)
   
    else:
        print("not a valid option")
formating(box)

