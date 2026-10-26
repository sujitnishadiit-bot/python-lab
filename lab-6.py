#lab-6:
'''  
#project:1

print("     Addition Table     ")
print(f"{ ' ':>3}", end =" ")

for i in range(1,10):
    print(f"{ i: >4}", end =" ")
print()

print(" _"* 25)

for i in range(1,10):
    print(f" {i :>2} |", end =" ")
    for j in range(1,10):
        print(f"{i +j : >4}", end = " ")
    print()    
    
'''    

#project:2
'''
n = int(input("enter n :"))
i = n 
while i<= 1000:
    if i % 4!= 0:
        print(i,end =" ")
    i = i+n 
 '''   
    
'''
#project:3
#a:
n = int(input("enter n:"))
for i in range(1,n +1):
    for j in range(1,i+1):
        print(j,end =" ")
    print() 
    
# b:
n =int(input("enter n:"))
for i in range(n,0,-1) :
    for j in range(1,i +1):
        print("*" ,end = " ")
    print()  
    
    
    
#  c:
n = int(input("enter n:"))
i =1
while i<= n:
    j =1
    while j <=i :
        print(" *",end =" ")
        j =j+1
    print()
    i = i+1
    
#project:4 
n =int(input("enter n:"))
ans = " " 
for i in range(n):
    if n == 0:
        break
    r = n % 8
    ans = str(r) +ans
    n = n// 8
print()    
    
    
# project:5 
n = int(input("enter n:"))
winner = 0
runner = 0
for i in range(n):
    x = int(input("enter distance:"))
    if x > winner:
        runner = winner
        winner = x
    elif x> runner and x< winner:
        runner = x 
print("winner =",winner)
print("runner_up =",runner) 


# project:6
n = int(input("enter n:"))      
for i in range(1,n+1):
    x = i
    total = 0
    while x > 0:
        digit = x % 10
        total = total +digit ** 3
        x = x // 10
    if total == i:
        print(i,end =" ")
    
    
 # project:7 
for i in range(1,16):
    square = i*i
    cube = i*i*i
    root = i ** 0.5
print(i,square,cube,round(root,4))


# project:8
n = int(input("enter n:"))
for i in range(1,n +1):
    for j in range(i):
        print(i , end =" ")
    print()    


# project:9
n = int(input("enter n:"))
num = 1
for i in range(1,n +1):
    for j in range(i):
        print(num,end =" ")
        num = num +1
    print()



# project:10
n = int(input("enter n :"))
for i in range(1,n +1):
    if i <=(n +1)// 2:
        stars = 2* i-1
    else:
        stars = 2*(n-1) +1
    print(" *" * stars)    


'''









    

    
    
    