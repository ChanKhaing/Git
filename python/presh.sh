#!/bin/bash


# ၁။ $1 ကို အသုံးပြုပြီး ပထမဆုံးလူကို နှုတ်ဆက်ခြင်း
echo "hello hello  $1 ..."
echo "-----------------------------------"

# ၂။ $@ ကို အသုံးပြုပြီး ပေးပို့လိုက်သမျှ လူအားလုံးကို Loop ပတ်ပြီး နှုတ်ဆက်ခြင်း
echo "ရောက်လာကြတဲ့သူတွေ အားလုံးကတော့ -"

for name in "$@"
do
    echo "- $name"
done
echo "today the party person is $#" # $# က ပေးပို့လိုက်သမျှ argument အရေအတွက်ကို ပြန်ပေးတယ်
echo "The script name is $0"  #$0 က script name ကို ပြန်ပေးတယ်