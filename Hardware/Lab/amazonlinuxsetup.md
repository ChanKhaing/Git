Amazon Linux VM Setup with Cloud-init (Seed.iso)
ဤလမ်းညွှန်သည် Amazon Linux cloud image (.qcow2) ကို virt-manager ဖြင့် Virtual Machine အဖြစ်တည်ဆောက်နည်းကို ရှင်းပြထားပါသည်။ Cloud-init မှတစ်ဆင့် ကနဦး Password နှင့် SSH authentication ကို သတ်မှတ်နိုင်မည် ဖြစ်သည်။

### အဆင့် ၁ – Cloud-init (Seed.iso) ဖိုင် ဆောက်ခြင်း
Amazon Linux သည် cloud image ဖြစ်သောကြောင့် ပုံမှန်အားဖြင့် Password မပါရှိပါ။ ထို့ကြောင့် login ဝင်ရန်အတွက် configuration CD တစ်ခု ဦးစွာဖန်တီးရမည်။

၁.၁ user-data ဖိုင် ဆောက်ခြင်း
Terminal ကိုဖွင့်ပြီး အောက်ပါ command ကို ရိုက်ထည့်ပါ။


nano user-data
ပွင့်လာသော screen တွင် အောက်ပါစာသားများကို ကူးထည့်ပါ (MySecurePass123 နေရာတွင် သင်နှစ်သက်ရာ password ပြောင်းလဲနိုင်သည်)။


#cloud-config
autotesting: true
users:
  - default
chpasswd:
  list: |
    ec2-user:MySecurePass123
  expire: False
ssh_pwauth: True
ပြီးလျှင် Ctrl + O (သိမ်းရန်) → Enter → Ctrl + X (ထွက်ရန်) နှိပ်ပါ။

၁.၂ meta-data ဖိုင် ဆောက်ခြင်း
ဖိုင်အလွတ်တစ်ခုကို အောက်ပါအတိုင်း ဆောက်ပါ။


touch meta-data
၁.၃ Seed.iso ဖိုင် ဖန်တီးခြင်း
ဖိုင်နှစ်ခုကို ISO အဖြစ် စုစည်းရန် အောက်ပါ command ကို လုပ်ဆောင်ပါ။


genisoimage -output seed.iso -volid cidata -joliet -rock user-data meta-data
အောင်မြင်ပါက သင့် directory တွင် seed.iso ဖိုင် ရရှိလာမည်။

### အဆင့် ၂ – Virtual Machine Manager တွင် VM သတ်မှတ်ခြင်း
Virtual Machine Manager ကိုဖွင့်ပါ။
ဘယ်ဘက်အပေါ်ရှိ New Virtual Machine (ကွန်ပျူတာပုံစံ icon) ကိုနှိပ်ပါ။
“Import existing disk image” ကိုရွေးပြီး Forward နှိပ်ပါ။
Storage box တွင် Browse ကိုနှိပ်ကာ သင်ဒေါင်းလုဒ်ဆွဲထားသော .qcow2 ဖိုင်ကို ရွေးချယ်ပါ။
Choose the operating system တွင် Red Hat Enterprise Linux 9 သို့မဟုတ် fedora ဟု ရိုက်ရှာပြီး ရွေးပါ (သို့မဟုတ် သင့်လျော်သော OS ကိုရွေးပါ)။ Forward နှိပ်ပါ။
Memory (RAM) နှင့် CPU သတ်မှတ်ပါ (ဥပမာ – RAM 2048 MB, CPU 2)။
နောက်ဆုံးအဆင့်တွင် VM အတွက် နာမည်ပေးပါ (ဥပမာ – amazon-linux)။
အရေးကြီး – Finish မနှိပ်မီ “Customize configuration before install” ဟူသော checkbox ကို အမှန်ခြစ်ပေးပါ။ ထို့နောက် Finish ကိုနှိပ်ပါ။
### အဆင့် ၃ – CDROM အဖြစ် Seed.iso ထည့်သွင်းပြီး VM စတင်ခြင်း
Finish နှိပ်ပြီးနောက် Configuration ပြောင်းလဲနိုင်သော window အသစ်တစ်ခု ပွင့်လာပါမည်။
ဘယ်ဘက်အောက်ခြေရှိ “Add Hardware” ခလုတ်ကို နှိပ်ပါ။
Storage ကိုရွေးပါ။
Device type drop-down menu တွင် Disk device မှ CDROM device သို့ပြောင်းပါ။
Manage (သို့မဟုတ် Browse Local) ကိုနှိပ်ကာ အဆင့် ၁ တွင်ဖန်တီးထားသော seed.iso ဖိုင်ကို ရွေးပြီး Finish နှိပ်ပါ။
ပင်မ Configuration window ၏ အောက်ခြေရှိ Apply ကိုနှိပ်ပါ။
ဘယ်ဘက်အပေါ်ဆုံးရှိ “Begin Installation” ကိုနှိပ်လိုက်ပါက VM စတင်အလုပ်လုပ်ပါမည်။
Login ဝင်ရန်
VM boot ဖြစ်ပြီးနောက် login screen တွင် အောက်ပါအတိုင်း ရိုက်ထည့်ပါ။
### 
Field	Value
Username	ec2-user
Password	အဆင့် 1 တွင် သင်သတ်မှတ်ခဲ့သော password (ဥပမာ – MySecurePass123)
မှတ်ချက် – ဤလမ်းညွှန်သည် virt-manager (Virtual Machine Manager) ကို အသုံးပြုထားပြီး Cloud-init ပုံစံဖြင့် Amazon Linux VM ကို စတင်တည်ဆောက်ရန် ရည်ရွယ်ပါသည်။