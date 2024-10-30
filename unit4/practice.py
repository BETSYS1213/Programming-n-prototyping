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
def version1():
    password = "simonsnyc"
userInput = input("Enter Passcode: ")

while password != userInput :
    print("Wrong Password!")
    userInput = input("Enter Passcode: ")

print("Correct! You may enter..") 
    
#version1()

def version2():
    password = "simonsnyc"
    userInput = input("Enter Passcode: ")
    num_guesses = 0
    

while password != userInput and num_guesses < 3 :
    
    print("Wrong Password!")
    userInput = input("Enter Passcode: ")
    num_guesses += 1
 if password == "simonsnyc":
    print("Correct! You may enter..")
    
else:
    print("Wrong Password!")
    
version2()    
    
    







