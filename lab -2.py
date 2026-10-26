# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:52:41 2026

@author: lab
"""

#project:1-divisiblity by 5
num =int(input("enter a number: "))
if num % 5 == 0:
    print("Hi")
else:
     print("Bye")    
     
#   2:area of trapezoid- 
x =float(input("enter the length of x side in metre:")) 
y =float(input("enter the length of y side in metre:")) 
h =float(input("enter the length of h side in metre:")) 

area = 0.5 * (x+y) * h
print(f"the area of trapezoid is :{area} sq. meters")

#3.BMI INTERPRETER:
Weight = float(input("enter weight in kg:"))
height = float(input("enter height in metre :"))

bmi = Weight/ (height ** 2)
print(f"your bmi is :{bmi:2f}") 

if 0< bmi >18.5:
    print("underweight")
elif 18.5< bmi <25 :
    print("normal weight")
elif 25< bmi<30 :
    print("slightly overweight")
elif 30<bmi < 35 :
    print("obese")
else:
    print("clinically obese")
    
    
#4:vowel or consonant checker:    
pawan = input("enter an alphabet : ").lower()

if pawan in ['a','e','i','o','u']:
    print("vowel")
elif pawan.isalpha():
    print("consonant")
else:
    print("invalid input: not an alphabet ")



#5:bacterial growth percentage:
initial = 2.19e14
final = 4.68e14 

growth_percentage = ((final- initial) / initial) * 100
print(f"bacterial growth :{round(growth_percentage)}%")


#6:time converter:
total_months = int(input("enter total number of months: "))

years = total_months // 12
remaining_months = total_months % 12

print(total_months,"is equal to",years,"and",remaining_months,"months" )     

#7. John Hancock Building Weather Forecast
color = input("Enter color (Blue/Red): ").strip().lower() 
mode = input("Enter mode (Steady/Flashing): ").strip().lower()
if color == "blue" and mode == "steady":  
      print("Steady blue, clear view.")
elif color == "blue" and mode == "flashing":  
      print("Flashing blue, clouds due.")
elif color == "red" and mode == "steady": 
      print("Steady red, rain ahead.") 
elif color == "red" and mode == "flashing":  
      print("Flashing red, snow instead.")
else: 
     print("Invalid color or mode input.")


#8. Break-Even, Profit, or Loss 
cost = float(input("Enter total costs: ")) 
revenue = float(input("Enter total revenue: "))
if cost == revenue:   
     print("Break even")
elif revenue > cost:   
     profit = revenue - cost   
     print(f"Profit: {profit}")
else:  
     loss = cost - revenue  
     print(f"Loss: {loss}")


   
 #9. Widget Order Cost Calculator
widgets = int(input("Enter the number of widgets ordered: ")) 
if widgets < 100:   
     total_cost = widgets * 0.25
else: 
     total_cost = widgets * 0.20 

print(f"Total cost: ${total_cost:.2f}") 


#10. Supermarket Cashier Program
pounds = float(input("Enter number of pounds of apples: ")) 
cash = float(input("Enter amount of cash tendered: "))
total_cost = pounds * 2.50
if cash >= total_cost: 
       change = cash - total_cost 
       print(f"Transaction successful. Your change is: ${change:.2f}") 
else:   
     owed = total_cost - cash 
     print(f"You owe ${owed:.2f} more.") 


#11. Largest of 3 Numbers (Nested If-Else)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2:   
    if num1 >= num3:     
      largest = num1  
    else:    
     largest = num3
else: 
   if num2 >= num3:    
       largest = num2  
   else:    
     largest = num3 

print(f"The largest number is: {largest}")



#12. Gross Salary Calculation
basic_salary = float(input("Enter the basic salary: ")) 
hra = 0.20 * basic_salary
ta = 0.05 * basic_salary
da = 0.10 * basic_salary
gross_salary = basic_salary + hra + ta + da
print(f"Gross Salary: Rs. {gross_salary:.2f}") 


#13. Income Tax Slab Identification
gross_salary = float(input("Enter the gross salary: "))
if gross_salary < 300000:   
     tax_rate = "0%"   
     tax_amount = 0.0
elif gross_salary <= 1000000:   
     tax_rate = "10%" 
     tax_amount = 0.10 * gross_salary 
elif gross_salary <= 2500000:  
      tax_rate = "20%"   
      tax_amount = 0.20 * gross_salary
else:   
     tax_rate = "30%"  
     tax_amount = 0.30 * gross_salary 
print(f"Income Tax Slab: {tax_rate} of the gross salary") 
print(f"Tax Amount: Rs. {tax_amount:.2f}") 


#14. State Income Tax Flowchart Implementation
income = float(input("Get taxable income: "))
if income <= 20000: 
       tax = 0.02 * income
else: 
    if income <= 50000:  
              tax = 400 + 0.025 * (income - 20000)
    else:       
             tax = 1150 + 0.035 * (income - 50000)
print(f"Display tax: {tax:.2f}")