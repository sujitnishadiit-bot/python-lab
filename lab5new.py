'''
x = int(input("input x:"))                       #ans1
y = int(input("input y:"))
n = int(input("input z:"))
not_w = 0
for i in range(x,y):
    if i%n != 0:
        print(i,end=' ')
        not_w+=1
print(f"\nthe number of working posts: {not_w}")
'''
'''
n = int(input('enter digit:'))                      #ans2
multi = 1
d = 0
while n>0:
    d = n%10
    multi = multi * d
    n = n//10
print(multi)
 '''
'''
n = int(input("enter N:"))                          #ans3
b = int(input("enter bill amount:"))
sb = 0
lb = 0
while b != -999:
    if b>n:
        lb+=1
    else:
        sb+=1
    b = int(input("enter bill amount:"))
print(f"the amount of small bill: {sb} \nthe amount of large bill: {lb}")
'''    
'''
n = int(input("enter N:"))                        #ans4
v = 1
p = int(input("enter P:"))
while n>0 and p>0:
    v = v*n
    p = p-1
print(v)

'''
'''
n1 = int(input("enter first number:"))               #ans5
n2 = int(input("enter second number:"))
rev = 0
while n1>0 and n2>0:
    rev = rev*10 + n1%10
    n1 = n1//10
if rev == n2:
    print(f"{n2}nis exact reverse of {n1}")

else:
    print(f"{n2}nis not the reverse of {n1}")
'''
'''
n = int(input("enter n:"))                       #ans6
v = 1
for i in range(n+1):
    print(v,end=' ')
    v = v*2
 ''' 
'''
n = int(input("enter number:"))                  #ans7
sum = 0
for i in range(1,n):
    if n%i == 0:
        sum+=i
if sum == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is  not a perfect number")
'''   
'''
n = int(input("enter number:"))                    #ans8
for i in range(1,n+1):
    print("*"*i)    
'''
'''
n = int(input("enter number:"))                     #ans9
d = int(input(" enter D:"))
count = 0
while n>0:
      x = n%10
      n = n//10
      if d == x:
        count+=1
print(count)
 '''
'''
n = int(input("enter number:"))                  #ans10
count = 0
for i in range(1,n+1):
    if n%i == 0:
        print(i,end=' ')
        count+=1
print("\n")
print(f"the number of factors: {count}")
'''







