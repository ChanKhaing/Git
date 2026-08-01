# 🌐 Networking & Cloud Foundation Study Notes (မြန်မာဘာသာ)

ဤ မှတ်စုသည် Cloud & DevOps လမ်းကြောင်းအတွက် လေ့လာခဲ့သော **Networking သဘောတရားများ၊ Subnetting တွက်ချက်မှုများ နှင့် Linux Command များ**ကို ပြန်လည်ကြည့်ရှုလေ့လာနိုင်ရန် စနစ်တကျ မှတ်တမ်းတင်ထားခြင်း ဖြစ်သည်။

---

## 📌 ၁။ Subnetting အခြေခံများ (FLSM & VLSM)

### 🔹 FLSM (Fixed Length Subnet Mask)
Network တစ်ခုကို အရွယ်အစား **ညီတူညီမျှ** ပိုင်းခြားခြင်းဖြစ်သည်။
* **Original Network:** `192.168.10.0/24` ကို Subnet ၄ ခု ညီတူညီမျှ ခွဲခြားခြင်း။
* **Subnet Mask:** `255.255.255.192` (`/26`)
* **Usable Hosts (သုံးစွဲနိုင်သော IP အရေအတွက်):** Subnet တစ်ခုလျှင် `62` ခု ရရှိမည်။

| Subnet | Subnet Address | IP Range (သုံးစွဲနိုင်သော IP) | Broadcast Address |
| :--- | :--- | :--- | :--- |
| **Subnet 1** | `192.168.10.0/26` | `192.168.10.1` - `192.168.10.62` | `192.168.10.63` |
| **Subnet 2** | `192.168.10.64/26` | `192.168.10.65` - `192.168.10.126` | `192.168.10.127` |
| **Subnet 3** | `192.168.10.128/26` | `192.168.10.129` - `192.168.10.190` | `192.168.10.191` |
| **Subnet 4** | `192.168.10.192/26` | `192.168.10.193` - `192.168.10.254` | `192.168.10.255` |

---

### 🔹 VLSM (Variable Length Subnet Mask)
ဌာနတစ်ခုချင်းစီ၏ **လိုအပ်သော Host အရေအတွက်ပေါ် မူတည်၍ IP များကို မတူညီသော အရွယ်အစားဖြင့် ခွဲခြားခြင်း** ဖြစ်သည်။ (IP လေလွင့်မှုကို လျှော့ချပေးသည်)
* **Original Network:** `172.16.0.0/24`

| Department | လိုအပ်သော Host | ရရှိသော Subnet | IP Range | Subnet Mask |
| :--- | :--- | :--- | :--- | :--- |
| **HR Dept** | 60 Hosts | `172.16.0.0/26` | `172.16.0.1` - `172.16.0.62` | `255.255.255.192` |
| **Sales Dept** | 25 Hosts | `172.16.0.64/27` | `172.16.0.65` - `172.16.0.94` | `255.255.255.224` |
| **IT Dept** | 12 Hosts | `172.16.0.96/28` | `172.16.0.97` - `172.16.0.110` | `255.255.255.240` |

---

## 📌 ၂။ Route Summarization (Supernetting)

**Route Summarization** ဆိုသည်မှာ ဆက်တိုက်ဖြစ်နေသော (Contiguous) Network များကို Summary Route တစ်ခုတည်းအဖြစ် ပေါင်းစည်းလိုက်ခြင်း ဖြစ်သည်။ Router ၏ Routing Table အရွယ်အစားကို သေးငယ်စေပြီး CPU/Memory သုံးစွဲမှုကို သက်သာစေသည်။

### အဓိက မှတ်သားရန် အချက်များ:
1. **Contiguous Networks:** Network များသည် စာရင်းဇယားအရ အစဉ်လိုက်/ဆက်တိုက် ဖြစ်နေရမည်။
2. **Binary Matching:** Binary level တွင် အစမှစ၍ တူညီသော Bit များကို ရေတွက်ခြင်းဖြင့် Summary Prefix Length ကို ရှာဖွေရသည်။
3. **Subnet Boundary Alignment:** Summarization ပြုလုပ်သည့်အခါ မလိုအပ်သော အခြား IP range များကို မလွှမ်းခြုံမိစေရန် Boundary Block Size ကို သတိပြုရမည်။

### လေ့ကျင့်ပြီးခဲ့သော ပုစ္ဆာ နမူနာများ:
* **/24 Network ၄ ခုကို ပေါင်းခြင်း:** `10.1.4.0/24` မှ `10.1.7.0/24` $\rightarrow$ **Summary Route:** `10.1.4.0/22` (`255.255.252.0`)
* **VLSM Subnet များကို ပေါင်းခြင်း:** `172.16.0.0/26`, `172.16.0.64/27`, `172.16.0.96/28` $\rightarrow$ **Most Specific Summary Route:** `172.16.0.0/25`

---

## 📌 ၃။ Linux Networking အခြေခံ Command များ

Networking သဘောတရားများကို Linux System, Docker Container နှင့် Cloud Infrastructure (AWS VPC) တို့တွင် လက်တွေ့ အသုံးချရန် အခြေခံ Command များ:

```bash
# Server / Machine ၏ IP Address နှင့် Subnet Mask (/24, /26) စစ်ဆေးခြင်း
ip a

# Traffic များ ထွက်သွားမည့် Routing Table နှင့် Default Gateway ကို ကြည့်ခြင်း
ip route

# Network ချိတ်ဆက်မှု (Connectivity) ရမရ စစ်ဆေးခြင်း
ping -c 4 8.8.8.8

# Network ပေါ်တွင် ပွင့်နေသော Port များ (Web Port 80, 443 စသည်) ကို စစ်ဆေးခြင်း
ss -tulpn

# DNS Name Resolution (Domain မှ IP သို့ ပြောင်းလဲမှု) ကို စစ်ဆေးခြင်း
dig google.com