def getBinary(num, length=7):
    binStr = ""
    while num:
        binStr = str(num % 2) + binStr
        num //= 2

    return binStr.rjust(length, "0")

num = int(input("Input num less than 127: "))
print(getBinary(num))