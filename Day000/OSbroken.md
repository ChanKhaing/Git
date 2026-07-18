

---

# 📝 Linux Networking Troubleshooting Note (2026-07-18)

## 📌 Executive Summary (အကျဉ်းချုပ်)

Rocky Linux VM တွင် NetworkManager configuration များ လွဲမှားပြင်ဆင်မိပြီး Network အသုံးမပြုနိုင်တော့ဘဲ OS ပျက်စီး (Broken) သွားခဲ့သည်။ စက်အသစ်ပြန်တင်ပြီး NAT mode ပြောင်းလဲကာ IP address (`192.168...`) ပြန်လည်ရရှိအောင် ဖြေရှင်းနိုင်ခဲ့သည်။

---

## ❌ 1. Root Causes of Failure (ပျက်စီးသွားရသည့် အဓိကအကြောင်းရင်းများ)

### A. The Autoconnect Trap

`/etc/NetworkManager/system-connections/enp0s3.nmconnection` ဖိုင်ထဲတွင် အောက်ပါအတိုင်း ပြင်ဆင်မိခဲ့ခြင်း -

```ini
autoconnect-priority=-999

```

* **ပြဿနာ:** NetworkManager ကို priority အနိမ့်ဆုံး သတ်မှတ်လိုက်သဖြင့် OS မှ အဆိုပါ network card ကို လုံးဝ အသိအမှတ်မပြုဘဲ ပစ်ထားလိုက်သည်။

### B. Missing UUID

* **ပြဿနာ:** ဖိုင်ထဲတွင် `uuid=` နေရာ၌ မည်သည့် hex string မှ ရှိမနေခဲ့သဖြင့် NetworkManager က စနစ်တကျ profile အဖြစ် မဖတ်နိုင်ခဲ့ပါ။

### C. OS Bloat from Multiple Trials

* **ပြဿနာ:** ကွန်နက်ရှင်ပြန်ရရန် နည်းလမ်းမျိုးစုံ၊ command မျိုးစုံဖြင့် အကြိမ်ကြိမ် ဇွတ်ပြင်ဆင်ခဲ့သဖြင့် NetworkManager service နှင့် core configuration များ တစ်ခုနှင့်တစ်ခု ငြိပြီး OS ပါ ခေါ်မရအောင် Broken ဖြစ်သွားခဲ့သည်။

---

## 💡 2. Lessons Learned (ရရှိခဲ့သည့် သင်ခန်းစာများ)

1. **Clone First:** နောက်တစ်ကြိမ် မသိသေးသော Network Setting များကို မစမ်းသပ်မီ VM ကို မဖြစ်မနေ **Clone** ပြုလုပ်ထားရန် သို့မဟုတ် **Snapshot** ရိုက်ထားရန်။
2. **File Permissions:** Network config ဖိုင်များကို ကိုယ်တိုင် manually ပြင်ပြီးပါက permission ကို `sudo chmod 600` ပြန်ပြောင်းပေးရမည်။ (မပြောင်းပါက လုံခြုံရေးအရ Linux က ဖတ်မည်မဟုတ်)
3. **Hypervisor Mode:** VM များတွင် Bridged မုဒ်သည် ပြင်ပ router အခြေအနေပေါ်မူတည်၍ IP မကျတတ်သဖြင့် စမ်းသပ်ရန် **NAT Mode** သည် အစိတ်ချရဆုံး ဖြစ်သည်။

---

## 🛠️ 3. Standard Recovery Flow (နောက်နောင် သုံးရမည့် အဆင့်ဆင့် ပြင်ဆင်နည်း)

အကယ်၍ configuration မှားယွင်းပါက စက်မဖျက်မီ အောက်ပါအတိုင်း dynamic IP ရအောင် ပြန်ပြင်မည် -

```bash
# ၁။ Clean Config ဖြည့်သွင်းခြင်း
sudo nano /etc/NetworkManager/system-connections/enp0s3.nmconnection

# အောက်ပါ setting အတိုင်း သေချာပါစေ -
# [connection]
# autoconnect=true
# (autoconnect-priority လိုင်းရှိရင် ဖျက်ပစ်ပါ သို့မဟုတ် 0 ထားပါ)

# ၂။ Permission ပြန်ပြင်ခြင်း
sudo chmod 600 /etc/NetworkManager/system-connections/enp0s3.nmconnection

# ၃။ Network Service ကို Refresh ဖြစ်အောင် ကန်ချခြင်း
sudo nmcli connection reload
sudo nmcli connection down enp0s3
sudo nmcli connection up enp0s3

# ၄။ IP Address ကျ/မကျ ပြန်စစ်ခြင်း
ip address show enp0s3

```

---

