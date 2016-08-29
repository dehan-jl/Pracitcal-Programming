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

def justParityBit(byte, parity):
    count = 0
    for char in range(len(byte)):
        if byte[char] == "1":
            count += 1
    if (count % 2) == parity:
        byte = "0"
    else:
        byte = "1"
    return byte

def getNumbers(numberOf):
    bytes = []
    count = 0
    while count < numberOf:
        n = int(input("Input a number less than 127: "))
        if n < 127:
            bytes.append(getBinary(n))
            count += 1
    return bytes

def putParityBit(bytes):
    for byte in range(len(bytes)):
        bytes[byte] = parityBit(bytes[byte], ODD)
    return bytes

def printBlock(block):
    for j in range(len(block)):
        print(block[j])

def getParityByte(bytes, n):
    byte = ""
    for i in range(8):
        tbyte = ""
        for j in bytes:
            tbyte = j[i] + tbyte
        byte += justParityBit(tbyte, ODD)
    return byte

#MAIN
num = 5
block = getNumbers(num)
block = putParityBit(block)
printBlock(block)
print(getParityByte(block, num))
