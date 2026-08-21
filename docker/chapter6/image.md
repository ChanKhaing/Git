
📘 အခန်း (၆) - Images (Docker ပုံရိပ်များ)

၁။ Concept (အဓိက သဘောတရား) - "Docker Image ဆိုတာ ဘာလဲ၊ ဘယ်လိုဖွဲ့စည်းထားလဲ"

Docker Image က ကွန်တိန်နာတွေ မောင်းဖို့အတွက် မရှိမဖြစ် Template (ပုံစံခွက်) ပါ။ ဒါကို နားလည်ဖို့ ကိတ်မုန့် (Cake) ဥပမာ ကို ကြည့်ပါ။

· Image = ကိတ်မုန့်တစ်ခုလုံးရဲ့ ဓာတ်ပုံ (Recipe Book) ပါ။ ဒီဓာတ်ပုံမှာ ကိတ်မုန့်ရဲ့ အလွှာတွေ (Layers) အကုန်ပါတယ် - အောက်ခြေဂျုံလွှာ၊ ထောပတ်လွှာ၊ သစ်သီးလွှာ စသဖြင့်။ ဒါပေမယ့် ဒီဓာတ်ပုံက စားလို့မရသေးဘူး (Stopped Container)။
· Layers (အလွှာများ) = ကိတ်မုန့်ရဲ့ အလွှာတစ်ခုချင်းစီပါ။ Image တစ်ခုက အလွှာများစွာ ပေါင်းစပ်ထားတာဖြစ်ပြီး၊ ဒီအလွှာတွေကို Storage Driver (ဥပမာ - overlay2) က စုပေါင်းပြီး တစ်ခုတည်းအဖြစ် ပြသပေးတယ်။
· Image Registry (သိုလှောင်ရုံ) = ကိတ်မုန့် ဓာတ်ပုံတွေ သိမ်းထားတဲ့ စာကြည့်တိုက် (Library) ပါ။ အသုံးအများဆုံးက Docker Hub ဖြစ်တယ်။

Image Layers ရဲ့ အားသာချက် - Sharing (မျှသုံးခြင်း)
ကိတ်မုန့် ဓာတ်ပုံနှစ်ပုံမှာ တူညီတဲ့ အောက်ခြေဂျုံလွှာ (Base Layer) ပါရင်၊ ဒီအလွှာကို နှစ်ခါသိမ်းစရာမလိုဘူး။ မျှသုံးလို့ရတယ်။ ဒါက Disk Space သက်သာပြီး Download မြန်စေတယ်။

---

၂။ Hands-on / Step-by-Step (လက်တွေ့ လိုက်လုပ်ရမည့် အဆင့်များ)

ဒီအဆင့်တွေက Image ဆွဲခြင်း၊ စာရင်းကြည့်ခြင်း၊ Tag လုပ်ခြင်းနဲ့ ဖျက်ခြင်းတွေကို လက်တွေ့ လုပ်ဆောင်မှာပါ။

အဆင့် ၁: Image ဆွဲခြင်း (Pulling)

# Command: docker image pull alpine:latest
# Alpine Linux Image (အလွန်သေးငယ်တဲ့ Linux - 5MB ဝန်းကျင်) ကို Docker Hub ကနေ ဆွဲယူတယ်။
# "latest" က Tag (ဗားရှင်းအမှတ်) ဖြစ်တယ်။
docker image pull alpine:latest

# Command: docker image pull ubuntu:latest
# Ubuntu Image (~70MB) ကို ဆွဲယူတယ်။
docker image pull ubuntu:latest
အဆင့် ၂: Image စာရင်းကြည့်ခြင်းနဲ့ Layers ကိုကြည့်ခြင်း

# Command: docker image ls
# ခင်ဗျားရဲ့ စက်ထဲမှာ ရှိတဲ့ Image အားလုံးကို စာရင်းပြတယ်။
docker image ls

# Command: docker image history alpine:latest
# ဒီ Image ကို ဘယ်လို Layers တွေနဲ့ တည်ဆောက်ထားလဲဆိုတာ ပြတယ်။
# (အောက်ခြေကနေ အပေါ်ကို ဖတ်ရမယ်)
docker image history alpine:latest
မှတ်ချက် (Comment): docker image ls ရဲ့ အထွက်မှာ REPOSITORY, TAG, IMAGE ID, CREATED, SIZE ဆိုတဲ့ ကော်လံတွေပါတယ်။ alpine က 5MB ဝန်းကျင်ဖြစ်ပြီး ubuntu က 70MB ဝန်းကျင်ဖြစ်တာကို တွေ့ရမယ်။ 
အဆင့် ၃: Image ရဲ့ အသေးစိတ်အချက်အလက် (Inspect)

