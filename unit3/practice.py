#10/10/2024
#Betsy Sumba
#CF7 


num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
num3 = int(input("enter a number: "))

def calc_sum(num1, num2, num3):
    sum = num1 + num2 + num3
    print("The sum of you 3 numbers is: "+ str(sum))
    
def average3(num1, num2, num):
    avg = (num1 + num2 +num3)/3
    print("The average of your 2 number is:"+str(avg))
    
calc_sum(num1, num2 ,num3)
average3(num1, num2, num3)
calc_sum(2,4,5)





#Betsy Sumba
#10/15/2024
#period 1,2

delivery = input ("Did you order food? yes or no")

if delivery == "yes" or delivery == "yes" :
    print("Great")
    
else:
    print("NO?! so who is cooking?")



#------ Today---------#
#Betsy Sumba
#10/18/2024
# 1 and 2

import random
print("lets's roll the dice! ")
total = 0
num_rolls = int(input("How many times do we want to roll the the dice? "))

def guess(total):
    
    guess = int(input("Guess the roll: "))
    if guess == num_random:
        total = total +6
        
    else:
        total = total -1
  
def rolls(num_rolls, total=0):
    num_random = random.randint(1,6)
    if num_rolls== 0:
        return total
    else:
        num_rolls = num_rolls -1
        guess(num_random,total)
        print(f"you roll a {num_random}!")
        return rolls(num_rolls,total)
            
total = rolls(num_rolls)
print(f"the total is: {total}")
             
           
