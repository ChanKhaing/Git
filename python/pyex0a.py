# ဒီChapter ရဲ့ ရည်ရွယ်ချက် (DevOps Perspective)
# DevOps လောကမှာ ဒီChapter က အခြေခံအုတ်မြစ် ပါ။

# DevOps မှာ List က ဘာကြောင့်အရေးကြီးသလဲ?

# Container တွေရဲ့ IP Address စာရင်း သိမ်းဖို့

# Service တွေရဲ့ Log လိုင်းတွေ စုဆောင်းဖို့

# Environment Variables တွေ စီမံဖို့

# API Response က JSON Array တွေ ကိုင်တွယ်ဖို့


spam = ['cat', 'bat', 'rat', 'elephant']
# print(spam[0])   # Output: 'cat' (ပထမတန်ဖိုး)
# print(spam[1])   # Output: 'bat'      (ဒုတိယ)
# print(spam[2])   # Output: 'rat'      (တတိယ)
# print(spam[3])   # Output: 'elephant' (နောက်ဆုံး)



# print(spam[-1])   # Output: 'elephant' (နောက်ဆုံးတန်ဖိုး)
# print(spam[-2])   # Output: 'rat'      (နောက်ဆုံးမှ ဒုတိယ)
# print(spam[-3])   # Output: 'bat'      (နောက်ဆုံးမှ တတိယ)
# print(spam[-4])   # Output: 'cat'      (နောက်ဆုံးမှ စတုတ္ထ)

logs = [
    '2024-01-01 10:00:00 INFO Service started',
    '2024-01-01 10:05:00 WARN Memory high',
    '2024-01-01 10:10:00 ERROR Connection failed'
]
last_log = logs[-1]  # နောက်ဆုံး log ကိုယူတယ်
# print(last_log)      # '2024-01-01 10:10:00 ERROR Connection failed'


spam = ['cat', 'bat', 'rat', 'elephant']

# spam[start:end] - end က မပါဝင်ဘူး
# print(spam[1:3])   # Output: ['bat', 'rat'] (index 1 ကနေ 2 အထိ)
# print(spam[0:4])   # Output: ['cat', 'bat', 'rat', 'elephant']
# print(spam[1:])    # Output: ['bat', 'rat', 'elephant'] (အဆုံးထိ)
# print(spam[:2])    # Output: ['cat', 'bat'] (အစကနေ index 1 အထိ)
# print(spam[:])     # Output: ['cat', 'bat', 'rat', 'elephant'] (အကုန်လုံး)
# spam[3] = 'giraffe'  # index 3 ကို ပြောင်းလဲခြင်း
# print(spam[-2:])   # Output: ['rat', 'giraffe'] (နောက်ဆုံး ၂ လိုင်း)
# နောက်ဆုံး ၃ လိုင်း log ကိုယူဖို့
logs = ['log1', 'log2', 'log3', 'log4', 'log5', 'log6']
last_3_logs = logs[-3:]  # ['log4', 'log5', 'log6']

# ပထမ ၂ လိုင်းကိုယူဖို့
first_2_logs = logs[:2]  # ['log1', 'log2']
print(len(logs))

# Container list အရေအတွက် စစ်ဖို့
containers = ['nginx', 'mysql', 'redis', 'app']
print(f"Total containers: {len(containers)}")  # Total containers: 4

# တန်ဖိုးပြောင်းခြင်း (Container အမည်ပြင်ခြင်း)
containers[2] = 'redis-cache'
print(containers)  # ['nginx', 'mysql', 'redis-cache', 'app']


spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]  # index 2 က 'rat' ကိုဖျက်တယ်
print(spam)  # Output: ['cat', 'bat', 'elephant']


supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# supplies=[1,2,3,4]
# for item in supplies:
#     print(item)
    
# for i in range(len(supplies)):
#     print(f"{i}: {supplies[i]}")
    
    
# my_pets = ['Zophie', 'Pooka', 'Fat-tail']
# print('Zophie' in my_pets)      # True
# print('Simon' in my_pets)       # False
# print('Simon' not in my_pets)   # True  

# # Multiple Assignment & enumerate()

