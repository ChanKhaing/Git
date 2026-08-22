

### Pre-flight Resource Checks (အခြေခံ Resource စစ်ဆေးခြင်း):

Free RAM & Disk Space Check: Server ရဲ့ Memory (RAM) နဲ့ Disk Space လုံလောက်မှု ရှိမရှိ အရင် စစ်ဆေးတာ ဖြစ်ပါတယ်။

### Service Health Check (Service အခြေအနေ စစ်ဆေးခြင်း):

Nginx Status Inspection: Nginx Web Server run နေလား/ရပ်နေလား စစ်ပါတယ်။

Auto-Recovery Action: ရပ်နေခဲ့ရင် systemctl start nginx နဲ့ Automatically ပြန်စပေးပါတယ်။

### Firewall Safety & Accessibility Check (Security စစ်ဆေးခြင်း):

UFW Firewall Status: Firewall Active ဖြစ်မဖြစ် စစ်ပါတယ်။

SSH Rule Validation: Sysadmin တွေ Server ထဲ ဝင်ရအောင် SSH Port (22) ပိတ်မသွားအောင် Check လုပ်ပြီး Rule ထည့်ပေးတာ ဖြစ်ပါတယ်


## The concept cover 
#### Prevents Server Crashes (Resource Awareness):
RAM နဲ့ Disk Space မလောက်ဘဲ Nginx ကို အတင်း run ရင် Server Out of Memory (OOM) ဖြစ်ပြီး တစ်စက်လုံး Hang သွားနိုင်ပါတယ်။

### High Availability (Auto-Healing):
Nginx Down နေရင် Auto-start ပြန်လုပ်ပေးတဲ့အတွက် Website Down time ကို လျှော့ချပေးပါတယ်။

#### Security & Lockout Protection:
UFW Firewall မှာ SSH Port (Port 22) ကို အမြဲ စစ်ဆေးပေးထားတာကြောင့် Server ကနေ Admin Lockout မဖြစ်အောင် ကာကွယ်ပေးပါတယ်။