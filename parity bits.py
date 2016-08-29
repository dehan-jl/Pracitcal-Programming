EVEN = 0
ODD = 1

def getBinary(num, length=7):
    binStr = ""
    while num:
        binStr = str(num % 2) + binStr
        num //= 2

    return binStr.rjust(length, "0")

def parityBit(byte, parity):
    count = 0
    for char in range(len(byte)):
        if byte[char] == "1":
            count += 1
    if (count % 2) == parity:
        byte = "0" + byte
    else:
        byte = "1" + byte
    return byte

def getNumbers(numberOf):
    bytes = []
    count = 0
    while count < 5:
        n = int(input("Input a number less than 127: "))
        if n < 127:
            bytes.append(getBinary(n))
            count += 1
    return bytes

def putParity(bytes):
    for byte in range(len(bytes)):
        bytes[byte] = parityBit(bytes[byte], ODD)
    return bytes

def printBlock(block):
    for j in range(len(block)):
        print(block[j])

#MAIN
block = getNumbers(5)
block = putParity(block)
printBlock(block)