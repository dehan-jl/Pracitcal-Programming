def getBinary(num, length=7):
    binStr = ""
    while num:
        binStr = str(num % 2) + binStr
        num //= 2

    return binStr.rjust(length, "0")

def checkError(byte):
    count = 0
    errorq = 0
    parity = len(byte) % 2
    for j in range(len(byte)):
        if byte[j] == "1":
            count += 1
    if (count % 2) != parity:
        print("error picked up")
    elif count == len(byte):
        print("correct value")
    elif (count % 2) == parity:
        print("error not picked up")
        errorq = 1
    return errorq


#MAIN
ercount = 0
bits = int(input("Input number of bits: "))
for i in range(2**bits):
    print(i, getBinary(i, bits), end=' ')
    ercount += int(checkError(getBinary(i, bits)))

print(ercount)
print(((2**bits)/2)-1)

#The formula for the number of errors not picked up in "n" number of bits is
#((2**n)/2)-1
