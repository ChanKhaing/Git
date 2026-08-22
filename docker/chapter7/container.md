

၁။ Concept (အဓိက သဘောတရား) - "Container ဆိုတာ ဘာလဲ၊ VM နဲ့ ဘာကွာလဲ"

Container ဆိုတာ Image ရဲ့ အသက်ဝင်နေတဲ့ ပုံစံ (Running Instance) ပါ။ ဒါကို နားလည်ဖို့ တိုက်ခန်း (Apartment) ဥပမာ ကို ကြည့်ပါ။

· VM (Virtual Machine) = အိမ်တစ်လုံးစီမှာ ကိုယ်ပိုင် မီးဖိုချောင်၊ ရေချိုးခန်း၊ လျှပ်စစ်မီတာ (တစ်ခုလုံး OS) ပါတယ်။ အိမ်တိုင်းက သီးခြား စရိတ်စကတွေ ကုန်တယ်။ (OS Tax)
· Container = တိုက်ခန်းတစ်ခုလုံးမှာ ဗဟိုမီးဖိုချောင်နဲ့ ရေချိုးခန်း (Shared OS Kernel) ကို သုံးတယ်။ တိုက်ခန်းတိုင်းက ကိုယ်ပိုင်ပရိဘောဂ (Application) ပဲ ထည့်ထားတယ်။ ပေါ့ပါးတယ်၊ မြန်တယ်၊ စရိတ်သက်သာတယ်။

Container ရဲ့ ဘဝသံသရာ (Lifecycle):
Container တစ်လုံးကို စတင်တယ် (run) → အလုပ်လုပ်တယ် → ခဏရပ်တယ် (stop) → ပြန်စတယ် (start) → ထာဝရဖျက်တယ် (rm)။

PID 1 ရဲ့ အရေးပါမှု:
Container တစ်လုံးမှာ အဓိက Process (PID 1) တစ်ခုရှိတယ်။ ဒီ Process သေရင် Container လုံးဝသေတယ်။ ဒါကြောင့် Container က Application တစ်ခုကို မောင်းဖို့ပဲ ဒီဇိုင်းထုတ်ထားတယ်။

---

၂။ Hands-on / Step-by-Step (လက်တွေ့ လိုက်လုပ်ရမည့် အဆင့်များ)

ဒီအဆင့်တွေက Container ကို စတင်ခြင်း၊ အတွင်းဝင်ခြင်း၊ ရပ်ခြင်း၊ ဖျက်ခြင်းနဲ့ Restart Policy တွေကို လက်တွေ့ လုပ်ဆောင်မှာပါ။

အဆင့် ၁: Container အသစ် စတင်ခြင်း (Run)

# Command: docker container run -it ubuntu:latest /bin/bash
# -it = Interactive Mode (ခင်ဗျား Terminal ကို Container ထဲ ချိတ်မယ်)
# ubuntu:latest = သုံးမယ့် Image
# /bin/bash = Container ထဲမှာ စမယ့် Application (PID 1 ဖြစ်လာမယ်)
docker container run -it ubuntu:latest /bin/bash

# ဒီ Command ရိုက်ပြီးရင် Prompt က root@<container-id>:/# လို့ ပြောင်းသွားပြီး
# ခင်ဗျားဟာ Container ထဲကို ရောက်နေပါပြီ။
အဆင့် ၂: Container ထဲမှာ Command များ စမ်းသပ်ခြင်းနဲ့ Process စစ်ဆေးခြင်း

Container ထဲရောက်ရင် အောက်ပါတွေကို ရိုက်ကြည့်ပါ။

# Container ထဲက လုပ်ငန်းစဉ်တွေကို ကြည့်ခြင်း (PID 1 က /bin/bash ဖြစ်နေတာတွေ့ရမယ်)
ps -elf

# ဖိုင်တစ်ခု ဖန်တီးခြင်း (ဒီဒေတာ ဆက်ရှိမလားဆိုတာ နောက်မှ ပြန်စစ်မယ်)
echo "My data is safe" > /tmp/mydata.txt
cat /tmp/mydata.txt
အဆင့် ၃: Container ထဲကနေ ထွက်ခြင်း (Detach) - Container ဆက်ရှိနေစေရန်

# Keyboard Shortcut: Ctrl + P ပြီး Ctrl + Q (သို့) Ctrl + P Q ကို ဆက်တိုက်နှိပ်ပါ။
# ဒါက Container ကို မသတ်ဘဲ နောက်ခံမှာ ဆက်ပြေးနေစေပြီး ခင်ဗျားရဲ့ Host Terminal ကို ပြန်ခေါ်တယ်။
အဆင့် ၄: Container စာရင်းကြည့်ခြင်းနဲ့ ပြန်ချိတ်ဆက်ခြင်း (Exec)

# Command: docker container ls
# လက်ရှိ ပြေးနေတဲ့ Container အားလုံးကို စာရင်းပြတယ်။ (NAME ကော်လံကို မှတ်ထားပါ)
docker container ls

