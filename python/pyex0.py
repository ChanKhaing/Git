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

# isinstance(variable, type)  # return true or false
# name=input("Enter your name  :  ")
# print(name)
# if isinstance(name, str):
#     print("It is an string")

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

# number = 5

# if number == 5:
#     print("Number is 5")

# elif number > 10:
#     print("Number is greater than 10")
# elif number < 5 :
#     print("Number is less than 5")

# while number > 0:
#     print(number)
#     number = number - 1
#     break
# print("Loop ended",{number})



#functional
# def say_hello():
#     print("Hello!")
#     print("How are you?")
# say_hello()
# say_hello()

# def say_name(name="Guest"):
#     print(f"hello {name}")
    
# say_name("chan")
# say_name()

# def add(a, b):
#     result = a + b
#     print(f"{a} + {b} = {result}")

# add(5, 3)                  # 5 + 3 = 8

# def square(n):
#     return n ** 2

# print(square(3))           # 9
# print(square(5) + square(2))  # 25 + 4 = 29


# return မပါတဲ့ Function → None ပြန်တယ်
# def do_nothing():
#     # print("hello world")
#     pass   
# # pass က ဘာမှမလုပ်ဘူး
# print(do_nothing())  # None

# spam = print("Hello!")     # print() က None ပြန်တယ်
# print(spam)                # None

# result = None
# if result is None:         # is က identity စစ်တယ် (== ထက် ပိုကောင်းတယ်)
#     print("Result is None")


# global_var = "I'm global"

# def local_demo():
#     local_var = "I'm local"    # Local variable
#     print(local_var)           # Local ကို သုံးလို့ရတယ်
#  #  print(global_var)          # Global ကိုလည်း သုံးလို့ရတယ်

# local_demo()
# # print(local_var)             # ❌ Error! Local ကို အပြင်မှာသုံးလို့မရဘူး
# print(global_var)  


# x= "Hello"
# def meeting():
#     # x = "Hi"  # Local variable
#     global x  # Global variable ကို သုံးချင်ရင် global keyword သုံးရမယ်
#     x = "Hello !!!!"  # Assigning a new value to the global variable
#     print(f"{x}, everyone ")  # Local variable ကို သုံးတယ်

# meeting()  # Output: Hi
# print(x)


def calculate_tax(price, tax_rate=0.07):
    """Price နဲ့ tax_rate ကိုထည့်ရင် tax ပါတဲ့စျေးကို ပြန်ပေးတယ်"""
    return price * ( 1 + tax_rate)

# ဒီ function ဘယ်လိုအလုပ်လုပ်လဲဆိုတာ မသိပေမယ့် သုံးလို့ရတယ်
final_price = calculate_tax(100)     # 107.0
print(f"Price with tax: {final_price}")

# ZeroDivisionError	ဂဏန်းတစ်ခုကို 0 နဲ့ စားမိတဲ့အခါ	10 / 0
# IndexError	List ထဲမှာ မရှိတဲ့ Index နံပါတ်ကို သွားခေါ်မိသည့်အခါ	a = [1, 2]; print(a[5])
# FileNotFoundError	မရှိတဲ့ ဖိုင်ကို ဖွင့်ဖို့ ကြိုးစားသည့်အခါ	open("abc.txt")
# NameError	မသတ်မှတ်ရသေးတဲ့ (Declare မလုပ်ရသေးတဲ့) Variable ကို သုံးမိသည့်အခါ	print(x)
# TypeError	မတူညီသော သို့မဟုတ် မသက်ဆိုင်သော Data Type နှစ်ခုကို ပေါင်းစပ်မိသည့်အခါ	"age: " + 25


# def divide(a, b):
#     try:
#         return a / b
#     except Exception as e:
#         print(f"Error: {e}")
#         return None

# print(divide(10, 2))      # 5.0
# print(divide(10, "chan"))      # Error message, None

# Multiple except blocks
def safe_int_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"Error: '{value}' is not a valid integer!")
        return None
    except TypeError:
        print(f"Error: '{value}' is the wrong type!")
        return None

print(safe_int_convert("123"))   # 123
print(safe_int_convert("abc"))   # Error message, None
print(safe_int_convert([1, 2]))  # Error message, None


# စာရွက်ချက်ပြုတ်နည်း (Function)├── နာမည်: "ကြက်သားဟင်း" (Function Name)├── ပါဝင်ပစ္စည်း: ကြက်သား, ငရုတ်, ဆား (Parameters)├── ချက်ပြုတ်နည်းအဆင့်များ (Code Block)└── ရလဒ်: ကြက်သားဟင်းအဆင်သင့် (Return Value)
def make_chicken_curry(chicken, chili, salt):
    # ချက်ပြုတ်နည်း အဆင့်များ (Code Block)
    cooked_food = f"{chicken} ကို {chili}၊ {salt} တို့နဲ့ နယ်ပြီး မွှေးနေအောင် ချက်လိုက်ပါပြီ"
    
    # ရလဒ် ပြန်ပေးခြင်း (Return Value)
    return cooked_food

# Function ကို ခေါ်သုံးခြင်း (ပါဝင်ပစ္စည်းများ ထည့်ပေးလိုက်ခြင်း)
dish = make_chicken_curry("ကြက်သား ၅၀ ကျပ်သား", "ငရုတ်သီး ၂ ဇွန်း", "ဆား နည်းနည်း")
print(dish)

# Deduplication (မထပ်အောင်): တူတဲ့ code ကို ထပ်ခါထပ်ခါ မရေးရဘူး။

# Modularity (အပိုင်းပိုင်းခွဲခြင်း): ကြီးမားတဲ့ program ကို အပိုင်းလေးတွေခွဲပြီး စီမံရလွယ်တယ်။

# Reusability (ပြန်သုံးနိုင်မှု): တစ်ခါရေးထားတဲ့ function ကို နေရာမျိုးစုံမှာ သုံးလို့ရတယ်။

# Abstraction (ဖုံးကွယ်ခြင်း): "Black Box" သဘော - အတွင်းအလုပ်ကို မသိပေမယ့် သုံးလို့ရတယ်။


def get_min_max(numbers):
    """List ထဲက အငယ်ဆုံးနဲ့ အကြီးဆုံးကို ပြန်တယ်"""
    return min(numbers), max(numbers)  # Tuple အနေနဲ့ ပြန်တယ်

scores = [85, 92, 78, 95, 88]
lowest, highest = get_min_max(scores)  # Unpacking
print(f"Lowest: {lowest}, Highest: {highest}\n")


def order_food(item, quantity=1, size="medium"):
    print(f"Order: {quantity} x {size} {item}")

# Positional arguments (နေရာအတိုင်း)
order_food("pizza", 2, "large")

# Keyword arguments (အမည်နဲ့ခေါ်)
order_food(size="small", item="burger", quantity=3)
order_food("fries", size="large")  # positional + keyword
print()


def convert_int(value):
    try:
        return int(value)
    except Exception as e:
        print(f"Error: {e}")
        return None
    
convert_int("123")   # 123