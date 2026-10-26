'''
#ans1
a = input("enter your line: ")
a = a.lower()
d = 0
v = 0
c = 0
s = 0
sc = 0
for i in a:
    if i.isdigit():
        d+=1
    elif i in "aeiou":
        v+=1
    elif i==" ":
        s+=1
    elif i.isalpha():
        c+=1
    else:
        sc+=1
print(f"total digits in string: {d}") 
print(f"total vowels in string: {v}") 
print(f"total consonants in string: {c}") 
print(f"total space in string: {s}") 
print(f"total special characters in string: {sc}")
'''
'''
#ans2
x = input("enter your string: ")
x = x.lower()
y = ""
for i in range(len(x)):
    if i%2==0:
       y+= x[i].capitalize()
    else:
       y+= x[i]
print(y)
'''
'''
#ans3 #isalpha and is digit only give true for all string
x = input("input your password:")
c = 0
if len(x)<8:
    print("WEAK")
else:
    for i in x:
        if i.isalpha():
            c+=1
        
        if i.isalnum()==False and i!=" ":
                c+=1
if c==4:
            print("STRONG")
elif 4>c>1:
            print("MODERATE")
else:
            print("WEAK")
'''
'''
#ans4 #to join list of strings we use syntax "seperator".join(list)
x = map(input("enter your string:").split())
c = input("character:")
pos = [-1]
position = -1
for i in x:
    position+=1
    count = x.count(c)
    if i==c:
        pos.remove(-1)
        pos.append(position) #use str(i) instead of just (i)
pos = " ".join(pos)  # i need to covernt int to str to use join # i can use "".join(map(str,pos)) or "".join[str(x) for x in pos])
print(f"Count: {count}")
print(f"Position: {pos}")
'''
'''
#ans5 [list]
x = input("enter your string:").split()  #split ignores spaces
count=0
for i in x:
    for j in i:
        count+=1
    print(count,end=" ")
    count = 0
'''
'''
#ans5 [no list]
x = input("enter your string:")
count = 0
final = 0
for i in x:
    if i!=" ":
        count+=1
    if count>0 and i==" ":
        print(count,end=" ")
        count=0
if count>0:     #for last word since it wont be printed
    print(count)
'''

#ans6
x = input("enter your numberplate: ")
if x.isupper():
    a = x[0:4:]
    b = x[4:6]
    c = x[6:10]
    if a == "RJ14" and b.isalpha() and c.isdigit():
        print("TRUE")
    else:
        print("FALSE")
else:
    print("FALSE")
      
'''
#ans7
x = input("enter your string:")
new = []
new2 = []
count =0
if len(x)%2==0:
    a = len(x)//2
    for i in range(a):
        new.append(x[i])
    for j in range(a, len(x)):
        new2.append(x[j])
    for q in range(a):
        y = new[q]
        z = new2[q]
        if y!=z:
            count+=1
    print(count)
else:
    a = len(x)//2
    for i in range(a):
        new.append(x[i])
    for j in range(a+1, len(x)):
        new2.append(x[j])
    new2.reverse()
    for q in range(a):
        y = new[q]
        z = new2[q]
        if y!=z:
            count+=1
    print(count)
'''
        
        
'''
#ans8
x = input("enter your string:")   
seen = ""   
for i in x:
    if i not in seen:
        print(i,end="")
        seen+=i
'''  
'''
#ana9 
x = input("enter your string:").strip()
shift = int(input("enter shift:"))
n =""
for i in x:
  a = ord(i)
  if 65<=a<97:
    base = 65
  elif 97<=a<=122:
    base = 97
  else:
    n = n+i
    continue
  a_normal = a-base
  s = a_normal+shift
  s = s%26
  n = n + chr(s+base)
print(n)
'''
'''
#ans10
x = input("enter your string:").strip().lower()
seen=""
for i in x:
  if i not in seen:
    count = x.count(i)
    print(f"{i} {count}")
    seen+=i
'''
























