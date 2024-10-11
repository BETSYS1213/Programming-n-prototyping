#Betsy Sumba
#9/24/2024
#1,2

fname = input("please give me your first name")
lname = input("please enter last name")

num1 = int(input("please give me a whole number:"))
num2 = float(input("please give me a decimal number:"))

print("nice to meet you " + fname, lname )

addition = num1 + num2
substraction = num1 + num2
multiplication = num1 * num2 
division = num1 / num2 
modulos = num1 % num2 

print("let's do some math with these numbers")
print("the addition of "+ str(num1 ) +" "+ str(num2) + " is "+str(addition))
print("the substraction of "+ str(num1 ) +" "+ str(num2) + " is "+str(substraction))

print(f"the multiplication of {num1} * {num2} is {multiplication}")



#Betsy Sumba
#10/11/2024
#Room Area



A = int(input("Enter side A: "))
B = int(input("Enter side B: ")) 
C = int(input("Enter side C: "))
D = int(input("Enter side D: "))
E = int(input("Enter side E: "))
Rcet = A * B 
scae = (A - C ) * (D -  (B + E))
tran = E * 0.5 * (A - C)
print("Room Area: " + str(Rcet + scae + tran))
