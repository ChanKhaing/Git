#!/bin/bash

# ========================================================
# 🎯 Chan's Bash Learning Log & System Script
# "Be honest and love what we do, even if no one claps."
# ========================================================

echo "=================================================="
echo "          🌟 MY DAILY LEARNING LOG 🌟             "
echo "=================================================="

# ၁။ What is Shell? (သင်ယူမှု မှတ်တမ်း)
echo "1. [Shell Concept]: I learned that Shell is a bridge between me and the Kernel."

# ၂။ .bashrc & Alias Rule (Space မပါရတဲ့ သင်ခန်းစာ)
echo "2. [.bashrc Rule]: Put 'alias c=clear' in ~/.bashrc. NEVER use spaces around '='!"

# ၃။ Double Quotes vs Single Quotes Different
echo "3. [Quotes Rule]:"
Food="Apple"
echo "   - Double Quotes look inside: \"My favorite food is \$Food\" -> My favorite food is $Food"
echo '   - Single Quotes freeze text: '\''My favorite food is $Food'\'' -> My favorite food is $Food'

# ၄။ Semicolon (;) to chain commands & Read Input
echo "--------------------------------------------------"
echo "4. [Input & Semicolon Chain Demo]:"
read -p "What is your favourite game?: " Game ; echo "   - Wow! $Game is an amazing thing!"

# ၅။ Command Substitution $(...) using cat & grep -E
echo "--------------------------------------------------"
echo "5. [System Info Fetched by Me]:"

# ဒီနေ့ ရက်စွဲကို Command Substitution နဲ့ ဖမ်းမယ်
CURRENT_DATE=$(date)
echo "   - Date Check : $CURRENT_DATE"

# မင်းကိုယ်တိုင် စမ်းသပ်အောင်မြင်ခဲ့တဲ့ OS Release Fetch နည်းလမ်း
OS_INFO=$(cat /etc/os-release | grep -E "PRETTY_NAME|ID_LIKE")
echo "   - OS Info Check:"
echo "$OS_INFO"

echo "=================================================="
echo "🎉 Script Executed Successfully! Exit Code: $?"
echo "=================================================="