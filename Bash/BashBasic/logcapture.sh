#!/bin/bash

SERVICE="nginx"

# Service active ဖြစ်မဖြစ် စစ်ဆေးခြင်း
if systemctl is-active --quiet "$SERVICE"; then
    echo "Service $SERVICE is running normally."
else
    echo "[WARNING] Service $SERVICE is DOWN!"
    echo "Fetching last 5 error logs for $SERVICE:"
    # journalctl ဖြင့် နောက်ဆုံး Log ၅ ကြောင်း ဆွဲထုတ်ခြင်း
    journalctl -u "$SERVICE" -n 5 --no-pager
fi