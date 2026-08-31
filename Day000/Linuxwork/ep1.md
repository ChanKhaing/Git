အောက်ဆုံးအလွှာ (Basic Services): Kernel နဲ့ အနီးဆုံး။ သေးငယ်ပြီး ရိုးရှင်းတဲ့ Component တွေ။

အလယ်အလွှာ (Utility Services): Mail, Print, Database လိုမျိုး ပိုကြီးတဲ့ Component တွေ။

အပေါ်ဆုံးအလွှာ (Applications): User တွေ တိုက်ရိုက်သုံးတဲ့ Web Browser, User Interface စတာတွေ။
Linux စနစ်မှာ အဓိက အဆင့်သုံးဆင့် (Hardware, Kernel, User Space) ရှိတယ်။ Kernel က Process တွေ၊ Memory၊ Device တွေကို စီမံပြီး User Process တွေက အသုံးပြုသူတွေအတွက် အလုပ်လုပ်တယ်။ Kernel က Process တွေကို အချိန်ကိုက် (time slice) ခွဲပြီး Multitasking လုပ်ပေးတယ်။ Process အသစ်တွေကို fork() နဲ့ မွေးပြီး exec() နဲ့ Program အသစ်တွေ စတင်တယ်။ User တွေက သီးခြားနယ်နိမိတ်တွေနဲ့ ကာကွယ်ထားပြီး Root User ကတော့ အထူးအခွင့်အရေးတွေ ရှိတယ်။

Multitasking ကို စားသောက်ဆိုင်နဲ့ ဥပမာပေးရရင်: စားသောက်ဆိုင်မှာ ထမင်းချက်တဲ့မီးဖို (CPU) တစ်ခုပဲရှိတယ်။ ဒါပေမယ့် ဟင်းအများကြီး (Process တွေ) ကို တစ်ပြိုင်နက်တည်း ချက်နေသလိုပေါ်အောင် မီးဖိုကို ဟင်းတစ်မျိုးချက်ပြီး ခဏရပ်၊ နောက်ဟင်းတစ်မျိုးချက်၊ ဒီလိုလှည့်ပြီး ချက်တယ်။ ဒီလိုလုပ်တာကို Context Switch လို့ခေါ်တယ်။ မီးဖိုကို ဘယ်ဟင်းဘယ်လောက်ကြာကြာချက်မလဲ ဆုံးဖြတ်တာက Kernel ရဲ့ Scheduling ပါ။

fork() နဲ့ exec() ကို စာရွက်မိတ္တူကူးနဲ့ ဥပမာပေးရရင်: ခင်ဗျားမှာ စာရွက်တစ်ရွက် (Process) ရှိတယ်။ ဒီစာရွက်ကို မိတ္တူကူးချင်တယ်ဆိုရင် fork() က အတူတူစာရွက်တစ်ရွက် ထပ်ထုတ်ပေးတယ်။ ပြီးရင် အဲဒီစာရွက်အသစ်ပေါ်မှာ စာသားအသစ် (new program) ရေးချင်တယ်ဆိုရင် exec() က ဟောင်းနွမ်းနေတဲ့စာသားကို ဖျက်ပြီး အသစ်ထည့်ပေးတယ်။

# 1. လက်ရှိ shell process ရဲ့ ID (PID) ကိုကြည့်ပါ။
echo $$  
# $$ ဆိုတာ လက်ရှိ shell process ရဲ့ PID ကို ပြတဲ့ special variable ဖြစ်ပါတယ်။

# 2. စနစ်ထဲမှာ အလုပ်လုပ်နေတဲ့ Process အားလုံးကို စာရင်းကြည့်ပါ။
ps -ef  
# ps က process status ပြဖို့ပါ။ -e က အားလုံးကိုပြဖို့၊ -f က full format နဲ့ပြဖို့ပါ။
# ရလာတဲ့စာရင်းထဲမှာ PID (Process ID) နဲ့ PPID (Parent Process ID) ကို သတိထားကြည့်ပါ။

# 3. တိကျတဲ့ Process တစ်ခုရဲ့ အချက်အလက်ကို ကြည့်ပါ (ဥပမာ PID 1 ဖြစ်တဲ့ init process)။
ps -p 1 -o pid,ppid,cmd  
# -p 1 က PID 1 ကိုပြဖို့၊ -o က output format သတ်မှတ်ဖို့။ pid, ppid, cmd ကိုပြပါ။

# 4. Process တွေရဲ့ သစ်ပင်ပုံစံ (tree) ကို ကြည့်ပါ (ဘယ် Process က ဘယ်ဟာကို fork လုပ်ထားလဲဆိုတာ သိဖို့)။
pstree -p
# pstree က process tree ကိုပြတယ်။ -p က PID ပါထည့်ပြဖို့ပါ။

# 5. လက်ရှိ shell ကနေ ကလေး process တစ်ခုကို ဖန်တီးကြည့်ပါ (နောက်ခံမှာ အလုပ်လုပ်ဖို့ & သုံးပါ)။
sleep 30 &
# sleep 30 က 30 စက္ကန့်စောင့်တဲ့ command ပါ။ & က နောက်ခံ (background) မှာ run ဖို့ပါ။

# 6. အခုအလုပ်လုပ်နေတဲ့ နောက်ခံ process တွေကို ကြည့်ပါ။
jobs
# jobs က လက်ရှိ shell အောက်မှာ နောက်ခံ run နေတဲ့ process တွေကိုပြတယ်။

# 7. နောက်ခံ process ကို foreground ကို ပြန်ခေါ်ပြီး ရပ်လိုက်ပါ (kill လုပ်ပါ)။
fg %1   # jobs စာရင်းထဲက နံပါတ် 1 ကို foreground ခေါ်မယ်။
# ပြီးရင် Ctrl+C နှိပ်ပြီး process ကို ရပ်လိုက်ပါ။

# 8. Process တစ်ခုကို kill (terminate) လုပ်ကြည့်ပါ (ဥပမာ sleep process ကို)။
sleep 100 &
ps                       # sleep process ရဲ့ PID ကိုရှာပါ။
kill PID_နံပါတ်         # ဥပမာ kill 1234 (သတိထား! PID ကိုယ်စားထည့်ပါ)
# kill command က process ကို signal ပို့ပြီး ရပ်စေပါတယ်။






