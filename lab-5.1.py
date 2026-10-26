

#project-1:
x =int(input()) 
y =int(input())
n =int(input()) 

count =0
for i in range(x,y):
    if i % n != 0:
        print(i)
        count = count + 1
print(count)


#project-2:
n = int(input())

product =1
while n > 0:
    digit = n % 10
    product =product * digit
    n = n// 10
    
print(product)    
    
   




#project-3:
n = int(input())
large_count = 0
small_count = 0
while True:
    bill = int(input())
    if bill == -999:
        break
    
    if bill>n:
        large_count += 1
    else:
        small_count += 1
print(large_count)
print(small_count)


#project-4:
n  =int(input())
p = int(input())
if n <= 0 or p <= 0:
    print("invalid")
else:
    result =1
    count = 0
    while count<p:
        result *= n
        count += 1
        print("result:",result)


#project-5:
num1 = int(input())
num2 = int(input())
reversed_num1 =0
while num1 >0:
    reversed_num1 =(reversed_num1* 10)+(num1*10)
    num1 //= 10
if reversed_num1 == num2 :
    print("2nd is reverse of 1st")
else:
    print("2nd is not reverse of 1st")
    

#project-6:
n = int(input())    
current_term = 1

for i in range (n):
    print(current_term)
    current_term *= 2
print()   

#project-7:
n = int(input())
if n <= 0:
     print("invalid")
else:
    divisor_sum = 0
    for i in range(1,(n//2)+1):
        if n % i  ==0:
            divisor_sum += i
    if divisor_sum ==n:
        print("it is a perfect number")
    else:
        print("it is not a perfect number")
        

#project-8:
n = int(input())

for i in range(1,n+1):
    print(" *" * i)
    
#project-9:
n = int(input())
d = int(input("enter digit 0-9:"))
count = 0

if n==0 and d==0:
    count = 1
    
while n > 0:
    if n % 10 == d:
        count +=1
    n //= 10
print(f"digit{d} appears {count}times")



#project-10:
n = int(input())
divisor_count =0
print("divisors:")

for i in range(1, n+1):
    if n % i == 0:
        print(i)
        divisor_count += 1

print("total divisors:",divisor_count)

if divisor_count  ==2:
    print("it is a prime_number ")
else:
    print("it is not a prime_number")
    
      
    
     

      

    
    
    






















    
        
    
        
    