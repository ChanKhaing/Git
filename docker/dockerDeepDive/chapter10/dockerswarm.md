### Swarm ရဲ့ အားသာချက်တွေ -
၁။ High Availability (HA) - Manager တစ်လုံးပျက်ရင် နောက်တစ်လုံးက ဆက်လုပ်တယ်။
၂။ Load Balancing - Service Replica တွေကို Swarm Node အကုန်လုံးမှာ ဖြန့်ပေးတယ်။
၃။ Self-Healing - Container တစ်လုံးသေရင် အလိုအလျောက် ပြန်စတယ်။
၄။ Rolling Updates - Downtime မရှိဘဲ Application ကို Update လုပ်လို့ရတယ်။
၅။ Secure by Default - TLS ကို Default အနေနဲ့ သုံးထားတယ်။


Docker Swarm ဆိုတာ ဘာလဲ"
ဒီအခန်းမတိုင်ခင် ကျနော်တို့လုပ်ခဲ့တာက  Docker Host တစ်လုံးတည်းပေါ်မှာ Container တွေ မောင်းခဲ့တယ်။ ဒါပေမယ့် လက်တွေ့ Production Environment တွေမှာ Server အများကြီး (Cluster) ပေါ်မှာ Container တွေ မောင်းရတယ်။ ဒီလိုအခါမျိုးမှာ Docker Swarm က ကူညီတယ်။

အုပ်စုဖွဲ့ ခရီးသွား (Group Tour) ဥပမာ -

Swarm = ခရီးသွားအုပ်စုကြီးတစ်ခု (Cluster)။ Server အကုန်လုံး ပါတယ်။

Manager Node = ခရီးစဉ်မှူး (Tour Guide)။ ဘယ်သွားမယ်၊ ဘယ်လိုသွားမယ်ဆိုတာ စီစဉ်တယ်။

Worker Node = ခရီးသွားတွေ (Tourists)။ ခရီးစဉ်မှူး ပြောတဲ့အတိုင်း လိုက်လုပ်တယ်။

Service = ခရီးစဉ်အစီအစဉ် (Itinerary)။ ဘယ် Application ကို ဘယ်နှစ်ခု (Replicas) မောင်းရမယ်ဆိုတာ သတ်မှတ်တယ်။

Task (Replica) = ခရီးသွားတစ်ယောက်ချင်း (Individual Tourist)။ Service ရဲ့ တစ်ခုချင်းစီပါ။






Swarm vs Compose (ဘာကွာခြားလဲ) -

# Compose = Single Host ပေါ်မှာ Multi-Container App ကို စီမံတယ်။ (Development, Testing)

# Swarm = Cluster (Host များစွာ) ပေါ်မှာ Service တွေကို စီမံတယ်။ (Production)


Port 2377/tcp, 7946/tcp, 7946/udp, 4789/udp ကို ဖွင့်ထားရမယ်။

 ၁: Swarm ကို စတင်ခြင်း (Initialize)
# Command: docker swarm init --advertise-addr <IP>
# ပထမဆုံး Manager Node ကို Swarm အဖြစ် စတင်တယ်။
# --advertise-addr က တခြား Node တွေ ဘယ် IP နဲ့ ဆက်သွယ်ရမလဲဆိုတာ ပြတယ်။
docker swarm init --advertise-addr 192.168.1.10

# ရလဒ် (Output) -
# Swarm initialized: current node (abc123def456) is now a manager.
# 
# To add a worker to this swarm, run the following command:
#     docker swarm join --token SWMTKN-1-... 192.168.1.10:2377
#
# To add a manager to this swarm, run 'docker swarm join-token manager'

၂: Worker Node တွေကို ထည့်သွင်းခြင်း (Join)
# Command: docker swarm join --token <token> <manager-ip>:2377
# Manager က ထုတ်ပေးတဲ့ Token ကို သုံးပြီး Worker Node တွေ ထည့်တယ်။
# (ဒီ Command ကို Worker Node တွေမှာ ရိုက်ပါ)
docker swarm join --token SWMTKN-1-... 192.168.1.10:2377
# ရလဒ် (Output) -
# This node joined a swarm as a worker.

၃: Swarm Node တွေကို စစ်ဆေးခြင်း
# Command: docker node ls
# Swarm ထဲက Node အားလုံးကို စာရင်းပြတယ်။
# (Manager Node မှာ ရိုက်ပါ)
docker node ls
# ရလဒ် (Output) -
# ID                            HOSTNAME    STATUS    AVAILABILITY   MANAGER STATUS
# abc123def456 *                manager1    Ready     Active         Leader
# def456ghi789                  worker1     Ready     Active
# ghi789jkl012                  worker2     Ready     Active