# Command: docker image inspect alpine:latest
# ဒီ Image ရဲ့ ဖွဲ့စည်းပုံ၊ Layers တွေရဲ့ SHA256 Hashes၊ ENV variables စတဲ့
# အသေးစိတ် JSON အချက်အလက်တွေကို ပြပေးတယ်။
docker image inspect alpine:latest
docker image inspect ရဲ့ အထွက်ထဲက "RootFS" ဆိုတဲ့ အပိုင်းကို ရှာပါ။ အဲဒီမှာ Layers တွေရဲ့ Hash တွေ ပါတယ်။ Layers ဘယ်နှစ်လွှာပါလဲ ရေတွက်ကြည့်ပါ။ 
### (Alpine က ၁ လွှာပဲရှိတတ်တယ်၊ Ubuntu က ၄-၅ လွှာရှိတယ်)။

အဆင့် ၄: Image Tagging (နာမည်ပြောင်းခြင်း)

# Command: docker image tag alpine:latest my-alpine:v1
# ဒီ Command က ရှိပြီးသား Image ကို နာမည်အသစ် (my-alpine:v1) ထပ်ပေးတယ်။
# (ဒါက Image အသစ် မဖန်တီးဘူး၊ Tag အသစ်ပဲ ထပ်ထည့်တာ)
docker image tag alpine:latest my-alpine:v1

# စာရင်းပြန်ကြည့်ရင် တူညီတဲ့ IMAGE ID နဲ့ နာမည်နှစ်ခု ပါနေမယ်။
docker image ls
အဆင့် ၅: Image ဖျက်ခြင်းနဲ့ သန့်ရှင်းရေး (Prune)

# Command: docker image rm my-alpine:v1
# Tag အသစ်ကို ဖယ်ရှားတယ်။ (ဒါပေမယ့် alpine:latest က ရှိနေသေးလို့ Image က မပျက်ဘူး)
docker image rm my-alpine:v1

# Command: docker image prune
# ဘယ် Container မှ မသုံးတဲ့ Image (Dangling Images) အားလုံးကို ဖျက်ပစ်တယ်။
# -f ထည့်ရင် အတည်ပြုမမေးဘဲ ဖျက်တယ်။
docker image prune -f

# Command: docker image rm $(docker image ls -q) -f
# စက်ထဲက Image အားလုံးကို အတင်းဖျက်တယ်။ (သတိထားသုံးပါ)
# docker image ls -q က ID တွေကို စာရင်းပြတယ်။
# docker image rm -f က အတင်းဖျက်တယ်။
docker image rm $(docker image ls -q) -f
---

၃။ Key Takeaways & Best Practices (သတိထားရန်နှင့် မရှိမဖြစ် မှတ်သားရမည့် အချက်များ)

ဒီအခန်းပြီးသွားရင် အောက်ပါ အချက် (၃) ချက်ကို သေချာမှတ်ထားပါ။

၁။ Image က Immutable (ပြင်လို့မရဘူး)
· Image တစ်ခုကို ဖန်တီးပြီးရင် အတွင်းထဲက ဖိုင်တွေကို ပြင်လို့မရဘူး။ ပြင်ချင်ရင် Image အသစ် (New Layer) ကို ထပ်ထည့်ပြီး Rebuild လုပ်ရမယ်။ (ဒါက Version Control အတွက် ကောင်းတယ်)။

၂။ "latest" Tag က အန္တရာယ်များတယ်

· latest Tag က အသစ်ဆုံး (Newest) ဖြစ်မယ်လို့ အာမခံချက်မရှိဘူး။ ဥပမာ - ခင်ဗျား ubuntu:latest ဆွဲလိုက်တာက ဟောင်းနေနိုင်တယ်။ Production မှာ တိကျတဲ့ Tag (ဥပမာ ubuntu:20.04) ကို သုံးပါ။ ဒါမှမဟုတ် Digest (SHA256 hash) ကို သုံးပါ။

၃။ Multi-Architecture Images (ဗိသုကာမျိုးစုံ)

· တူညီတဲ့ Image Tag (ဥပမာ golang:latest) က Linux (amd64) အတွက် ဆွဲရင် တစ်မျိုး၊ Windows (amd64) အတွက် ဆွဲရင် တစ်မျိုး အလိုအလျောက် သင့်တော်တဲ့ Image ကို ဆွဲပေးတယ်။ (ဒါက Manifest List ကြောင့်ပါ)။ 
---

⚠️ စာအုပ်ထဲမှာ docker rmi (အဟောင်း) ကို သုံးထားပေမယ့် အခုအခါမှာ docker image rm (အသစ်) ကို သုံးပါ။ ထို့အတူ docker images (အဟောင်း) အစား docker image ls (အသစ်) ကို သုံးပါ။ docker pull ကို docker image pull လို့ သုံးနိုင်ပေမယ့် pull က အုပ်စုမပါဘဲ သုံးတာကို ဆက်လက်ခွင့်ပြုထားတယ်။ ဒါပေမယ့် စနစ်ကျဖို့ image group ကို သုံးတာကောင်းတယ်။

---