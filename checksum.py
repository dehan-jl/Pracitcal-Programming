word = input("Word: ")
values = []
total = 0
for i in range(len(word)):
    values.append(ord(word[i]))
    print(word[i], values[i], bin(values[i]))
    total += values[i]

checksum = total % 256
print("CS", checksum, bin(checksum))