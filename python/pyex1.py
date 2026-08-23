###### Variables, Data Types, Operators & Expressions  ########
# 1. Variables & Types
age = 25              # int
height = 5.8      # float
name = "Ko Ko"        # str
is_student = False    # bool

# 2. Operators & Expressions
years_to_add = 5
future_age = age + years_to_add # Expression

# 3. Output with f-string(without f it can't error but also it doesn't show variable value)
print(f"Name: {name}, Current Age: {age}")
print(f"In {years_to_add} years, age will be {future_age}.")

# 4. Type Checking
print(type(age))    
# <class 'int'>
print(type(height))
# <class 'float'>
a = range(5)
print(type(a))


######   Control Flows (Conditionals & Loops)     ########

# --- (1) Conditionals ---
score = 85

# if score > 90 :
#         print("this is good ")
# elif score >= 70 :
#         print("this is no bad")
# else:
#         print("okay fine it ")
        
        
for i in range(5):
    print(f"number in {i}")

if score >= 90:
    print("Grade: A")
elif score >= 75 and score < 90:
    print("Grade: B")  # ဒီလိုင်း အလုပ်လုပ်မည်
else:
    print("Grade: C")

# --- (2) For Loop with range() ---
# range(5) က 0 ကနေ 4 အထိ ထုတ်ပေးပါတယ်
print("For Loop output:")
for i in range(5):
    print(f"Number: {i}")

# --- (3) While Loop ---
count = 3
print("While Loop output:")
while count > 0:
    print(f"Countdown: {count}")
    count -= 1  # count = count - 1     print("okay fine it ")

    
