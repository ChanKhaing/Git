# Linux Filesystem Structure & Directory Manipulation Lab

ဒီနေ့မှာတော့ Linux CLI (Command Line Interface) ကို အသုံးပြုပြီး Directory (Folder) တွေ တည်ဆောက်ခြင်း၊ လမ်းကြောင်းရှာဖွေခြင်းနဲ့ မလိုလားအပ်တဲ့ Folder တွေကို ပြန်လည် ဖျက်သိမ်းခြင်းဆိုင်ရာ အခြေခံ အယူအဆတွေကို လက်တွေ့ လေ့လာခဲ့ပါတယ်။

## 🛠️ တတ်မြောက်ခဲ့သည့် ကျွမ်းကျင်မှုများ (Skills)
* **လမ်းကြောင်း ရှာဖွေခြင်း:** `cd`, `pwd`
* **Folder အသစ် ဆောက်ခြင်း:** `mkdir` နှင့် မိခင် Folder ပါ တစ်ခါတည်း ဆောက်သည့် `mkdir -p` 
* **အမြန် Folder ဆောက်ခြင်း:** Bash Brace Expansion (`{folder1,folder2}`) ကို သုံးပြီး တစ်ကြိမ်တည်းနဲ့ Folder အများကြီး ဆောက်ခြင်း
* **စစ်ဆေးခြင်း:** Folder ထဲမှာ ဘာတွေရှိလဲ ကြည့်ရှုခြင်း (`ls`, `ls -l`)
* **အမည်ပြောင်းလဲခြင်း/ရွှေ့ပြောင်းခြင်း:** `mv` command သုံးခြင်း
* **ဖျက်သိမ်းခြင်း:** Folder တစ်ခုလုံးကို ၎င်းအထဲရှိ ဖိုင်များအပါအဝင် အကုန်ဖျက်ခြင်း (`rm -r`)
* **အသုံးပြုခဲ့သမျှ မှတ်တမ်းကြည့်ခြင်း:** `history`

## 📂 တည်ဆောက်ခဲ့သည့် Folder တည်ဆောက်ပုံ (Directory Structure)
Lab ရဲ့ ရည်ရွယ်ချက်အတိုင်း `/home/bob` အောက်မှာ အောက်ပါ တိရစ္ဆာန်မျိုးခွဲခြားမှုပုံစံ Folder Structure ကို ဆောက်ခဲ့ပါတယ် -

```text
/home/bob
├── amphibian
│   └── salamander
├── birds
│   └── eagle
├── fish
│   └── salmon
├── mammals
│   ├── elephant
│   └── monkey
└── reptile (ဆောက်ပြီး၊ ပြုပြင်ပြီးနောက် ပြန်ဖျက်ခဲ့သည်)
    ├── frog
    └── snake -> (crocodile ဟု ပြောင်းလဲခဲ့သည်)