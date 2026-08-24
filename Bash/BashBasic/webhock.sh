#!/bin/bash

WEBHOOK_URL="https://httpbin.org/post"

# JSON Payload ပြင်ဆင်ခြင်း
PAYLOAD=$(jq -n \
  --arg msg "System health check completed successfully." \
  --arg status "OK" \
  '{message: $msg, status: $status}')

# curl ဖြင့် API/Webhook သို့ POST request ပို့ခြင်း
echo "Sending report..."
RESPONSE=$(curl -s -X POST -H "Content-Type: application/json" -d "$PAYLOAD" "$WEBHOOK_URL")

# JSON Response ထဲမှ status code ကို jq ဖြင့် ပြန်ထုတ်ခြင်း
echo "Server Response Status: $(echo "$RESPONSE" | jq -r '.json.status')"