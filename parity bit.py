count = 0
byte = input("Input byte: ")
for i in range(len(byte)):
    count += byte[i] == "1"

bit = 1 - count % 2
print(str(bit)+byte)