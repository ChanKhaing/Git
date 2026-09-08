

💻 အပိုင်း (၂) - Dev Perspective (ဆော့ဖ်ဝဲရေးသူ ရှုထောင့်)

ဒီအပိုင်းမှာ GitHub ကနေ Web App Code ကို ကူးယူပြီး Dockerfile နဲ့ Image တည်ဆောက်ကာ Container အနေနဲ့ မောင်းမယ်။

အဆင့် ၁: Application Code ကို Clone လုပ်ခြင်း
[19/08/2026 19:27] chan khine (linux ): # Command: git clone <repo-url>
# GitHub ပေါ်က Node.js Web App Code ကို ခင်ဗျားရဲ့ စက်ထဲ ကူးယူတယ်။
git clone https://github.com/nigelpoulton/psweb.git

# Code ရှိတဲ့ Folder ထဲကို ဝင်ပါ။
cd psweb
အဆင့် ၂: Dockerfile ကို ကြည့်ရှုခြင်း

# Command: cat Dockerfile
# Dockerfile ထဲမှာ App ကို ဘယ်လို Image အဖြစ် ပြောင်းရမယ်ဆိုတဲ့ ညွှန်ကြားချက်တွေ ပါတယ်။
cat Dockerfile
အဆင့် ၃: Docker Image အသစ် တည်ဆောက်ခြင်း (Build)

# Command: docker image build -t test:latest .
# -t က Tag (နာမည်) သတ်မှတ်တယ်။ ဒီမှာ test:latest လို့ ပေးထားတယ်။
# နောက်ဆုံးက . (အစက်) က လက်ရှိ Folder (psweb) ကို Build Context အဖြစ် သတ်မှတ်တယ်။
docker image build -t test:latest .
အဆင့် ၄: Container ကို နောက်ခံမှာ စတင်ပြီး Port ဖွင့်ခြင်း

# Command: docker container run -d --name web1 -p 8080:8080 test:latest
# -d က Detach mode (နောက်ခံ) မှာ ပြေးစေတယ်။
# --name web1 က Container ကို နာမည်ပေးတယ်။
# -p 8080:8080 က Host ရဲ့ Port 8080 ကို Container ရဲ့ Port 8080 နဲ့ ချိတ်ပေးတယ်။
docker container run -d --name web1 -p 8080:8080 test:latest
အဆင့် ၅: Web App ကို စမ်းသပ်ခြင်း

ခင်ဗျားရဲ့ Web Browser ကို ဖွင့်ပြီး http://localhost:8080 (Docker Desktop သုံးရင်) သို့မဟုတ် ခင်ဗျားရဲ့ VM IP Address (ဥပမာ http://192.168.1.100:8080) ကို သွား## 📚 References & Credits (ကိုးကားချက်များ)

ဒီ Repository မှာပါတဲ့ သင်ခန်းစာများနှင့် လေ့လာမှုပုံစံ (Learning Path) များကို အောက်ပါ စာအုပ်မှ အခြေခံ၍ ကိုးကား ပြုစုထားခြင်းဖြစ်ပါတယ် -

* **Book:** [Docker Deep Dive](https://nigelpoulton.com/books/docker-deep-dive/) by **Nigel Poulton**ပါ။ "Hello World" ဆိုတဲ့ စာမျက်နှာ ပေါ်လာရင် အောင်မြင်ပါပြီ။

---

၃။ Key Takeaways & Best Practices (သတိထားရန်နှင့် မရှိမဖြစ် မှတ်သားရမည့် အချက်များ)

ဒီအခန်းပြီးသွားရင် အောက်ပါ အချက် (၃) ချက်ကို သေချာမှတ်ထားပါ။

၁။ Image နဲ့ Container ကွာခြားချက်

· Image က ရပ်နေတဲ့ Container (Template) ဖြစ်ပြီး၊ Container က အသက်ဝင်နေတဲ့ Image (Running Process) ဖြစ်တယ်။ Image ကိုပြင်လို့မရဘူး (Immutable)၊ Container ထဲမှာတော့ အပြောင်းအလဲလုပ်လို့ရတယ် (Mutable)။

၂။ Port Mapping (-p) က အရေးကြီးဆုံး

· Container က သီးသန့် Network (Sandbox) ထဲမှာ ရှိတယ်။ အပြင်ကနေ ဝင်ရောက်ဖို့ -p host_port:container_port နဲ့ ဖွင့်ပေးရမယ်။ ဒီလိုမှမဟုတ်ရင် Browser နဲ့ ဝင်လို့မရဘူး။

၃။ Dockerfile က Documentation ဖြစ်တယ်

· Dockerfile က Code တစ်ပိုင်းဖြစ်ပြီး App ရဲ့ လိုအပ်ချက်တွေကို ရှင်းရှင်းလင်းလင်း ဖော်ပြတယ်။ ဒါက Dev နဲ့ Ops ကြား ပေါင်းကူးတံတား (Bridge) ဖြစ်တယ်။ ဒါကြောင့် Dockerfile ကို Source Control (Git) မှာ အမြဲသိမ်းပါ။

---

⚠️ သတိထားရမည့် အချက် (Warning)

စာအုပ်ထဲမှာ docker container run နဲ့ docker container exec ကို သုံးထားတယ်။ ဒါက မှန်ကန်ပြီး ခေတ်မီဆဲဖြစ်လို့ ပြောင်းစရာမလိုပါဘူး။ ဒါပေမယ့် စာအုပ်ထဲက docker ps (အဟောင်း) အစား docker container ls (အသစ်) ကို သုံးဖို့ သတိရပါ။ docker images (အဟောင်း) အစား docker image ls (အသစ်) ကို သုံးပါ။ (ကျွန်တော်တို့ အထက်မှာ ဒီအသစ်တွေကိုပဲ သုံးထားပြီးသားပါ)။

---
