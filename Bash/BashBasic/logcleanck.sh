#!/bin/bash

LOG_DIR="/var/log/myapp"
DAYS=7

echo "[$(date)] Starting Log Cleanup..."

# Directory ရှိမရှိ စစ်ဆေးခြင်း
if [ -d "$LOG_DIR" ]; then
    # ၇ ရက်ထက်ဟောင်းသော .log file များကို ရှာပြီး ဖျက်ခြင်း
    find "$LOG_DIR" -type f -name "*.log" -mtime +$DAYS -exec rm -f {} \;
    echo "Successfully deleted logs older than $DAYS days."
else
    echo "Directory $LOG_DIR does not exist!"
fi