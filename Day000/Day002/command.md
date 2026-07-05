💻 ၂။ commands.md (စနစ်တကျ ပြင်ဆင်ထားသော Linux Commands များ)
Markdown
# SSH Key Generation and Remote Login Workflow

အောက်ပါတို့သည် SSH Key Pair ဆောက်ခြင်းမှစ၍ ဆာဗာပေါ်သို့ Key လှမ်းတင်ပြီး Login ဝင်သည်အထိ အသုံးပြုရမည့် စံနှုန်းကိုက် Linux အမိန့် (Commands) များ ဖြစ်ကြသည်။

### ၁။ SSH Key Pair တည်ဆောက်ခြင်း (Client စက်တွင် လုပ်ရန်)
```bash
# RSA algorithm အသုံးပြုပြီး 2048-bit ရှိသော Key ဆောက်ခြင်း (Passphrase ထည့်ရန် မမေ့ပါနှင့်)
ssh-keygen -t rsa -b 2048

# တည်ဆောက်ပြီးပါက Key ဖိုင်များ သွားရောက်သိမ်းဆည်းသည့်နေရာ
# Root အသုံးပြုသူဖြစ်ပါက: /root/.ssh/
# သာမန်အသုံးပြုသူဖြစ်ပါက: /home/username/.ssh/
၂။ သော့ဖိုင်များ၏ လုံခြုံရေးခွင့်ပြုချက် (Permission) သတ်မှတ်ခြင်း
Bash
# မည်သူမျှ ကြားဖြတ်မဖတ်နိုင်စေရန် ကန့်သတ်ခြင်း
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa
၃။ Public Key ကို ဆာဗာပေါ်သို့ လှမ်းတင်ခြင်း (Upload to Server)
Bash
# ဆာဗာ၏ IP နှင့် အသုံးပြုသူအမည်ထည့်၍ ရိုက်ပါ။ (ဤအဆင့်တွင် ဆာဗာ၏ Password ကို တစ်ကြိမ်ရိုက်ရမည်)
ssh-copy-id -i ~/.ssh/id_rsa.pub username@server_ip_address
၄။ Password မလိုဘဲ SSH ဖြင့် အဝေးမှ လော့ဂ်အင်ဝင်ခြင်း (Remote Login)
Bash
# သတ်မှတ်ထားသော Private Key ကို သုံး၍ ချိတ်ဆက်ခြင်း
ssh -i ~/.ssh/id_rsa username@server_ip_address
၅။ ချိတ်ဆက်မှု အောင်မြင်ကြောင်း စစ်ဆေးခြင်း
Bash
# ဆာဗာထဲ ရောက်ရှိသွားပါက လက်ရှိရောက်နေသော စက်၏ IP ကို စစ်ဆေးရန်
ifconfig

# စက်၏ OS အမျိုးအစားကို စစ်ဆေးရန်
cat /etc/os-release