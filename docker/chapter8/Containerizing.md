

## 📘 အခန်း (၈) - Containerizing an App (Application ကို Container ဖြစ်အောင် ပြောင်းလဲခြင်း)

### ၁။ Concept (အဓိက သဘောတရား) - "Containerizing ဆိုတာ ဘာလဲ၊ ဘယ်လိုလုပ်လဲ"

Containerizing ဆိုတာ ခင်ဗျားရဲ့ Application ကို **Docker Image အဖြစ် ပြောင်းလဲခြင်း** ပါ။ ဒါကို နားလည်ဖို့ **ဟင်းချက်နည်း (Recipe) ဥပမာ** ကို ကြည့်ပါ။

- **Application Code** = ဟင်းချက်ဖို့ လိုတဲ့ **ပါဝင်ပစ္စည်းတွေ (Ingredients)** ။ (ဥပမာ - ကြက်သား၊ ငရုတ်ကောင်း၊ ဆား)
- **Dockerfile** = ဟင်းချက်နည်းကို ရေးထားတဲ့ **စာရွက် (Recipe Card)** ။ ဘယ်လိုချက်ရမယ်၊ ဘယ်အဆင့်တွေ လုပ်ရမယ်ဆိုတာ ပါတယ်။
- **Build Process** = စာရွက်အတိုင်း ဟင်းချက်တဲ့ **ချက်ပြုတ်ခြင်း (Cooking)** ။
- **Docker Image** = ချက်ပြီးသား **ဟင်းအချောထုတ် (Finished Dish)** ။ ဒါကို Container အဖြစ် မောင်းလို့ရပြီ။

**Multi-Stage Builds (အဆင့်စုံ တည်ဆောက်ခြင်း) - အရေးကြီးဆုံး**
ဒါက ခေတ်မီဆုံး Build နည်းလမ်းပါ။ ဟင်းချက်တဲ့အခါ **အဆင့် (၂) ဆင့်** လုပ်သလိုပါပဲ။
- **အဆင့် (၁)** - Build Stage: ဟင်းချက်ဖို့ လိုအပ်တဲ့ ကိရိယာတွေ (ဥပမာ - ဓား၊ ဒယ်အိုး) နဲ့ ဟင်းကို ချက်တယ်။ ဒါပေမယ့် ဒီအဆင့်က ကိရိယာတွေ အများကြီးပါတဲ့ Image ကြီးကို ထုတ်တယ်။
- **အဆင့် (၂)** - Production Stage: အဆင့် (၁) ကနေ **အဆင်သင့်စားလို့ရတဲ့ ဟင်းသာ (Final Dish)** ကို ကူးယူပြီး ကိရိယာတွေ မပါတဲ့ သေးငယ်တဲ့ Image အသစ်ကို ထုတ်တယ်။
- **ရလဒ်:** Production Image က **အလွန်သေးငယ် (Small)** ပြီး **ပိုလုံခြုံ (Secure)** တယ်။ (စာအုပ်ထဲမှာ "big is bad" လို့ ပြောထားတာက ဒါပါ)။

---

### ၂။ Hands-on / Step-by-Step (လက်တွေ့ လိုက်လုပ်ရမည့် အဆင့်များ)

ဒီအဆင့်တွေက ရှိပြီးသား Web App Code ကို ကူးယူပြီး Dockerfile နဲ့ Image တည်ဆောက်ကာ Container အနေနဲ့ မောင်းမှာပါ။

#### အဆင့် ၁: Application Code ကို Clone လုပ်ခြင်း
```bash
# Command: git clone https://github.com/nigelpoulton/psweb.git
# GitHub ပေါ်က Node.js Web App Code ကို ခင်ဗျားရဲ့ စက်ထဲ ကူးယူတယ်။
git clone https://github.com/nigelpoulton/psweb.git

# Code ရှိတဲ့ Folder ထဲကို ဝင်ပါ။
cd psweb

# ဖိုင်တွေကို ကြည့်ပါ (Dockerfile ပါတာကို တွေ့ရမယ်)
ls -la
```

#### အဆင့် ၂: Dockerfile ကို စစ်ဆေးခြင်း
```bash
# Command: cat Dockerfile
# Dockerfile ထဲမှာ App ကို ဘယ်လို Image အဖြစ် ပြောင်းရမယ်ဆိုတဲ့ ညွှန်ကြားချက်တွေ ပါတယ်။
cat Dockerfile
```
**Dockerfile အကြောင်း ရှင်းလင်းချက်:**
- `FROM alpine` → Base Image အဖြစ် Alpine Linux ကို သုံးတယ်။ (သေးငယ်တယ်)
- `RUN apk add --update nodejs` → Node.js ကို တပ်ဆင်တယ်။ (ဒါက Layer အသစ် ဖန်တီးတယ်)
- `COPY . /src` → လက်ရှိ Folder ထဲက Code အကုန်ကို Image ထဲက `/src` ဆိုတဲ့ Folder ထဲ ကူးတယ်။ (Layer အသစ်)
- `WORKDIR /src` → အလုပ်လုပ်မယ့် Folder ကို `/src` လို့ သတ်မှတ်တယ်။ (Metadata)
- `RUN npm install` → Node.js Dependencies တွေ တပ်ဆင်တယ်။ (Layer အသစ်)
- `EXPOSE 8080` → Port 8080 ကို ဖွင့်တယ်။ (Documentation)
- `ENTRYPOINT ["node", "./app.js"]` → Container စတင်ရင် `node ./app.js` ကို အလိုအလျောက် မောင်းတယ်။ (Metadata)

