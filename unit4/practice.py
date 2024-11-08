
#Betsy Sumba
#10/29/2024
#CFU11
# 1 and 2 

for i in range(21):
    print(i * 0.5) 
    
for x in range (10,71,10):
    print(x)


#Betsy Sumba
#10/30/2024
#1 and 2 
#CFU12
def v1():
    password = "simonsnyc"
    

while password != userInput :
    print("Wrong Password!")
    userInput = input("Enter Passcode: ")

print("Correct! You may enter..") 
    
#v1()

def v2():
    password = "simonsnyc"
    userInput = input("Enter Passcode: ")
    i = 0
    

while password != userInput and i < 2 :
    
    print("Wrong Password!")
    i +=1
    userInput = input("Enter Passcode: ")
if password == userInput:
    print("Correct! You may enter..")
    

    
#version2()
def main():
    version = input("choose 1 or 2")
    if version == "1":
        v1()
   


        
    elif version == "2":
        v2()
    else:
        print("that isn't a choice")
        
main() 


    
    
