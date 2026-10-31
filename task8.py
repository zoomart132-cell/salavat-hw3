
def decimalToBinary(n):
    binary = ""

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    return binary


number = 13
print("Binary =", decimalToBinary(number))
