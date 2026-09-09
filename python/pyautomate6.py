# string method 


# 1. Case Conversion (စာလုံးအကြီးအသေး ပြောင်းခြင်း)
# text = "Hello, World!"
# text="hello chan"
# # .upper() - စာလုံးအားလုံးကို အကြီးဖြစ်အောင် ပြောင်းတယ်
# uppercase_text = text.upper()  # "HELLO, WORLD!"
# print(f"Uppercase: {uppercase_text}")

# # .lower() - စာလုံးအားလုံးကို အသေးဖြစ်အောင် ပြောင်းတယ်
# lowercase_text = text.lower()  # "hello, world!"
# print(f"Lowercase: {lowercase_text}")

# # ⚠️ Important: မူရင်း string က မပြောင်းဘူး (immutable)
# print(f"Original: {text}")  # မူရင်းအတိုင်းပဲ ရှိနေတယ်

# #  အထဲက စာတေကို စစ်တာ 
# print(f"Is uppercase? {text.isupper()}")  # False
# print(f"Is lowercase? {text.islower()}")  # False


# user_input = "Python123"
# user_input="python"
# print(f"is alpha ? {user_input.isalpha()}")
# print(f"Is alphanumeric? {user_input.isalnum()}")  # True (စာလုံးနဲ့ နံပါတ်ပဲပါတယ်)
# print(f"Is alphabetic? {user_input.isalpha()}")    # False (နံပါတ်ပါလို့)
# print(f"Is decimal? {user_input.isdecimal()}")      # False (စာလုံးပါလို့)

# # 4. startswith() & endswith() - အစ/အဆုံး စစ်ဆေးခြင်း
# filename = "report_2024.pdf"
# filenamea= "chan_cahn.txt"
# print(filenamea.startswith("chan"))
# print(f"Starts with 'report'? {filename.startswith('report')}")  # True
# print(f"Ends with '.pdf'? {filename.endswith('.pdf')}")          # True
# # ⚠️ Practical Use: file extension စစ်ဖို့ အသုံးဝင်တယ်


# Example 2: String Manipulation Techniques
# -----------------------------------------

# 1. join() & split() - စာကြောင်းတွေကို ပေါင်းခြင်း/ခွဲခြင်း
# words = ["Python", "is", "awesome"]

# # join() - စာရင်းထဲက စာကြောင်းတွေကို ပေါင်းတယ်
# # sentence = " ".join(words)  # "Python is awesome"/
# sentence = " ".join(words)  # "Python/is/awesome"
# print(f"Joined: {sentence}")

# # split() - စာကြောင်းကို စာရင်းအဖြစ် ခွဲတယ် (default: space မှာ ခွဲ)
# back_to_list = sentence.split()  # ['Python', 'is', 'awesome']
# print(f"Split: {back_to_list}")

# # Custom separator နဲ့ ခွဲတယ်
# csv_data = "apple,banana,orange"
# fruits = csv_data.split(",")  # ['apple', 'banana', 'orange']
# print(f"CSV Split: {fruits}")

# # 2. strip() - ဘေးနှစ်ဖက်က whitespace ဖယ်ရှားခြင်း
# messy_text = "  Hello World!  "
# cleaned_text = messy_text.strip()  # "Hello World!"
# print(f"Stripped: '{cleaned_text}'")

# # lstrip() - ဘယ်ဖက်က ဖယ်တယ် / rstrip() - ညာဖက်က ဖယ်တယ်
# print(f"Left stripped: '{messy_text.lstrip()}'")   # "Hello World!  "
# print(f"Right stripped: '{messy_text.rstrip()}'")  # "  Hello World!"

# # 3. find() & replace() - ရှာဖွေခြင်းနဲ့ အစားထိုးခြင်း
# text = "I love Python. Python is great."
# position = text.find("Python")  # 7 (ပထမဆုံးတွေ့တဲ့နေရာ)
# print(f"First 'Python' at index: {position} ")

# # replace() - စာသားကို အစားထိုးတယ်
# new_text = text.replace("Python", "JavaScript", 1)  # တစ်ခုသာ အစားထိုးမယ်
# print(f"Replaced: {new_text}")
# ⚠️ Note: replace() က အကုန်လုံးကို အစားထိုးတယ် (replace all)


# Example 3: Modern String Formatting (f-strings)
# ------------------------------------------------

# name = "Alice"
# age = 30
# salary = 75000.505

# # 1. f-string (Python 3.6+) - အကြံပြုထားတဲ့ နည်းလမ်း
# message = f"Name: {name}, Age: {age}, Salary: ${salary:,.2f}"
# print(message)  # "Name: Alice, Age: 30, Salary: $75,000.50"

# # 2. String Interpolation (%) - ရှေးနည်းလမ်း (မသုံးသင့်တော့)
# old_style = "Name: %s, Age: %d" % (name, age)
# print(old_style)

# # 3. format() method - အလယ်အလတ်နည်းလမ်း
# new_style = "Name: {}, Age: {} , Salary: ${}".format(name, age, salary)
# print(new_style)

# # 4. f-string with expressions (အတွင်းမှာ expression တွေ ထည့်လို့ရတယ်)
# next_year_age = f"Next year, {name} will be {age + 1} years old."
# print(next_year_age)  # "Next year, Alice will be 31 years old."

#  Important: f-string က performance အကောင်းဆုံးနဲ့ readability အကောင်းဆုံးပါ






# # Example 4: Clipboard Automation with pyperclip
# # ---------------------------------------------

import pyperclip  # Third-party module (pip install pyperclip)

# # 1. Copy to clipboard
text_to_copy = "This text will be copied to your clipboard!"
pyperclip.copy(text_to_copy)
# print("Text copied to clipboard!")

# # 2. Paste from clipboard
copied_text = pyperclip.paste()
print(f"Pasted from clipboard: {copied_text}")

# # 3. Practical use-case: Clean up copied text
# def clean_clipboard_text():
#     """ကလစ်ဘုတ်ထဲက စာသားကို သန့်ရှင်းအောင်လုပ်ပြီး ပြန်ကူးယူပေးတယ်"""
#     # ကလစ်ဘုတ်ထဲက စာသားကို ယူတယ်
#     raw_text = pyperclip.paste()
    
#     # နေရာလွတ်တွေကို ဖယ်ရှားပြီး စာကြောင်းတွေကို ပုံမှန်ဖြစ်အောင်လုပ်တယ်
#     cleaned = "\n".join([line.strip() for line in raw_text.splitlines() if line.strip()])
    
#     # သန့်ရှင်းပြီးသား စာသားကို ပြန်ကူးယူတယ်
#     pyperclip.copy(cleaned)
#     print("Cleaned text copied to clipboard!")

# # Run the function
# clean_clipboard_text()