# Command: docker container exec -it <container-name> bash
# ပြေးနေတဲ့ Container ထဲကို ပြန်ဝင်ဖို့ ဒီ Command ကိုသုံးတယ်။
# (ဥပမာ - docker container exec -it inspiring_swanson bash)
docker container exec -it inspiring_swanson bash

# ပြန်ရောက်ရင် /tmp/mydata.txt ရှိမရှိ စစ်ကြည့်ပါ။ (ရှိနေမယ်)
cat /tmp/mydata.txt

# ထွက်ချင်ရင် exit လို့ ရိုက်ပါ။ (ဒါက Container ကို မသတ်ဘူး၊ exec session ကိုပဲ ပိတ်တယ်)
exit
အဆင့် ၅: Container ကို ရပ်ခြင်း (Stop) နဲ့ သိမ်းဆည်းထားတဲ့ ဒေတာ စစ်ဆေးခြင်း

# Command: docker container stop <container-name>
# Container ကို နူးညံ့စွာ (Gracefully) ရပ်တန့်စေတယ်။ (SIGTERM ပို့တယ်)
docker container stop inspiring_swanson

# Command: docker container ls -a
# -a က ရပ်သွားတဲ့ Container ကိုပါ ပြပေးတယ်။ (STATUS က Exited ဖြစ်နေမယ်)
docker container ls -a

# Command: docker container start <container-name>
# ရပ်သွားတဲ့ Container ကို ပြန်စတယ်။ (ဒေတာတွေ ဆက်ရှိနေသေးတယ်)
docker container start inspiring_swanson

# ပြန်ဝင်ပြီး ဒေတာ စစ်ကြည့်ပါ။
docker container exec -it inspiring_swanson cat /tmp/mydata.txt
# "My data is safe" ဆိုတဲ့ စာသား ပြန်ထွက်လာမယ်။ (ဒေတာ ဆက်ရှိနေတယ်ဆိုတာ သက်သေပါ)
အဆင့် ၆: Container ကို ထာဝရ ဖျက်ခြင်း (Remove)

# Command: docker container rm <container-name>
# ရပ်သွားတဲ့ Container ကို စနစ်ကနေ လုံးဝ ဖယ်ရှားတယ်။
docker container rm inspiring_swanson

# သေချာအောင် စစ်ကြည့်ပါ (စာရင်းထဲ မပါတော့ဘူး)
docker container ls -a

အဆင့် ၇: Restart Policy (Self-Healing) ကို စမ်းသပ်ခြင်း

ဒါက Container သေသွားရင် အလိုအလျောက် ပြန်စဖို့ပါ။

# Command: docker container run -d --name auto-restart --restart always alpine sleep 1d
# --restart always က Container သေရင် အမြဲတမ်း ပြန်စမယ်။
docker container run -d --name auto-restart --restart always alpine sleep 1d

# Container ကို အတင်းသတ်ပါ။ (kill)
docker container kill auto-restart

# ခဏစောင့်ပြီး စာရင်းကြည့်ပါ။ (STATUS က Up (ပြန်စပြီး) ဖြစ်နေမယ်)
docker container ls
---



## note for notice
၁။ Container က Application တစ်ခုအတွက်ပဲ (PID 1 က အဓိက)

· Container တစ်လုံးမှာ Application တစ်ခုပဲ ထားသင့်တယ် (Microservices)။ PID 1 က အဲဒီ Application ဖြစ်တယ်။ ဒီ Application သေရင် Container သေတယ်။ ဒါကြောင့် Container ထဲမှာ Systemd လိုမျိုး မထည့်သင့်ဘူး။

၂။ Stop (SIGTERM) vs Kill (SIGKILL)

· docker container stop က Application ကို သေခါနီး အချိန် (၁၀ စက္ကန့်) ပေးတယ်။ (Graceful Shutdown)
· docker container rm -f (သို့) docker container kill က ချက်ချင်းသတ်တယ်။ (Data Loss ဖြစ်နိုင်တယ်)။ Production မှာ stop ကို အရင်သုံးပြီးမှ rm လုပ်ပါ။

၃။ Restart Policy က Self-Healing အတွက်

· --restart always က Container ဘယ်လိုပဲသေသေ ပြန်စတယ် (Daemon Restart ချိန်မှာလည်း စတယ်)။
· --restart unless-stopped က ခင်ဗျား ကိုယ်တိုင် stop လုပ်ထားရင် Daemon Restart ချိန်မှာ ပြန်မစဘူး။
· Production မှာ unless-stopped ကို ဦးစားပေးသုံးပါ။

---

⚠️ 
စာအုပ်ထဲမှာ docker ps (အဟောင်း) ကို သုံးထားပေမယ့် အခုအခါမှာ docker container ls (အသစ်) ကို သုံးပါ။ ထို့အတူ docker start, docker stop တို့ကို docker container start, docker container stop လို့ သုံးနိုင်ပါတယ်။ docker container run ကတော့ ခေတ်မီဆဲဖြစ်လို့ ဒီအတိုင်းသုံးပါ။ နောက်ပြီး Ctrl + P Q ကို မှတ်မိဖို့ အရေးကြီးပါတယ်။

---