# cat = ['fat', 'gray', 'loud', 'loves to sleep']
# size, color, disposition, personality = cat
# print(size)        # 'fat'
# print(color)       # 'gray'
# print(disposition) # 'loud'
# print(personality)  # 'loves to sleep'


# people = ['Alice', 'Bob', 'Charlie']
# student,teacher,admin = people
# print(student)  # 'Alice'
# print(teacher)  # 'Bob' 
# print(admin)    # 'Charlie'


supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for index, item in enumerate(supplies):
    # print(f'Index {index} in supplies is: {item}')
    
    
# for item in supplies:
#     print(f'Item in supplies is: {item}')

# for i in range(len(supplies)):
#     print(f'Index {i} in supplies is: {supplies[i]}'    )

# for index, item in enumerate(supplies):
#     print(f'Index {index} in supplies is: {item}')
    
    
import random
print(random.choice(['apple', 'banana', 'cherry']))  # Randomly prints one of the fruits



people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)  # ['Carol', 'David', 'Alice', 'Bob'] (ရောကုန်တယ်)



# Load balancer အတွက် random server ရွေးတယ်
servers = ['server-1', 'server-2', 'server-3', 'server-4']
selected = random.choice(servers)
print(f"Routing request to: {selected}")

# Server list ကို shuffle လုပ်ပြီး rolling update အတွက်သုံး
random.shuffle(servers)
print(f"Update order: {servers}")
# chan= "hello"
# chan *= 2
# print(chan)  # Output: 'hellohello'

# List concatenation
my_list = ['a', 'b']
my_list += ['c', 'd']  # ['a', 'b', 'c', 'd']

# List replication
my_list *= 2  # ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
print(my_list)  # Output: ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']

# Environment variables တွေထည့်တယ်
env_vars = ['PATH=/usr/bin', 'HOME=/root']
env_vars += ['USER=admin', 'SHELL=/bin/bash']
print(env_vars)

# Server list ကို duplicate လုပ်တယ်
servers = ['web-1', 'web-2']
servers *= 3  # ၃ ခါထပ်တယ်
print(servers)  # ['web-1', 'web-2', 'web-1', 'web-2', 'web-1', 'web-2']

fruits = ['apple', 'banana', 'cherry'] # Randomly prints one of the fruits
fruits.insert(0,fruits[1])  # index 0 မှာ banana ထည့်တယ်
print(fruits)  # Output: ['banana', 'apple', 'banana', 'cherry']
fruits.append('cherry')  # နောက်ဆုံးမှာ cherry ထည့်တယ်
print(fruits)  # Output: ['banana', 'apple', 'banana', 'cherry', 'cherry']
fruits.remove('apple')  # 'apple' ကိုဖျက်တယ်
print(fruits)  # Output: ['banana', 'banana', 'cherry', 'cherry']
# fruits.pop()  # နောက်ဆုံးတန်ဖိုးကိုဖျက်တယ်
print(fruits.index('cherry'))



spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)  # [-7, 1, 2, 3.14, 5]

# စာလုံးစီခြင်း (ASCIIbetical order - မှတ်ထားရမယ်)
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)  # ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']

# ပုံမှန်အက္ခရာစဉ်အတိုင်းစီဖို့
spam.sort(key=str.lower)
print(spam)  # ['Alice', 'ants', 'badgers', 'Bob', 'Carol', 'cats']

meta = ['cat', 'chicken', 'dog', 'moose']
meta.reverse()
print(meta) 


import random

