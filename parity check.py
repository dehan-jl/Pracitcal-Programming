count = 0
byte = input("Input byte: ")
for i in range(len(byte)):
    count += byte[i] == "1"

print("Error" if count % 2 else "No error")