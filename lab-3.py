#project -1:
# x1 =float(input("enter x1:"))
# y1 = float(input("enter y1:"))
# r = float(input("enter r:"))
# x2 = float(input("enter x2:"))
# y2 = float(input("enter y2:"))
# distance = ((x2-x1)**2 +(y2-y1)**2)**0.5
# if distance<r:
#     print("inside")
# elif distance == r:
#     print("boundary")
# else:
#     print("outside")  

# #project -2:
# import math  
# s = float(input("enter length:"))  
# if s<= 0:
#     print("side positive")
# else:
#     area =(5 *s**2)/(4*math.tan(math.pi/ 5))
#     print(f"the area of pentagon is :{round(area,2)}")

#project -3:     
# a1 =float(input("enter first angle:"))
# a2 = float(input("enter second angle:"))
# a3 = float(input("enter third angle:"))
# if a1<= 0 or a2<= 0 or a3 <= 0:
#     print("invalid")
# elif a1 +a2 +a3 !=180:
#     print("invalid angles")
# else:
#     print("can form triangles")
# if a1 ==90 or a2==90 or a3==90:
#         print("right angle")
# elif a1> 90 or a2>90 or a3>90:
#         print("obtuse angle")  
# else :
#         print("acute angle")     \

# project -4:
# num = int(input("enter four digit no.:")) 
# if num<1000 or num>9999:
#       print("invalid input")
# else :
#      first_two = num//100
#      last_two = num % 100
#      sum_first =(first_two //10) +(first_two% 10)
#      sum_last = (last_two//10) + (last_two%10)
#      print(f"sum of first two:{sum_first}")
#      print(f"sum of last two:{sum_last}")

# if sum_first ==sum_last:
#       print("the two sum are equal")
# else:
#       print("the two sum are not equal")  


# #project -5:
# num = int(input("enter 5 digit number:"))
# if num<10000 or num >99999:
#       print("invalid input")
# else:
#       d1 =num //10000
#       d2 = (num //1000) %10
#       d3 = (num //100)%10
#       d4 = (num //10)%10
#       d5 =num % 10

# largest =d1
# position = 1
# if d2> largest :
#     largest =d2
#     position =2

# if d3> largest:
#       largest = d3
#       positon = 3 

# if d4 > largest:
#       largest = d4
#       position = 4

# if d5 > largest:
#       largest = d5
#       position = 5
# print(f"the largest number is:{largest}")
# print(f"position from left:{position}")      

#project -6:
# a = int(input("enter a:"))
# b = int(input("enter b:"))
# c =int(input("enter c:"))
# a = a+b+c
# b =a-(b+c)
# c = a-(b+c)
# a = a-(b+c)
# print(f"a ={a},b ={b},c ={c}")

# #project-7:
# num = int(input("enter 3 digit number:"))
# hundreds = num//10
# tens = (num//10) %10
# ones = num %10
# digit_sum =hundreds + tens +ones
# if num % digit_sum ==0:
#     print(f"{num} is harshad number")
# else:
#     print(f"{num}is not harshad number")

# #project -8:
# v =float(input("enter initial vol:"))
# n =int(input("enter the no. of days:"))

# if v<0:
#     print("invalid input for v")
# elif n<0:
#     print("invalid input for n")
# else:
#     if n==0:
#         final_volume = v
#     else: 
#         r = 0.95

#         final_volume = (v*(r**n)) +(10*(1-r**n) /(1-r))
#         print(f"the quantity of water after{n} days is:{round(final_volume)}")  

#project -9:
# a1 = float(input("enter a1: "))
# b1 = float(input("enter b1:"))
# c1= float(input("enter c1:"))
# a2 = float(input("enter a2:"))
# b2 = float(input("enter b2:"))
# c2 = float(input("enter c2:"))
# d =(a1*b2)-(a2 *b1)
# dx = (c1*b2)-(c2*b1)
# dy = (a1*c2)-(a2*c1)

# if d ==0 :
#     if dx ==0 and dy ==0:
#         print("/nthe lines are coincide")
#     else:
#         print("/n lines are parallel")
# else:
#     x = dx/d 
#     y =dy/d  
#     print(f" point of intersection:({x:.2f},{y:.2f})")         




    
                     