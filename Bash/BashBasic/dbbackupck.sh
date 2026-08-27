#!/bin/bash

DB_NAME="production_db"
DB_USER="root"
DB_PASS="SecurePassword123"
BACKUP_DIR="/backups/mysql"
DATE=$(date "+%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_$DATE.sql.gz"

# Backup folder မရှိပါက ဆောက်ခြင်း
mkdir -p "$BACKUP_DIR"

# Database ကို Dump လုပ်ပြီး compress လုပ်ခြင်း
mysqldump -u"$DB_USER" -p"$DB_PASS" "$DB_NAME" | gzip > "$BACKUP_FILE"

if [ $? -eq 0 ]; then
    echo "Backup successful: $BACKUP_FILE"
    # ရက် ၃၀ ထက်ဟောင်းသော backup အဟောင်းများကို ဖျက်ခြင်း
    find "$BACKUP_DIR" -type f -name "*.sql.gz" -mtime +30 -delete
else
    echo "Backup failed!"
fi