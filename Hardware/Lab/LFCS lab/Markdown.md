Markdown
# LFCS Exam Lab Practice & Troubleshooting Guide

ဤ Repository သည် Linux Foundation Certified System Administrator (LFCS) စာမေးပွဲအတွက် ကျွန်ုပ်၏ လက်တွေ့လေ့ကျင့်မှုများနှင့် ကြုံတွေ့ရသော ပြဿနာများကို ဖြေရှင်းနည်းမှတ်တမ်းများ ဖြစ်သည်။

## 🚀 Environment Setup (စတင်ရန်လမ်းညွှန်)

Lab ကို စတင်အသုံးပြုရန် အောက်ပါအဆင့်များကို လိုက်နာပါ -

1. PowerShell ကို Administrator Mode ဖြင့်ဖွင့်ပြီး Lab Folder ထဲသို့ သွားပါ။
   ```powershell
   cd C:\Users\User\Desktop\lfcs-exam-lab
Vagrant ကို စတင်နှိုးပါ။

PowerShell
vagrant up
Tip: အကယ်၍ vagrant up အလုပ်မလုပ်ပါက Folder ထဲတွင် Shift + Right-Click နှိပ်ပြီး "Open in Terminal" ကို အသုံးပြုပါ။

🛠 Troubleshooting (ပြဿနာဖြေရှင်းနည်းများ)
Lab လုပ်တဲ့အခါ အသုံးများသော Error များအတွက် -

1. PowerShell Execution Policy Error
Script များ အလုပ်မလုပ်ပါက အောက်ပါ Command ကို သုံးပါ။

PowerShell
powershell -ExecutionPolicy Bypass -File .\lfcs.ps1
2. Snapshot/Machine Missing Error
Machine အဟောင်းများကို ရှာမတွေ့ပါက သို့မဟုတ် Snapshot Error တက်ပါက Setup ကို ပြန်လည် run ပေးပါ။

PowerShell
.\setup.ps1
ပြီးပါက .\lfcs.ps1 ကို ပြန်လည်အသုံးပြုပါ။


Ubuntu စက်ထဲ ဝင်ချင်ရင်:

PowerShell
vagrant ssh node1
Rocky Linux စက်ထဲ ဝင်ချင်ရင်:

PowerShell
vagrant ssh lfcs-rocky1

Task Documentation: q009 (Create a constrained user account)
Target Node: lfcs-node1 (Access via SSH)

Objective: Create a user named examuser with a UID of 2401, standard /bin/bash shell, account expiry set to 2030-12-31, and secondary group membership in lfcp.

Execution Command:

Bash
vagrant@lfcs-node1:~$ sudo useradd -u 2401 -s /bin/bash -e 2030-12-31 examuser