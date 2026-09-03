import json
import sys

def process_items(items):
    """List ကို process လုပ်တယ် (မင်း ဒီနေ့ သင်ထားတာ)"""
    result = []
    for item in items:
        result.append(item.upper())  # စာလုံးကြီးပြောင်း
    return result

def main():
    # Laravel က ပို့လိုက်တဲ့ JSON ကို လက်ခံမယ်
    input_data = sys.argv[1] if len(sys.argv) > 1 else '{"items": []}'
    data = json.loads(input_data)

    # Process လုပ်မယ်
    processed = process_items(data.get('items', []))

    # JSON အနေနဲ့ ပြန်ပို့မယ်
    result = {
        "status": "success",
        "processed": processed,
        "count": len(processed)
    }
    print(json.dumps(result))

if __name__ == "__main__":
    main()
