🛠️ အပိုင်း (၁) - Ops Perspective (စနစ်ထိန်းသိမ်းသူ ရှုထောင့်)

ဒီအပိုင်းမှာ Ubuntu Image ကို ဆွဲယူပြီး Container တစ်လုံး စတင်ကာ အတွင်းထိုးဝင်ပြီး Command ပေးမယ်။ ပြီးရင် ရပ်ပြီး ဖျက်မယ်။

အဆင့် ၁: Client နဲ့ Server အလုပ်လုပ်နေလား စစ်ဆေးခြင်း

# Command: docker version
# ဒါက Client နဲ့ Server (Daemon) ဆက်သွယ်မှု အဆင်ပြေရဲ့လား စစ်တယ်။
docker version
အဆင့် ၂: Ubuntu Image ကို ဆွဲယူခြင်း (Pull)

# Command: docker image pull ubuntu:latest
# Docker Hub ကနေ Ubuntu Operating System ပါတဲ့ Image ကို ဒေါင်းလုဒ်ဆွဲတယ်။
# (Windows သုံးရင် ubuntu နေရာမှာ microsoft/powershell:nanoserver ကိုသုံးပါ)
docker image pull ubuntu:latest
အဆင့် ၃: Container အသစ် စတင်ခြင်း (Run)

# Command: docker container run -it ubuntu:latest /bin/bash
# -it က Interactive Mode ဖြစ်ပြီး ခင်ဗျားရဲ့ Terminal ကို Container ထဲ ချိတ်ပေးတယ်။
# /bin/bash က Container ထဲမှာ Bash Shell ကို စတင်ခိုင်းတယ်။
docker container run -it ubuntu:latest /bin/bash

# ဒီ Command ရိုက်ပြီးရင် ခင်ဗျားရဲ့ Prompt က root@<container-id>:/# လို ပြောင်းသွားမယ်။
အဆင့် ၄: Container ထဲမှာ Command များ စမ်းသပ်ခြင်း

Container ထဲရောက်ရင် အောက်ပါတွေကို ရိုက်ကြည့်ပါ။

# Container ထဲက လုပ်ငန်းစဉ်တွေကို ကြည့်ခြင်း
ps -elf

# ဖိုင်တစ်ခု ဖန်တီးခြင်း (ဒီဒေတာက သိမ်းဆည်းထားမလားဆိုတာ နောက်မှပြန်စစ်မယ်)
echo "Hello Docker" > /tmp/test.txt
cat /tmp/test.txt
အဆင့် ၅: Container ထဲကနေ ထွက်ခြင်း (Exit without stopping)

# Ctrl + P ပြီး Ctrl + Q ကို ဆက်တိုက်နှိပ်ပါ။ (သို) Ctrl + P Q
# ဒါက Container ကို မသတ်ဘဲ နောက်ခံမှာ ဆက်ထားပြီး ခင်ဗျားရဲ့ Host Terminal ကို ပြန်ခေါ်တယ်။
# (ကိုယ်တိုင် ရိုက်လိုမရပါဘူး၊ Keyboard shortcut ဖြစ်တယ်)
အဆင့် ၆: Container ကို ပြန်ချိတ်ဆက်ခြင်း (Exec)

# Command: docker container exec -it <container-name> bash
# နောက်ခံမှာ ပြေးနေတဲ့ Container ထဲကို ပြန်ဝင်ဖို ဒီ Command ကိုသုံးတယ်။
# Container Name ကို သိဖို docker container ls နဲ့ ကြည့်ပါ။
docker container ls
# အထွက်မှာ NAME ကော်လံကို ကြည့်ပြီး အဲဒီနာမည်ကို သုံးပါ။ (ဥပမာ - inspiring_swanson)
docker container exec -it inspiring_swanson bash

# ပြန်ရောက်ရင် /tmp/test.txt ရှိမရှိ စစ်ကြည့်ပါ။ (ရှိနေမယ်)
cat /tmp/test.txt
အဆင့် ၇: Container ကို ရပ်ပြီး ဖျက်ခြင်း (Stop & Remove)

# Command: docker container stop <name>
# Container ကို နူးညံ့စွာ (Gracefully) ရပ်တန့်စေတယ်။
docker container stop inspiring_swanson

# Command: docker container rm <name>
# ရပ်သွားတဲ့ Container ကို စနစ်ကနေ လုံးဝ ဖျက်ပစ်တယ်။
docker container rm inspiring_swanson

# ဖျက်ပြီးသွားရင် စစ်ကြည့်ပါ။ (စာရင်းထဲ မပါတော့ဘူး)
docker container ls -a