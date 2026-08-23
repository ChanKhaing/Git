# Data structure and function  


# List ([]): Data တွေကို အစဉ်လိုက် သိမ်းပေးပါတယ်။ တန်ဖိုးတွေကို ပြန်ပြင်လို့ရပါတယ် (Mutable)။ (JS Array နဲ့ ဆင်တူ)

# Tuple (()): Data တွေကို အစဉ်လိုက် သိမ်းပေးပေမဲ့ တန်ဖိုးတွေကို ပြန်ပြင်လို့ မရပါ (Immutable)။ Data မပျောက်ပျက်စေချင်တဲ့အခါ သုံးပါတယ်။

# Dictionary ({}): Key-Value pairs တွေနဲ့ သိမ်းဆည်းပါတယ်။ (JS Object နဲ့ ဆင်တူ)

# Set ({}): ထပ်နေတဲ့ တန်ဖိုးများ (Duplicates) ကို လက်မခံဘဲ Unique values တွေကိုပဲ Unordered စနစ်နဲ့ သိမ်းပေးပါတယ်။

# (B) Practical Example

# 1. List
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")      # တန်ဖိုးသစ်ထည့်ခြင်း
fruits[0] = "green apple"   # တန်ဖိုးပြင်ခြင်း
# print(f"List: {fruits}")

# 2. Tuple
coordinates = (10, 20)
# coordinates[0] = 15  <- Error တက်ပါမည် (ပြင်ခွင့်မရှိပါ)
# print(f"Tuple X: {coordinates[0]}")

# 3. Dictionary
user = {
    "name": "Alice",
    "role": "Admin",
    "is_active": True
}
print(f"User Name: {user['name']}")
# user["role"] = "SuperAdmin"
# Key ရဲ့ တန်ဖိုးကို ပြင်ခြင်း


# 4. Set (Duplicates ဖျက်ခြင်း)
# numbers = {1, 2, 2, 3, 4, 4, 4}
# print(f"Unique Set : {numbers}")  # Output: {1, 2, 3, 4}

# function 

# 1. Basic Function with Default Parameter & Type Hints
def calculate_tax(amount: float, tax_rate: float = 0.05) -> float:
    """အခွန်ပမာဏကို တွက်ချက်ပေးသော Function"""
    return amount * tax_rate

# Function ကို ခေါ်သုံးခြင်း
total_tax_1 = calculate_tax(100.0)             # tax_rate ကို default (0.05) သုံးမည်
total_tax_2 = calculate_tax(100.0, 0.10)       # tax_rate ကို 0.10 ပြောင်းသုံးမည်

print(f"Default Tax: ${total_tax_1}")
print(f"Custom Tax: ${total_tax_2}")

# 2. Returning Multiple Values (Tuple Unpacking)
def get_user_status():
    name = "DevGuy"
    status = "Active"
    return name, status  # Tuple အဖြစ် ပြန်ပေးသည်

user_name, user_status = get_user_status()
print(f"User: {user_name}, Status: {user_status}")

def hello() -> str:
    print("hello world")
hello()