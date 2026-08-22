#!/bin/bash

# Configuration Thresholds
MIN_RAM_MB=500     # Minimum required free RAM in MB
MIN_DISK_PCT=90    # Maximum allowed disk usage percentage

echo "=== System Pre-Flight Checks ==="

# 1. Check Free RAM
FREE_RAM=$(free -m | awk '/^Mem:/ {print $7}')
echo "Available RAM: ${FREE_RAM} MB"
if [ "$FREE_RAM" -lt "$MIN_RAM_MB" ]; then
    echo "WARNING: Low memory! Less than ${MIN_RAM_MB} MB available."
fi

# 2. Check Available Disk Space (Root Partition)
DISK_USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')
echo "Disk Usage (/): ${DISK_USAGE}%"
if [ "$DISK_USAGE" -ge "$MIN_DISK_PCT" ]; then
    echo "WARNING: Disk space is running low (Over ${MIN_DISK_PCT}% capacity)."
fi

# 3. Check UFW Status & SSH Rule
echo "=== Checking Firewall Status ==="
if command -v ufw >/dev/null 2>&1; then
    UFW_STATUS=$(sudo ufw status | grep -i "Status: active")
    if [ -n "$UFW_STATUS" ]; then
        # Check if SSH (port 22 or 'OpenSSH') is allowed
        if sudo ufw status | grep -E -q "22/tcp|OpenSSH|SSH"; then
            echo "[OK] UFW is active and SSH rule is allowed."
        else
            echo "[ACTION] SSH rule missing! Allowing SSH in UFW..."
            sudo ufw allow ssh
        fi
    else
        echo "[INFO] UFW is currently inactive."
    fi
else
    echo "[INFO] UFW is not installed."
fi

# 4. Check Nginx Service Status
echo "=== Checking Nginx Service ==="
if systemctl is-active --quiet nginx; then
    echo "[OK] Nginx is already running."
else
    echo "[ACTION] Nginx is not running. Starting Nginx..."
    sudo systemctl start nginx
    
    # Confirm startup succeeded
    if systemctl is-active --quiet nginx; then
        echo "[SUCCESS] Nginx started successfully."
    else
        echo "[ERROR] Failed to start Nginx. Check logs with 'journalctl -u nginx'."
        exit 1
    fi
fi

echo "=== All Checks Complete ==="

