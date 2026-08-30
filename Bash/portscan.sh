#!/bin/bash

# သုံးစွဲသူထံမှ Target Input တောင်းယူခြင်း
read -p "Scan ဖတ်ချင်သည့် Domain သို့မဟုတ် IP ထည့်ပါ (eg. scanme.nmap.org သို့မဟုတ် 127.0.0.1): " TARGET_INPUT

if [ -z "$TARGET_INPUT" ]; then
    echo "[-] Target ထည့်သွင်းပေးရန် လိုအပ်ပါသည်။"
    exit 1
fi

# Python ကိုသုံးပြီး Domain မှ IP ပြောင်းခြင်း နှင့် Valid Target စစ်ခြင်း
TARGET_IP=$(python3 -c "
import socket, sys
try:
    ip = socket.gethostbyname('$TARGET_INPUT')
    print(ip)
except Exception:
    print('ERROR')
")

if [ "$TARGET_IP" == "ERROR" ]; then
    echo "[-] Error: '$TARGET_INPUT' အား ရှာမတွေ့ပါ သို့မဟုတ် Hostname မှားယွင်းနေပါသည်။"
    exit 1
fi

echo ""
echo "=========================================="
echo " Target: $TARGET_INPUT ($TARGET_IP)"
echo " Port Scanning & Service Detecting စတင်နေပါသည်..."
echo "=========================================="

# စစ်ဆေးမည့် Port များနှင့် Service အမည်များ (Port:Service)
PORTS=(
    "21:FTP"
    "22:SSH"
    "23:Telnet"
    "25:SMTP"
    "53:DNS"
    "80:HTTP"
    "110:POP3"
    "443:HTTPS"
    "3306:MySQL"
    "3389:RDP"
    "8080:HTTP-Proxy"
)

OPEN_COUNT=0

for ITEM in "${PORTS[@]}"; do
    PORT="${ITEM%%:*}"
    SERVICE="${ITEM##*:}"

    # Bash ၏ Netcat (nc) ဖြင့် Port အလုပ်လုပ်နေသလား အမြန်စစ်ခြင်း (Timeout: 1s)
    nc -z -w 1 "$TARGET_IP" "$PORT" 2>/dev/null
    
    if [ $? -eq 0 ]; then
        OPEN_COUNT=$((OPEN_COUNT + 1))
        echo ""
        echo "[+] Port $PORT ($SERVICE) is OPEN!"

        # Netcat သို့မဟုတ် Python ဖြင့် Banner Detail ကို ဖမ်းယူခြင်း
        BANNER=$(nc -v -w 2 "$TARGET_IP" "$PORT" 2>&1 | grep -v "succeeded")

        # Banner ဖမ်းယူရာတွင် ပိုမိုသန့်ရှင်းစေရန် Python သုံး၍ Format လုပ်ခြင်း
        CLEAN_BANNER=$(python3 -c "
import socket, sys

port = $PORT
ip = '$TARGET_IP'
banner = '''$BANNER'''.strip()

# Netcat မှ Banner မရပါက Python Socket ဖြင့် HEAD request ပို့ကြည့်ခြင်း
if not banner and port in [80, 443, 8080]:
    try:
        s = socket.socket()
        s.settimeout(1.5)
        s.connect((ip, port))
        s.send(b'HEAD / HTTP/1.1\r\nHost: ' + ip.encode() + b'\r\n\r\n')
        banner = s.recv(512).decode('utf-8', errors='ignore').splitlines()[0]
        s.close()
    except:
        banner = 'No Banner Response'

# Output ကို စာတစ်ကြောင်းတည်း သန့်ရှင်းအောင် ဖြတ်ထုတ်ခြင်း
first_line = banner.splitlines()[0] if banner else 'Unknown Service Details'
print(first_line[:80])
")
        echo "    └── Service Details: $CLEAN_BANNER"
    fi
done

echo ""
echo "=========================================="
if [ $OPEN_COUNT -eq 0 ]; then
    echo "[-] စစ်ဆေးခဲ့သော Common Ports များထဲတွင် ပွင့်နေသော Port မတွေ့ရှိပါ။"
else
    echo "[✓] စုစုပေါင်း ပွင့်နေသော Port ($OPEN_COUNT) ခု တွေ့ရှိခဲ့ပါသည်။"
fi
echo "=========================================="