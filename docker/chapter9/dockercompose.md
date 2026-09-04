###### 📘 အခန်း (၉) - Deploying Apps with Docker Compose (Multi-Container App များကို ချထားခြင်း)
၁။ Concept (အဓိက သဘောတရား) - "Docker Compose ဆိုတာ ဘာလဲ၊ ဘာကြောင့်သုံးလဲ"
ရှုပ်ထွေးတဲ့ Application တစ်ခုကို စဉ်းစားကြည့်ပါ။ သူ့မှာ Web Frontend, Database, Cache, Message Queue ဆိုပြီး အပိုင်းပေါင်းများစွာ (Microservices) ပါတယ်။ ဒီအပိုင်းတွေကို တစ်ခုချင်းစီ docker container run နဲ့ ချထားရင် Command တွေ အရမ်းရှည်ပြီး စီမံရခက်တယ်။

ဒါကို ဟင်းချက်နည်းစာအုပ် (Cookbook) ဥပမာ နဲ့ ကြည့်ပါ။

Docker Compose = ဟင်းပွဲတစ်ခုလုံးအတွက် မီနူးစာရွက် (Menu Card) ပါ။ ဒီမီနူးမှာ ဟင်းပွဲတစ်ခုချင်းစီအတွက် လိုအပ်တဲ့ ပါဝင်ပစ္စည်း၊ ချက်နည်း၊ အချိန်တွေ အကုန်ပါတယ်။

Compose File (docker-compose.yml) = ဒီမီနူးကို ရေးထားတဲ့ စာရွက် ပါ။ YAML ပုံစံနဲ့ ရေးထားတယ်။

docker compose up = မီနူးအတိုင်း ဟင်းပွဲအားလုံးကို တစ်ပြိုင်နက် ချက်ပြုတ်တဲ့ လုပ်ဆောင်ချက် ပါ။

အရေးကြီးတဲ့ အပြောင်းအလဲ (Update):
စာအုပ်ဟောင်းမှာ docker-compose (မျဉ်းစပ်ပါ) လို့ ခေါ်တယ်။ အခုအခါမှာ ဒါကို docker compose (မျဉ်းစပ်မပါ) လို့ ပြောင်းသုံးရပါမယ်။ (မျဉ်းစပ်ပါတဲ့ဟာက Python app ဖြစ်ပြီး၊ အသစ်က Go plugin ဖြစ်တယ်)။

၂။ Hands-on / Step-by-Step (လက်တွေ့ လိုက်လုပ်ရမည့် အဆင့်များ)
ဒီအဆင့်တွေက Simple Counter App (Flask + Redis) ကို Compose နဲ့ ချထားမှာပါ။

အဆင့် ၁: Application Code ကို Clone လုပ်ခြင်း
bash
# GitHub ကနေ Counter App Code ကို ကူးယူပါ။
git clone https://github.com/nigelpoulton/counter-app.git
cd counter-app

# ဖိုင်တွေကို ကြည့်ပါ (docker-compose.yml ပါတာကို တွေ့ရမယ်)
ls -la
အဆင့် ၂: docker-compose.yml ဖိုင်ကို ကြည့်ရှုခြင်း
bash
cat docker-compose.yml
ဖိုင်ထဲမှာ ဘာတွေပါလဲ -

version: "3.5" → Compose File Format ဗားရှင်း။ (အနည်းဆုံး 3.0 ဖြစ်ရမယ်)

services: → App ရဲ့ အစိတ်အပိုင်းတွေ။ ဒီမှာ web-fe (Flask) နဲ့ redis ဆိုပြီး နှစ်ခုပါတယ်။

web-fe: → build: . (လက်ရှိ Folder ထဲက Dockerfile နဲ့ Image ဆောက်မယ်)။ ports: "5000:5000" (Host Port 5000 ကို Container Port 5000 နဲ့ ချိတ်မယ်)။

redis: → image: "redis:alpine" (Docker Hub ကနေ Redis Image ကို ဆွဲမယ်)။

networks: → counter-net ဆိုတဲ့ Network အသစ် ဖန်တီးမယ်။ (Service နှစ်ခုလုံး ဒီ Network ပေါ်မှာ ဆက်သွယ်မယ်)

volumes: → counter-vol ဆိုတဲ့ Volume အသစ် ဖန်တီးမယ်။ (Data ကို သိမ်းဖို့)

အဆင့် ၃: Application ကို ချထားခြင်း (Deploy)
bash
# သတိပြုရန် - docker-compose (အဟောင်း) အစား docker compose (အသစ်) ကို သုံးပါ။
# -d က နောက်ခံ (Detach) မှာ ပြေးစေတယ်။
docker compose up -d

# ဒီ Command က network, volume, နဲ့ service တွေကို တစ်ပြိုင်နက် ဖန်တီးပေးတယ်။
အဆင့် ၄: App ကို စစ်ဆေးခြင်း
bash
# Container တွေ ပြေးနေလား ကြည့်ပါ။
docker container ls

# Network နဲ့ Volume တွေ ဖန်တီးထားလား ကြည့်ပါ။
docker network ls
docker volume ls

# Web Browser ကို ဖွင့်ပြီး http://localhost:5000 ကိုသွားပါ။
# Counter ကို နှိပ်ကြည့်ပါ။ (ဒေတာ Redis ထဲ သိမ်းနေတယ်)
⏸️ ၃။ Break (ခဏရပ်နားပြီး စဉ်းစားပါ)
ဒီအဆင့်မှာ ခင်ဗျား Command တွေ ရိုက်ပြီးပါပြီ။ App က ပုံမှန် အလုပ်လုပ်နေပါသလား။

ဆက်မလုပ်ခင် အောက်ပါအတိုင်း စဉ်းစားကြည့်ပါ။
၁။ docker compose up က ဘယ် Network ကို ဖန်တီးပေးသလဲ။
၂။ web-fe Service က ဘယ် Image ကို သုံးသလဲ။ (Build လုပ်တာလား၊ Pull လုပ်တာလား)
၃။ Port 5000 ကို ဘယ် Service က သုံးသလဲ။