messages = [
    'It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]

print(messages[random.randint(0, len(messages) - 1)])



# list နဲ့ string ကြားတူညီချက် 
name="chankhine"
print(name[0])
print(name[4:])
print('chan' in name)


# ကွာခြားချက် - Mutable vs Immutable

# List က Mutable (ပြောင်းလို့ရ)
spam = ['cat', 'bat', 'rat']
spam[1] = 'chicken'  # OK
print(spam)  # ['cat', 'chicken', 'rat']

# String က Immutable (မပြောင်းရ)
name = 'Zophie'
# name[0] = 'z'  # ERROR! ဒါကိုမလုပ်ရ 

# Tuple က parentheses () နဲ့
eggs = ('hello', 42, 0.5)
print(eggs[0])    # 'hello' (index သုံးလို့ရ)
print(eggs[1:3])  # (42, 0.5) (slice သုံးလို့ရ)

# Tuple က Immutable (မပြောင်းရ)
# eggs[1] = 99   # ERROR!

# Tuple ဘယ်ချိန်သုံးလဲ 
# မပြောင်းသင့်တဲ့ data (ဥပါဒ် - Database credentials)

# Dictionary key အနေနဲ့သုံးချင်

# ကုဒ်ဖတ်ရလွယ်အောင် (မပြောင်းဘူးဆိုတာသိစေချင်)


# List variable က List ကိုတိုက်ရိုက်မသိမ်းဘူး။ Reference (လိပ်စာ) ကိုသိမ်းတယ်။


spam = [0, 1, 2, 3, 4, 5]
cheese = spam  # reference ကို copy လုပ်တယ်

cheese[1] = 'Hello!'  # spam ကိုပါပြောင်းသွားစေတယ်
# print(spam)   # [0, 'Hello!', 2, 3, 4, 5]
# print(cheese) # [0, 'Hello!', 2, 3, 4, 5]



# ဒီလိုမျိုး Bug တွေဖြစ်တတ်တယ်
def add_container(container_list, new_container):
    container_list.append(new_container)
    return container_list

production_containers = ['nginx', 'mysql']
staging_containers = production_containers  # Reference!
staging_containers.append('redis')

print(production_containers)  # ['nginx', 'mysql', 'redis'] (ပြောင်းသွားတယ်!)
print(add_container(production_containers, 'postman'))



#same c++ address pointer


eggs = ['cat', 'dog']
print(id(eggs))  # 35152584 (Memory address)

eggs.append('moose')  # တူညီတဲ့ list ကိုပြောင်းတာ
print(id(eggs))  # 35152584 (အတူတူပဲ)

eggs = ['bat', 'rat']  # အသစ်ဖန်တီးတာ
print(id(eggs))  # 44409800 (မတူဘူး)


import copy
# Reference ဆိုတာ
# List variable က List ကိုတိုက်ရိုက်မသိမ်းဘူး။ Reference (လိပ်စာ) ကိုသိမ်းတယ်။

# reference မာ ပြင်လိုက်ရင် မူရင်းမာပါ ပြောင်းနိုင်တယ် ဒီတော့ ပြင်ချင်ရင် copy() ကို သုံးပါ 

spam = [0, 1, 2, 3, 4, 5]

spam = [0, 1, 2, 3, 4, 5]
cheese = spam  # reference ကို copy လုပ်တယ်

cheese[1] = 'Hello!'  # spam ကိုပါပြောင်းသွားစေတယ်
print(spam)   # [0, 'Hello!', 2, 3, 4, 5]
print(cheese) # [0, 'Hello!', 2, 3, 4, 5]

cheese = copy.copy(spam)  # New list ဖန်တီးတယ်
cheese = spam 
cheese[1] = 'Hello!'

print(spam)   # [0, 1, 2, 3, 4, 5] (မပြောင်းဘူး)
print(cheese) # [0, 'Hello!', 2, 3, 4, 5]


# List ထဲမှာ List ပါရင် သုံးရမယ်


spam = [[1, 2], [3, 4]]
cheese = copy.deepcopy(spam)  # အတွင်းက List ပါ copy လုပ်တယ်
cheese[0][0] = 99
# copy.copy() = Shallow copy (အပေါ်ယံ - အပြင်ဘက် list ကိုပဲ copy)

# copy.deepcopy() = Deep copy (အတွင်းက nested structures ပါ copy)

# Nested list ပါရင် deepcopy() သုံး၊ မပါရင် copy() သုံး
print(spam)   # [[1, 2], [3, 4]] (မပြောင်းဘူး)
print(cheese) # [[99, 2], [3, 4]]

deployment = {
    'metadata': {'name': 'app', 'namespace': 'default'},
    'spec': {
        'replicas': 3,
        'containers': [
            {'name': 'app', 'image': 'app:v1'},
            {'name': 'sidecar', 'image': 'sidecar:v1'}
        ]
    }
}

# Staging အတွက် copy လုပ်တယ်
staging_deployment = copy.deepcopy(deployment)
staging_deployment = copy.copy(deployment)
print(f"statging : {staging_deployment}")
# staging_deployment['spec']['containers'][0]['image'] = 'app:staging'
# staging_deployment['spec']['containers'][1]['image'] = 'sidecar:staging'

# print(deployment['spec']['containers'][0]['image'])  # 'app:v1' (မပြောင်းဘူး)
# print(staging_deployment['spec']['containers'][0]['image'])  # 'app:staging'

prod = ['nginx', 'mysql']
# staging = copy.copy(prod)  # copy လုပ်ဖို့မမေ့နဲ့
staging = prod.copy()
staging.append('redis')
print(prod)  

lst = [1, 2]
lst.append([3, 4])  # [1, 2, [3, 4]]

# extend() - adds multiple items
lst = [1, 2]
lst.extend([3, 4])  # [1, 2, 3, 4]

#copy.copy(): #Shallow copy - အပြင်ဘက် list ကိုပဲ copy

#copy.deepcopy(): Deep copy - inner structures ပါ copy

# nested list ပါရင် deepcopy() သုံး

# List comprehension သုံးပြီး list ကို generate လုပ်နိုင်တယ်


squares = [x**2 for x in range(10)]
# Equivalent to:
squares = []
for x in range(10):
    squares.append(x**2)
    # print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Dictionary ဖန်တီးနည်း - curly braces {} နဲ့
my_cat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

# Key နဲ့ Value ကိုယူခြင်း
print(my_cat['size'])   # 'fat'
print(my_cat['color'])  # 'gray'

# Integer key လည်းသုံးလို့ရ
spam = {12345: 'Luggage Combination', 42: 'The Answer'}
print(spam[42])  # 'The Answer'


# Key က Index နေရာမှာ သုံးတယ် (List က integer ပဲသုံးလို့ရ၊ Dictionary က ဘယ် type မဆိုရ)

# Key-Value Pair က Dictionary ရဲ့ အခြေခံအဆောက်အအုံ

# Mutable (ပြောင်းလို့ရ) - List နဲ့တူပဲ


server_config = {
    'host': 'localhost',      # String key
    'port': 8080,             # Integer value
    'debug': True,            # Boolean value
    'timeout': 30.5           # Float value
}
print(server_config)

server_config = {
    'host': 'localhost',      # String key
    'port': 8080,             # Integer value
    'debug': True,            # Boolean value
    'timeout': 30.5           # Float value
}
print(server_config)


print(f"Host: {server_config['host']}")      # Host: localhost


status_codes = {
    200: 'OK',
    404: 'Not Found',
    500: 'Internal Server Error'
}
print(f"Status 200: {status_codes[200]}")    # Status 200: OK

# 4. Mixed type keys
mixed_dict = {
    'name': 'server1',        # String key
    42: 'answer',             # Integer key
    (1, 2): 'tuple key'       # Tuple key (immutable)
}

print(f"Tuple Key: {mixed_dict[(1, 2)]}")  # Tuple Key: tuple key



config = {'host': 'localhost', 'port': 8080}
try:
    print(config['timeout'])  # Key doesn't exist
except KeyError as e:
    print(f"❌ KeyError: {e}")



# 6. Better way - Using get()
# print(f"Using get(): {config.get('timeout', 30)}")
print(f"hello {config.get('chan',40)}")


services = {
    'api-gateway': {'port': 8080, 'health': '/health'},
    'auth-service': {'port': 8081, 'health': '/ping'},
    'user-service': {'port': 8082, 'health': '/status'}
}

# Access service info
auth = services.get('api-gateway')
if auth:
    print(f"Auth service port: {auth['health']}")
else:
    print("Auth service not found")
    
    
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
print(list(eggs))  # ['name', 'species', 'age']
print(list(eggs.values()))  # dict_values(['Zophie', 'cat', '8'])


env_vars = {}
env_vars['PATH'] = '/usr/bin:/bin'
env_vars['HOME'] = '/root'
env_vars['USER'] = 'admin'
env_vars['SHELL'] = '/bin/bash'

for key, value in env_vars.items():
    print(f"export {key}={value}")
# export PATH=/usr/bin:/bin
# export HOME=/root
# export USER=admin
# export SHELL=/bin/bash

config = {}
config['host'] = 'localhost'
config['port'] = 8080
config['debug'] = True
config['timeout'] = 30


for key, value in config.items():
    print(f"config {key}: {value}")
    
# keys(), values(), items() Methods


# ============================================
# keys(), values(), items() Methods
# ============================================

# 1. Dictionary setup
server = {
    'name': 'web-1',
    'ip': '10.0.1.10',
    'status': 'running',
    'cpu': 45.5,
    'memory': 2048
}
print(f"Server: {server}")

# 2. keys() - Keys တွေကိုယူ
print("\n=== keys() ===")
keys = server.keys()
print(f"Keys: {keys}")
print(f"Keys as list: {list(keys)}")
# ['name', 'ip', 'status', 'cpu', 'memory']

# 3. values() - Values တွေကိုယူ
print("\n=== values() ===")
values = server.values()
print(f"Values: {values}")
print(f"Values as list: {list(values)}")
# ['web-1', '10.0.1.10', 'running', 45.5, 2048]

# 4. items() - Key-Value pairs တွေကိုယူ
print("\n=== items() ===")
items = server.items()
print(f"Items: {items}")
print(f"Items as list: {list(items)}")
# [('name', 'web-1'), ('ip', '10.0.1.10'), ('status', 'running'), ('cpu', 45.5), ('memory', 2048)]

# 5. Loop with keys()
print("\n=== Loop with keys() ===")
for key in server.keys():
    print(f"Key: {key}")

# 6. Loop with values()
print("\n=== Loop with values() ===")
for value in server.values():
    print(f"Value: {value}")

# 7. Loop with items() - Multiple assignment
print("\n=== Loop with items() ===")
for key, value in server.items():
    print(f"{key}: {value}")

# 8. ⚠️ dict_keys, dict_values, dict_items are view objects
# They reflect changes to the dictionary
print("\n=== View Objects Reflect Changes ===")
view = server.keys()
print(f"Before: {list(view)}")
server['new_key'] = 'new_value'
print(f"After: {list(view)}")  # 'new_key' appears

# 9. DevOps လက်တွေ့ - Config validation
print("\n=== Config Validation ===")
required_keys = ['name', 'ip', 'status']
server_config = {
    'name': 'web-1',
    'ip': '10.0.1.10',
    'status': 'running',
    'cpu': 45.5
}

missing_keys = [key for key in required_keys if key not in server_config.keys()]
if missing_keys:
    print(f"❌ Missing keys: {missing_keys}")
else:
    print("✅ All required keys present")

# 10. Dictionary to list conversion
print("\n=== Convert to List ===")
server_list = list(server.items())
print(f"Server items as list: {server_list}")


# Key စစ်ဖို့ key in dict က အတိုဆုံးနည်း

# Value စစ်ဖို့ value in dict.values() သုံး

# not in က မရှိဘူးဆိုရင် True ပြန်

spam = {'name': 'Zophie', 'age': 7}

# Key ရှိမရှိစစ်
print('name' in spam)        # True (shorthand)
print('name' in spam.keys()) # True (explicit)
print('color' in spam)       # False

# Value ရှိမရှိစစ်
print('Zophie' in spam.values())  # True
print('Zophie' not in spam.values())  # False


picnic_items = {'apples': 5, 'cups': 2}

# Key ရှိရင် value ပြန်
print(picnic_items.get('cups', 0))   # 2

# Key မရှိရင် default ပြန်
print(picnic_items.get('eggs', 0))   # 0

# ⚠️ Without get() - KeyError


spam = {'name': 'Pooka', 'age': 5}

# Key မရှိရင် set
spam.setdefault('color', 'black')  # 'black'
print(spam)  # {'name': 'Pooka', 'age': 5, 'color': 'black'}

# Key ရှိပြီးသားဆို မပြောင်း
spam.setdefault('color', 'white')  # 'black' (returns existing)
print(spam)  # {'name': 'Pooka', 'age': 5, 'color': 'black'}