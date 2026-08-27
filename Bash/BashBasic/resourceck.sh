#!/bin/bash

# Available RAM ရာခိုင်နှုန်း စစ်ဆေးခြင်း
FREE_MEM=$(free | grep Mem | awk '{print $4/$2 * 100.0}')
# Used RAM ရာခိုင်နှုန်း တွက်ချက်ခြင်း
# USED_MEM=$(printf "%.0f" $(echo "100 - $FREE_MEM" | bc))
USED_MEM=$(( 100 - FREE_MEM ))

THRESHOLD=85

if [ "$USED_MEM" -gt "$THRESHOLD" ]; then
    echo "[ALERT] High Memory Usage Detected: ${USED_MEM}%"
    echo "Top 5 Memory Consuming Processes:"
    # Memory အများဆုံး စားနေသော Process ၅ ခုကို ပြခြင်း
    ps aux --sort=-%mem | head -n 6
else
    echo "[OK] Memory Usage is at normal level: ${USED_MEM}%"
fi