#project 1:
# salary =float(input("enter salary:"))
# years = float(input("enter years:"))
# if years >5 :
#     bonus =0.05*salary
#     print(f"net bonus:{bonus:.2f}")
# else:
#     print("no bonus will there")    


# #project 2:
# password = input("enter password:")
# if password == "s3cr3t!P@ssword":
#     print("welcome")
# else:
#     print("wrong password")    


#project 3:
# shape_type =str(input())
# if shape_type =="square":
#     side = float(input())
#     area = side*side
#     print(f"{area:.3f}")
# elif shape_type =="rectangle":
#     a = float(input())
#     b = float(input())
#     area =a*b 
#     print(f"{area:.3f}")

# elif shape_type =="circle":
#     radius =float(input())
#     pi =3.14
#     area =pi*(radius**2)
#     print(f"{area:.3f}")

# elif shape_type =="triangle":
#      base =float(input())
#      altitude =float(input())
#      area =(base*altitude) /2
#      print(f"{area:.3f}")

# else:
#     print("invalid shape")


#project 4:
# hours =int(input())
# minutes =int(input())
# minutes += 15
# if minutes >60:
#     minutes -= 60
#     hours += 1
# elif hours >24:
#     hours  = 0
# print(f"{hours}:{minutes:02d}")


#project 5:
# distance =float(input())
# period = float(input())
# if period =="day":
#     tasi_price =33.58 +(distance*37.89)
# else:
#     taxi_price  =33.58 +(distance*43.17)
# cheap_price =taxi_price
# if distance >=   20:
#     bus =distance*4.32
#     if bus<cheap_price :
#         cheap_price =bus

# if distance >= 100:
#     train =distance*2.88
#     if train <cheap_price:
#         cheap_price =train

# print(f"{cheap_price:.2f}inr")


#project 6:
# holidays =int(input())
# workdays =365 -holidays
# play_time = (workdays*63) +(holidays*127)
# norm =30000
# difference =(norm -play_time)
# hours =difference //60
# minutes =difference% 60

# if play_time <=norm:
#     print("tom sleeps well")
#     print(f"{hours}hours and {minutes}minutes less for play")
# else:
#     print("tom will ran away")
#     print(f"{hours}hours and {minutes}minutes more for play")


#project 7:
# budget =float(input())
# season =str(input())
# destination =""
# accommodation =""
# money_spent =0.0
# if budget <= 100:
#     destination  = "bulgaria"
#     if season =="summer":
#         accommodation ="camp"
#         money_spent =budget *0.30
#     else:
#         accommodation ="hotel"
#         money_spent =budget*0.70
# elif budget<= 1000:
#     destination ="balkans"
#     if season =="summer":
#         accommodation ="camp"
#         money_spent = budget *0.40
#     else:
#         accommodation ="hotel"
#         money_spent =budget *0.80

# else:
#     destination ="europe"
#     accommodation ="hotel"
#     money_spent = budget *0.90
# print(f"{destination}")
# print(f"{accommodation}- {money_spent:.2f}")

        
#project 8:
# for num in range(6,1001,10):
#     print(num)

#project 9:
# n = int(input("enter the number:"))
# total_sum =0
# for i in range(n):
#     num =int(input(f"enter integer {i+1}:"))
#     total_sum += num 
# print(f"the sum of {n}is: {total_sum}")    


#project 10:
# n = int(input("enter a integer:"))
# for i in range(1,21):
#     print(f"{n} x{i} ={n*i}")