#### အဆင့် ၃: Docker Image တည်ဆောက်ခြင်း (Build)
```bash
# Command: docker image build -t my-web-app:latest .
# -t my-web-app:latest က Image ကို နာမည်ပေးတယ်။
# . (အစက်) က လက်ရှိ Folder (psweb) ကို Build Context အဖြစ် သတ်မှတ်တယ်။
docker image build -t my-web-app:latest .

# Build ပြီးသွားရင် Image စာရင်းကြည့်ပါ။
docker image ls
```

#### အဆင့် ၄: Container ကို နောက်ခံမှာ စတင်ပြီး Port ဖွင့်ခြင်း
```bash
# Command: docker container run -d --name web1 -p 8080:8080 my-web-app:latest
# -d → Detach mode (နောက်ခံ)
# --name web1 → Container ကို နာမည်ပေးတယ်
# -p 8080:8080 → Host Port 8080 ကို Container Port 8080 နဲ့ ချိတ်တယ်။
docker container run -d --name web1 -p 8080:8080 my-web-app:latest

# Container ပြေးနေလား စစ်ပါ။
docker container ls
```

#### အဆင့် ၅: Web App ကို စမ်းသပ်ခြင်း
Web Browser ကို ဖွင့်ပြီး `http://localhost:8080` (Docker Desktop) သို့မဟုတ် ခင်ဗျားရဲ့ VM IP (ဥပမာ `http://192.168.1.100:8080`) ကို သွားပါ။ "Hello World" ဆိုတဲ့ စာမျက်နှာ ပေါ်လာရင် အောင်မြင်ပါပြီ။

#### အဆင့် ၆: Multi-Stage Build (အဆင့်မြှင့် Build) ကို စမ်းသပ်ခြင်း (အရေးကြီး)
ဒါက Production-ready Image ကို သေးငယ်အောင် ဘယ်လိုလုပ်မလဲဆိုတာ ပြဖို့ပါ။
```bash
# စာအုပ်ထဲက AtSea Sample App ကို Clone လုပ်ပါ။
git clone https://github.com/nigelpoulton/atsea-sample-shop-app.git
cd atsea-sample-shop-app/app

# Dockerfile ကို ကြည့်ပါ (FROM သုံးခုပါတယ်)
cat Dockerfile

# Multi-stage Build ကို လုပ်ပါ။ (ဒါက အချိန်အတော်ကြာနိုင်တယ်)
docker image build -t my-atsea-app:latest .

# Image စာရင်းကြည့်ရင် သေးငယ်တဲ့ Production Image ကို တွေ့ရမယ်။
docker image ls
```

---

### ၃။ Key Takeaways & Best Practices (သတိထားရန်နှင့် မရှိမဖြစ် မှတ်သားရမည့် အချက်များ)

ဒီအခန်းပြီးသွားရင် အောက်ပါ အချက် (၃) ချက်ကို သေချာမှတ်ထားပါ။

၁။ **Dockerfile ရဲ့ Instruction တွေက Layer တွေ ဖန်တီးတယ်**
   - `FROM`, `RUN`, `COPY`, `ADD` စတဲ့ Instruction တွေက Layer အသစ် ဖန်တီးတယ်။ Layer များလေလေ Image ကြီးလေလေ၊ Build နှေးလေလေ။ ဒါကြောင့် `RUN` Instruction တွေကို ပေါင်းစပ်ပါ (ဥပမာ - `RUN apt update && apt install -y package`)။

၂။ **Multi-Stage Build ကို Production မှာ သုံးပါ**
   - Build Tools (ဥပမာ - Maven, Node, GCC) တွေက Image ကို ကြီးမားစေတယ်။ Multi-Stage Build က Build Tools တွေကို ဖယ်ရှားပြီး Final Image ကို သေးငယ်စေတယ်။

၃။ **Build Cache ကို အသုံးချပါ**
   - Docker က Layer တွေကို Cache လုပ်တယ်။ ဒါကြောင့် မကြာခဏ ပြောင်းလဲတဲ့ Instruction တွေ (ဥပမာ - `COPY . /src`) ကို Dockerfile ရဲ့ အောက်ဆုံးမှာ ထားပါ။ ဒါမှ Cache ကို ပိုပြီး အသုံးချနိုင်မယ်။

---


