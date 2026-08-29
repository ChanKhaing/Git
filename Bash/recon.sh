#!/bin/bash

# သုံးစွဲသူထံမှ Input တောင်းယူခြင်း
read -p "Domain သို့မဟုတ် IP Address ထည့်ပါ (eg. google.com သို့မဟုတ် 8.8.8.8): " TARGET

if [ -z "$TARGET" ]; then
    echo "Input တစ်ခုခု ထည့်ပေးရန် လိုအပ်ပါသည်။"
    exit 1
fi

echo ""
echo "=========================================="
echo " Target ကို စစ်ဆေးနေပါသည်: $TARGET"
echo "=========================================="

# ၁။ Input က IP ဖြစ်မဖြစ် စစ်ဆေးရန် Python အကူအညီယူခြင်း
IS_IP=$(python3 -c "
import socket, sys
try:
    socket.inet_aton('$TARGET')
    print('true')
except:
    print('false')
")

if [ "$IS_IP" == "true" ]; then
    echo ""
    echo "[+] IP Address အမျိုးအစားဖြစ်ပါသည်။ Domain ပြန်ရှာနေပါသည်..."
    
    # Reverse DNS Lookup (IP -> Domain)
    RESULT=$(host "$TARGET" 2>/dev/null)
    
    if [ $? -eq 0 ]; then
        echo "--- ရှာဖွေတွေ့ရှိသော Domain/PTR Record ---"
        echo "$RESULT"
    else
        echo "[-] ဒီ IP အတွက် Domain Name (PTR Record) မတွေ့ရှိပါ။"
    fi

else
    echo ""
    echo "[+] Domain Name အမျိုးအစားဖြစ်ပါသည်။ IP Address ရှာနေပါသည်..."
    
    # Domain -> IP Lookup
    RESULT=$(host -t A "$TARGET" 2>/dev/null)
    
    if [ $? -eq 0 ]; then
        echo "--- ရှာဖွေတွေ့ရှိသော IP Address ---"
        echo "$RESULT"
    else
        echo "[-] Domain ကို IP မပြောင်းနိုင်ပါ (သို့မဟုတ်) Domain မရှိပါ။"
    fi

    # ၂။ Subdomain စစ်ဆေးခြင်း
    echo ""
    echo "[+] '$TARGET' အတွက် Subdomain များကို စစ်ဆေးနေပါသည်..."
    
    SUBDOMAINS=("www" "mail" "blog" "dev" "admin" "api" "app" "shop" "portal")
    FOUND=0

    for SUB in "${SUBDOMAINS[@]}"; do
        FULL_SUB="${SUB}.${TARGET}"
        
        # Bash ကနေ host command ရိုက်ပြီး Output ကို Python နည်းဖြင့် IP ပဲ သီးသန့်ဆွဲထုတ်ခြင်း
        LOOKUP=$(host -t A "$FULL_SUB" 2>/dev/null)
        
        if echo "$LOOKUP" | grep -q "has address"; then
            # Python သုံးပြီး Result ထဲမှ IP ကို သန့်ရှင်းစွာ ဖြတ်ယူခြင်း
            CLEAN_OUTPUT=$(python3 -c "
import sys
text = '''$LOOKUP'''
ip = text.split('has address')[-1].strip()
print(f'  [✓] တွေ့ရှိသော Subdomain: $FULL_SUB -> IP: {ip}')
")
            echo "$CLEAN_OUTPUT"
            FOUND=1
        fi
    done

    if [ $FOUND -eq 0 ]; then
        echo "  [-] စစ်ဆေးခဲ့သော Common Subdomain များထဲတွင် မည်သည့် Subdomain မှ မတွေ့ရှိပါ။"
    fi
fi