၄: Service တစ်ခု ချထားခြင်း (Deploy)
# Command: docker service create --name web --replicas 3 -p 80:80 nginx:latest
# --replicas 3 က Nginx Container ၃ ခု မောင်းမယ်။
# -p 80:80 က Swarm Node အကုန်လုံးမှာ Port 80 ကို ဖွင့်တယ် (Ingress Mode)။
docker service create --name web --replicas 3 -p 80:80 nginx:latest
# ရလဒ် (Output) -
# overall progress: 3 out of 3 tasks
# 1/3: running   [=================================>]
# 2/3: running   [=================================>]
# 3/3: running   [=================================>]
# verify: Service converged

 ၅: Service ကို စစ်ဆေးခြင်း
# Command: docker service ls
# Service အားလုံးကို စာရင်းပြတယ်။
docker service ls
# ရလဒ် (Output) -
# ID            NAME    MODE        REPLICAS  IMAGE           PORTS
# xyz789abc123  web     replicated  3/3       nginx:latest    *:80->80/tcp
# Command: docker service ps web
# Service ရဲ့ Replica တွေကို အသေးစိတ် ပြတယ်။
docker service ps web
# ရလဒ် (Output) -
# ID            NAME    IMAGE           NODE      DESIRED STATE  CURRENT STATE
# 123abc456def  web.1   nginx:latest    worker1   Running        Running 30 seconds
# 456def789ghi  web.2   nginx:latest    worker2   Running        Running 30 seconds
# 789ghi123jkl  web.3   nginx:latest    manager1  Running        Running 30 seconds


၆: Service ကို Scale လုပ်ခြင်း
# Command: docker service scale web=5
# Replica အရေအတွက် ၃ ကနေ ၅ ကို တိုးမယ်။
docker service scale web=5
# ရလဒ် (Output) -
# web scaled to 5
# overall progress: 5 out of 5 tasks
# 1/5: running   [=================================>]
# ...
# verify: Service converged
# ပြန်စစ်ပါ။
docker service ls
# ရလဒ် - REPLICAS 5/5 ဖြစ်နေမယ်။

၇: Rolling Update လုပ်ခြင်း
# Command: docker service update --image nginx:1.23 --update-parallelism 2 --update-delay 20s web
# Nginx Version 1.23 ကို တစ်ခါ ၂ ခုနှုန်းနဲ့ ၂၀ စက္ကန့်ခြားပြီး Update လုပ်မယ်။
docker service update --image nginx:1.23 --update-parallelism 2 --update-delay 20s web
# Update လုပ်နေတာကို ကြည့်ပါ။
docker service ps web
# ရလဒ် (Output) -
# ID            NAME          IMAGE           NODE      DESIRED STATE  CURRENT STATE
# 123abc456def  web.1         nginx:1.23      worker1   Running        Running 10 seconds
# 456def789ghi  web.2         nginx:1.23      worker2   Running        Running 10 seconds
# 789ghi123jkl  web.3         nginx:1.23      manager1  Running        Running 10 seconds
# ...


 ၈: Service ကို ဖျက်ခြင်း
# Command: docker service rm web
# Service ကို ဖျက်တယ်။ (သတိထားပါ - ပြန်မယူနိုင်ဘူး)
docker service rm web
# ရလဒ် (Output) -
# web






၃။ Key Takeaways (အဓိက မှတ်စရာ ၃ ချက်)
# ၁။ Manager ကို ထူးခြားသော အရေအတွက် (၃၊ ၅) ထားပါ။

ဒါမှ Raft Consensus (အုပ်စုလိုက် ဆုံးဖြတ်ချက်) အတွက် ကောင်းတယ်။ (၂) လုံးထားရင် အန္တရာယ်များတယ်။ တစ်လုံးပျက်ရင် ကျန်တစ်လုံးတည်းနဲ့ ဆုံးဖြတ်လို့မရဘူး။

# ၂။ Service က Desired State (လိုချင်တဲ့ အခြေအနေ) ကို သတ်မှတ်တယ်။

ခင်ဗျားက "Nginx ၃ ခု မောင်းပါ" လို့ ပြောတယ်။ Swarm က ဒီအတိုင်း ထိန်းပေးတယ်။ (Self-healing) Container တစ်လုံးသေရင် အလိုအလျောက် ပြန်စတယ်။

# ၃။ Ingress Mode (Routing Mesh) က Swarm Node အကုန်လုံးမှာ Port ကို ဖွင့်ပေးတယ်။

Service ကို Port နဲ့ ချိတ်လိုက်ရင် Swarm Node အကုန်လုံးမှာ ဒီ Port ကို ဖွင့်ပေးတယ်။ ဘယ် Node ကိုပဲ ဝင်ဝင် Service ကို ရောက်တယ်။ (Load Balancing ပါတယ်)။