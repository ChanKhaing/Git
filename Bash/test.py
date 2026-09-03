

result=[]



def process_items(items):
    global result
    for item in items:
        # result.append(item.low())
        result.append(item.upper())
    return result

def main():
    print("Processing items...")

if __name__ == "__main__":
    main()
    
# process_items(["hello", "world", "test"])
# print(result)