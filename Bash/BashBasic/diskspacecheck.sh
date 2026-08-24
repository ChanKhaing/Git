#!/bin/bash

# Root Directory (/) ၏ Disk Usage Percentage ကို ရယူခြင်း
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

echo "Current Disk Usage on /: ${DISK_USAGE}%"

if [ "$DISK_USAGE" -gt 80 ];
 then
    echo "[ALERT] Disk space is above 80%!"
    echo "Top 3 largest directories in /var/log:"
    # du ဖြင့် ပမာဏအများဆုံး Directory ၃ ခုကို ရှာခြင်း
    du -sh /var/log/* 2>/dev/null | sort -rh | head -n 3
fi