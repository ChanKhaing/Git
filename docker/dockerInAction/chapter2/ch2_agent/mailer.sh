#!/bin/sh

echo "Mailer service is UP and listening on port 33333"

while true
do
    # ဒီနေရာမှာ nc က data ကိုလက်ခံပြီး log ထုတ်ပေးတယ်
    nc -l -p 33333 | while read line
    do
        if [ -n "$line" ]; then
            echo "Sending email: $line"
            echo "Email sent at $(date)"
            echo "----------------------------------------"
        fi
    done
done