# import sys
# import random



# print("hello world")
# print("\n--- 2. String Operations ---")
# print('Alice' + 'Bob')  # 'AliceBob' (Concatenation - စာသားတွဲခြင်း)
# print('Alice' * 3)  
# name = (input("Enter your name: "))
# print(f"Hello, {name}")  # f-string (String Interpolation - စာသားထဲမှာ Variable ထည့်ခြင်း)   


# age = (input("Enter your age: "))
# next_age=(int(age) + 1 )
# print(f"Hello, {name}! Next year, you will be {next_age}.")

# name = input("Enter your name: ")
# name_length = len(name)  # len() က string ရဲ့ အရှည်ကို  နံပါတ်နဲ့ ပြန်ပေးတယ်။
# print(f"Hello, {name}! Your name has {name_length} characters.")



# Python က Expression တွေကို အမြဲတမ်း တန်ဖိုးတစ်ခုအဖြစ် အကဲဖြတ်တယ်။ ဒါက ပရိုဂရမ်တွေရဲ့ အခြေခံအုတ်မြစ် ဖြစ်တယ်။

# Data Types (int, float, str) တွေက အရမ်းအရေးကြီးတယ်။ ဘာဖြစ်လို့လဲဆိုတော့ Operator (+, *) တွေရဲ့ အလုပ်လုပ်ပုံက Data Type ပေါ်မူတည်လို့ပဲ။ (string ဆို ဆက်ပေး၊ number ဆို ပေါင်း)

# Functions တွေက code ကို ပြန်သုံးလို့ရအောင်၊ ရှင်းလင်းအောင် ကူညီတယ်။ input() က အမြဲတမ်း string ပြန်တာမို့ integer အနေနဲ့ သုံးချင်ရင် int() နဲ့ ပြောင်းရမယ်။


# first_name = "Al"
# last_name = "Sweigart"
# # + က စာသားတွေကို ဆက်ပေးတယ်။
# full_name = first_name + " " + last_name
# print(f"Full Name:,{full_name}")  # Output: Full Name: Al Sweigart

# print("Ha" * 3)      # "HaHaHa" ထွက်မယ်
# print("!" * 10)      # "!!!!!!!!!!" ထွက်မ�ယ်
#  သတိပြုရန် - string နဲ့ integer ကို + နဲ့တွဲလို့မရဘူး။
# print("Age: " + 25)  # ဒီစာကြောင်းကို ဖွင့်ကြည့်ရင် TypeError ပြမယ်။



# အောက်ပါ Code မှာ အမှား (၃) ချက်ရှိနေပါတယ်။ ရှာပြီး ပြင်ပေးပါ။

# user_name = input("What is your name? )
# print("Hello, " + user_name)
# print("Your name has " + len(user_name) + " letters.")

# user_age = input("Enter your age: ")
# print("In 5 years, you will be " + user_age + 5)


#ဒါက ပြင်ဆင်ထားတဲ့ Code ဖြစ်ပါတယ်။
# user_name = input("What is your name? )
# user_name = (input("What is your name? "))  # Missing closing quote)
# print("Hello, " + user_name)
# print("Your name has " + str(len(user_name)) + " letters.")

# user_age = input("Enter your age: ")
# print("In 5 years, you will be " + str(int(user_age) + 5))

# x = 10
# y = 3
# print(x / y)
# print(x // y)
# print(x % y)


# color = input("What is your fav color  :")
# print(f"your fav color is  {color}")
# print(f"your fav color has {len(color)} letters")


# x = 10
# y = 20

# print(x < y)             # True
# print(x > y)             # False
# print(x <= y)            # True  <-- Changed x <= x to x <= y
# print(x >= y)            # False     # False  


# print(True and True)     
# print(True and False)    
# print(False and True)    
# print(False and False)   

# # or - တစ်ခုခု True ရင် True
# print(True or True)      
# print(True or False)     
# print(False or True)     
# print(False or False) 

# name = "Alice"
# age = 25

# if name == "Alice" and age < 22:
#     print("Hi, Alice!")          # ဒါက run မယ်
# elif age < 12 or name == "Alice":
#     print("You're  Alice, kiddo!")
# elif age > 2000:
#     print("Unlike you, Alice is not an undead vampire.")
# elif age > 100:
#     print("You're not Alice, grannie.")
# else:
#     print("You're neither Alice nor a little kid.")
    
    
# horse = 0 
# while horse < 5 :
#     print(f"horse is {horse}")
#     horse=horse + 1




i=0
# while i < 5:              # Infinite loop
#     print(i)
#     if i == 3:
#         break
#     i = i + 1

# print("\nContinue example:")
# for i in range(5):
#     if i == 4:
#         #sys.exit()        # program ကို ချက်ချင်းပိတ်တယ်
#         continue         # i==4ဆိုရင် ဒီအောက်က print ကို ကျော်သွားမယ်
#     print(i)
    
# # range(stop) - 0 ကနေ stop-1 အထိ   
# for i in range(5):
#     print(i , end= "|")    # 0 1 2 3 4
# print()

# # range(start, stop) - start ကနေ stop-1 အထိ
# for i in range(2, 7):
#     print(i, end=" ")    # 2 3 4 5
# print()

# # range(start, stop, step) - step အတိုင်း ခုန်တယ်
# for i in range(0, 10, 3):
#     print(i, end=" ")    # 0 2 4 6 8
# print()

# # နောက်ပြန်ရေတွက်တဲ့အခါ step ကို negative ထည့်တယ်
# # random.randint() - random integer ထုတ်တယ်
# for i in range(5, -1 , -1):
#     print(i , end= "*")   
# print()

# for i in range(3):
#     print(random.randint(1,20), end=" ")
# print()
# sys.exit() - program ကို ချက်ချင်းပိတ်တယ်

# အောက်ပါ Code မှာ အမှား ၃ ချက်ရှိနေပါတယ်။ ရှာပြီး ပြင်ပေးပါ။

number = 5

if number == 5:
    print("Number is 5")

elif number > 10:
    print("Number is greater than 10")
elif number < 5 :
    print("Number is less than 5")

while number > 0:
    print(number)
    number = number - 1
    break
print("Loop ended",{number})