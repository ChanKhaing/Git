
import subprocess
import socket

def lookup_domain_or_ip(target):
    target = target.strip()
    print("\n==========================================")
    print(f" Target ကို စစ်ဆေးနေပါသည်: {target}")
    print("==========================================")

    # ၁။ Input က IP ဖြစ်မဖြစ် စစ်ဆေးခြင်း
    is_ip = False
    try:
        socket.inet_aton(target)
        is_ip = True
    except OSError:
        is_ip = False

    if is_ip:
        print("\n[+] IP Address အမျိုးအစားဖြစ်ပါသည်။ Domain ပြန်ရှာနေပါသည်...")
        # Reverse DNS Lookup (IP -> Domain)
        cmd = ['host', target]
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            print("--- ရှာဖွေတွေ့ရှိသော Domain/PTR Record ---")
            print(result.stdout.strip())
        else:
            print("[-] ဒီ IP အတွက် Domain Name (PTR Record) မတွေ့ရှိပါ။")

    else:
        print("\n[+] Domain Name အမျိုးအစားဖြစ်ပါသည်။ IP Address ရှာနေပါသည်...")
        # Domain -> IP Lookup
        cmd = ['host', '-t', 'A', target]
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            print("--- ရှာဖွေတွေ့ရှိသော IP Address ---")
            print(result.stdout.strip())
        else:
            print("[-] Domain ကို IP မပြောင်းနိုင်ပါ (သို့မဟုတ်) Domain မရှိပါ။")