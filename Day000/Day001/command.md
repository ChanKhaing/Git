---

### ၂။ `commands.md` (ဒီနေ့ တကယ် Run ခဲ့တဲ့ Linux Command များ)

# Linux Command Log

Lab တစ်ခုလုံးမှာ တစ်ဆင့်ချင်းစီ အမှန်တကယ် Run ခဲ့တဲ့ Linux CLI command များ ဖြစ်ပါတယ်။

### ၁။ လမ်းကြောင်း စစ်ဆေးခြင်းနှင့် ရှာဖွေခြင်း (Navigation)

# လက်ရှိ ရောက်နေတဲ့ လမ်းကြောင်းကို စစ်ဆေးခြင်း
pwd

# Home ရဲ့ Environment Variable ကို ကြည့်ခြင်း
echo $HOME

# Welcome စာသား ရိုက်နှိပ်ပြခြင်း
echo Welcome

# Git install လုပ်ထားသလား စစ်ဆေးခြင်းနှင့် Git help ကြည့်ခြင်း
git
git --help
man git


၂။ တိရစ္ဆာန်မျိုးခွဲ Folder များ တည်ဆောက်ခြင်း (Creation)
Bash
# bob ရဲ့ home directory ထဲသို့ ပြောင်းလဲဝင်ရောက်ခြင်း
cd /home/bob

# ရှိနေတဲ့ folder တွေကို ကြည့်ခြင်း
ls

# birds ဆိုတဲ့ folder ဆောက်ခြင်း
mkdir birds

# လမ်းကြောင်း ပြန်စစ်ခြင်း
pwd

# fish အောက်မှာ salmon ဆိုတဲ့ folder ပါ တစ်ခါတည်း ဆောက်ခြင်း (-p သုံး၍)
mkdir -p fish/salmon

# စစ်ဆေးခြင်း
ls

# Brace Expansion သုံးပြီး mammals အောက်မှာ elephant ရော monkey ရော တစ်ပြိုင်နက် ဆောက်ခြင်း
mkdir -p mammals/{elephant,monkey}

# ဆောက်ထားတဲ့ folder တွေကို အသေးစိတ် စစ်ဆေးခြင်း
ls -l mammals

# reptile အောက်မှာ snake နဲ့ frog ကို တစ်ခါတည်း ဆောက်ခြင်း
mkdir -p reptile/{snake,frog}
၃။ Folder ပြုပြင်ခြင်းနှင့် ပြန်လည်ဖျက်သိမ်းခြင်း (Modification & Deletion)
Bash
# လက်ရှိ ရှိသမျှ folder အားလုံးကို စစ်ဆေးခြင်း
ls

# reptile folder ရဲ့ အထဲကို အသေးစိတ် ကြည့်ခြင်း
ls -l reptile

# reptile folder ထဲသို့ ဝင်ခြင်း
cd reptile

# snake folder ကို crocodile လို့ နာမည်ပြောင်းလဲခြင်း
mv snake ./crocodile

# နာမည်ပြောင်းသွားတာ သေချာလား စစ်ဆေးခြင်း
ls

# မူလ home directory သို့ ပြန်ထွက်ခြင်း
cd

# reptile folder နဲ့ သူ့အထဲက ဖိုင်/folder အားလုံးကို အကုန် ဖျက်ပစ်ခြင်း
rm -r reptile

# reptile folder မရှိတော့တာ သေချာအောင် ပြန်စစ်ခြင်း
ls

# ဒီနေ့ သုံးခဲ့သမျှ command history အားလုံးကို ထုတ်ကြည့်ခြင်း
history