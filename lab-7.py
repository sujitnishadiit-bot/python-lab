#lab-7:
'''    
#project-1: 
s = input("enter string:")
rev = " "  
for i in s:
    rev = i + rev
print("Reverse:",rev)  


#project-2:
s = input(" enter sentence:")
count =0
for ch in s[::-1]:
    if ch!= " ":
        count += 1
    else:
        break
print(count)


#project-3:
s = input("enter sentence:")
word = input("enter word:")

count =s.count(word)  

print("Count:",count)  


#project-4:
s = input("enter sentence:").lower()
pawan ="abcdefghijklmnopqrstuvwxyz"
con = True
for ch in pawan:
    if ch not in s:
        con = False
if con:
   print("panagram")
else:
    (" not panagram")
   
    
#project-5:
s = input("enter string:")
n = int(input("enter shift:"))
result =" "
abc ="abcdefghijklmnopqrstuvwxyz"
for ch in s:
    i = abc.index(ch)
    result = result +abc[(i +n) % 26]

print(result)    
  

#project-6:
a=b=c=d=e=0
total =0
n =int(input("enter number:"))
while n!= -1:
    if 1<=n<=2:
        a += 1
    elif 3<= n <=4:
        b += 1
    elif 5<=n<=6:
        c += 1
    elif 7<=n<=8:
        d += 1
    elif 9<= n <= 10:
        e += 1
    if 1 <= n <= 10:
        total += 1
    n =int(input("enter num:"))
if total > 0:
    print("1-2:"," #" *a,a* 100/total,"%")
    print("3-4:", " #"*b,b*100/total,"%")
    print("5-6:"," #" *c,c*100/total,"%")
    print("7-8:"," #" *d,d*100/total,"%")
    print("9-10:"," #" *e,e*100/total,"%")
else:
    print("no numbers entered")


#project-7:
s = input("enter string:")
rev= " "
for ch in s:
    rev = ch + rev
if s==rev:
    print("palindrome")
else:
    print("not palindrome")


#project:8 
# 1:
a = int(input("enter number:")).split()
sum =0
for i in range(len(a)):
    sum = sum + a
print("sum:",sum)    
        
#2:
a = int(input("enter number:"))
product =1
for x in a:
    product *= x
    
print("product:", product)

#3:
a =int(input("enter number:")).split()
small = a[0]
for x in a:
    if x < small:
        small = x
        
print("smallest:", small)        
        
        
#project-9:
a =list(int(input("enter numbers:").split()))
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] > a[j]:
            a[i] ,a[j] = a[j] ,a[i]
print(a)


#project-10:
s =input("enter words:")
a = s.split("-")
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print("-".join(a))     


# project-11:
s =input("enter paragraph:")
d = a = u = l = sp = 0
for ch in s:
    if ch.isdigit():
        d += 1
    elif ch.isalpha():
        a +=1
        if ch.isupper():
            u +=1
        else:
            l +=1
    else:
        sp +=1
        
print("digits:",d) 
print("alphabets:",a)
print("upper case:",u)
print("lower case:",l)
print("special:",sp)       
            
        
#project-12:
s = input("enter string:")
result =" "
for ch in s:
    if ch not in result:
        result +=ch
print(result)
'''
    







    
    
    
    

































    
    