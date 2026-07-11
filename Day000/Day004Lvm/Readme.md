# Linux File System Hierarchy Standard (FHS)

Linux System တစ်ခုလုံးရဲ့ File System တည်ဆောက်ပုံ မြေပုံညွှန်းနှင့် အခြေခံမှတ်စုများ။

## `/` (Root Directory)
Linux File System တစ်ခုလုံးရဲ့ **ပင်မ အရင်းအမြစ် (Main Directory)** ဖြစ်သည်။ အခြား Directory အားလုံးသည် ၎င်း၏ အောက်တွင်သာ တည်ရှိသည်။

---

## Directories နှင့် ၎င်းတို့၏ လုပ်ဆောင်ချက်များ

### 📂 `/bin` & `/sbin` (Binaries & System Binaries)
*   **/bin:** ပုံမှန် User များ အသုံးပြုနိုင်သည့် မရှိမဖြစ် အခြေခံ User Commands များ (ဥပမာ- `ls`, `cd`, `mkdir`) တည်ရှိသည်။
*   **/sbin:** System Administrator များသာ အသုံးပြုသည့် System Commands များ ရှိသည်။ ပုံမှန်အားဖြင့် `sudo` ခွင့်ပြုချက်ဖြင့်သာ အသုံးပြုရသည့် Commands များ ပါဝင်သည်။
*   *မှတ်ချက်:* `/usr/bin` နှင့် `/usr/sbin` အောက်တွင်လည်း အလားတူ ခွဲခြားထားသော command များ ရှိသည်။

### 📂 `/boot` (Boot Loader Files)
*   ကွန်ပျူတာ စက်စတင်ပွင့်ချိန် (Boot တက်ချိန်) တွင် လိုအပ်သော Kernel ဖိုင်များနှင့် Bootloader ဖိုင်များ သိမ်းဆည်းထားသည့်နေရာ ဖြစ်သည်။

### 📂 `/dev` (Device Files)
*   Hard disk များ၊ USB Storage များ အစရှိသည့် Hardware Devices များကို ဖိုင်အသွင်ဖြင့် ပြသပေးထားသောနေရာ ဖြစ်သည်။
*   ၎င်းတို့ကို တိုက်ရိုက်ကြည့်ရှု၍ မရနိုင်ဘဲ `/media` သို့မဟုတ် `/mnt` ဆီသို့ **Mount** လုပ်ပြီးမှသာ ဝင်ရောက်အသုံးပြုနိုင်သည်။

### 📂 `/etc` (Configuration Files)
*   System တစ်ခုလုံးနှင့် သက်ဆိုင်သော **Configuration (ပြင်ဆင်သတ်မှတ်ချက်) ဖိုင်များ** ရှိသည်။ အင်တာနက်/Network configuration များ၊ Systemd ဝန်ဆောင်မှုဆိုင်ရာ configuration များ ဤနေရာတွင် ရှိသည်။

### 📂 `/home` & `/root` (User Directories)
*   **/home:** ပုံမှန် အသုံးပြုသူ (User) များ၏ ကိုယ်ပိုင် Profile နှင့် ဖိုင်များ ထားရှိရာ နေရာဖြစ်သည်။ (Windows ရှိ `C:\Users\` နှင့် တူညီသည်)။
*   **/root:** System တစ်ခုလုံး၏ အမြင့်ဆုံး အာဏာရှိသူ **Root User (Superuser)** ၏ သီးသန့် Home Directory ဖြစ်သည်။ လုံခြုံရေးအရ အခြား standard users များနှင့် မရောနှောဘဲ သက်သက်ခွဲထားခြင်း ဖြစ်သည်။

### 📂 `/lib` & `/lib64` (Shared Libraries)
*   Kernel ဖိုင်များ၊ Protocols များနှင့် System commands များ run ရန် လိုအပ်သော Shared Library Module ဖိုင်များ တည်ရှိသည်။

### 📂 `/media` & `/mnt` (Mount Points)
*   **/media:** USB, CD-ROM အစရှိသော အလိုအလျောက် mount ဖြစ်သည့် ယာယီ devices များအတွက် ဖြစ်သည်။
*   **/mnt:** Administrator မှ ၎င်းစိတ်ကြိုက် Hardware/File system များကို ကိုယ်တိုင် manually mount လုပ်ပြီး သုံးရန်အတွက် ဖြစ်သည်။

### 📂 `/opt` (Optional Applications)
*   Gnome ကဲ့သို့သော UI files များနှင့် ပြင်ပမှ ထည့်သွင်းထားသည့် လွတ်လပ်သော (Add-on/Optional) software packages များ ထားရှိရာနေရာ ဖြစ်သည်။

### 📂 `/proc` (Process Information)
*   လက်ရှိ System ပေါ်တွင် Run နေသော Process များ၏ အချက်အလက်များကို သိမ်းဆည်းထားသည့် Virtual File System ဖြစ်သည်။ CPU အသုံးပြုမှု၊ Memory ဘယ်လောက်သုံးနေလဲ အစရှိသည်တို့ကို ဤနေရာမှတစ်ဆင့် ဖတ်ရှုနိုင်သည်။

### 📂 `/sys` (System Files)
*   Kernel နှင့် Hardware devices ဆိုင်ရာ အချက်အလက်များကို စနစ်တကျ ပြသပေးထားသည့်နေရာ ဖြစ်သည်။

### 📂 `/tmp` (Temporary Files)
*   System နှင့် Applications များ အသုံးပြုနေစဉ် ခေတ္တလိုအပ်သော **ယာယီဖိုင် (Temporary Files)** များ ထားရှိရာ နေရာဖြစ်သည်။ စက်ပိတ်လိုက်လျှင် သို့မဟုတ် restart ချလျှင် ဤနေရာရှိ ဖိုင်များ ပျက်သွားလေ့ရှိသည်။

### 📂 `/srv` (Service Data)
*   စက်ထဲတွင် Web Server သို့မဟုတ် FTP Server အစရှိသည့် Server များ run ထားပါက ၎င်း Server များနှင့် ပတ်သက်သော data ဖိုင်များ ထားရှိရာနေရာ ဖြစ်သည်။

### 📂 `/var` (Variable Data)
*   စနစ်လည်ပတ်နေစဉ် အမြဲတမ်း ပြောင်းလဲနေတတ်သော ဖိုင်များ ရှိသည်။ အထူးသဖြင့် စနစ်၏ အဝင်အထွက် အခြေအနေများကို မှတ်တမ်းတင်ထားသည့် **Log Files** များကို ဤနေရာတွင် ကြည့်ရှုနိုင်သည်။

---
📅 *နောက်ဆုံးပြင်ဆင်သည့်ရက်စွဲ: 11.7.2026*