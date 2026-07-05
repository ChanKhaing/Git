# SSH Key-Based Authentication Learning Log

ဒီနေ့မှာတော့ SSH (Secure Shell) အသုံးပြုပြီး Server နဲ့ Client ကြား Password မလိုဘဲ ပိုမိုလုံခြုံစိတ်ချရတဲ့ Key-Based Authentication စနစ်ကို လက်တွေ့ စမ်းသပ်လေ့လာခဲ့ပါတယ်။

## 💡 အဓိက နားလည်သဘောပေါက်ခဲ့သည့် Concept များ
SSH Key စနစ်သုံးဖို့အတွက် သော့တွဲ (Key Pair) တစ်ခု တည်ဆောက်ရပါတယ်။
1. **Public Key (အများသုံးသော့):** ဆာဗာ (Server) ပေါ်သို့ တင်ပေးရမည့် သော့ဖြစ်ပြီး စက်ထဲရှိ `~/.ssh/id_rsa.pub` တွင် သိမ်းဆည်းသည်။
2. **Private Key (ကိုယ်ပိုင်သော့):** မိမိစက် (Client) ထဲမှာပဲ လျှို့ဝှက်သိမ်းဆည်းထားရမည့် သော့ဖြစ်ပြီး `~/.ssh/id_rsa` တွင် သိမ်းဆည်းသည်။

### 🔒 အရေးကြီးသော လုံခြုံရေးစည်းမျဉ်းများ (Security Best Practices)
* **Passphrase:** Private Key ကို သူတပါးအလွယ်တကူ မသုံးနိုင်စေရန် သော့တွဲဆောက်စဉ် Passphrase (Password) ခံရမည်။
* **Permissions:** လုံခြုံရေးအရ Key ဖိုင်များ၏ Permission ကို `600` (Owner သာ ဖတ်/ရေးပိုင်ခွင့်) ပေးထားရမည်။

<!-- ## 📸 ဓာတ်ပုံများမှ လက်တွေ့သုံးသပ်ချက် (Lab Observations)
* **Screenshot 2026-07-05 131508.jpg:** ရလဒ်အရ Oracle VirtualBox ပေါ်တွင် Linux OS နှစ်ခုကို Network ချိတ်ဆက်ကာ `ifconfig` ဖြင့် IP Address များ စစ်ဆေးခြင်းနှင့် ဆာဗာအချင်းချင်း Telnet/SSH ဆက်သွယ်ရန် ပြင်ဆင်နေမှုကို တွေ့ရသည်။
* **Screenshot 2026-07-05 164256.png:** `cat /etc/os-release` အမိန့်ဖြင့် စစ်ဆေးရာ အသုံးပြုထားသော OS မှာ **Rocky Linux 10.2 (Red Quartz)** ဖြစ်ကြောင်း အတည်ပြုနိုင်ပြီး၊ SSH ဖြင့် ဆာဗာသို့ အောင်မြင်စွာ ချိတ်ဆက်နိုင်ခဲ့သည်။ -->