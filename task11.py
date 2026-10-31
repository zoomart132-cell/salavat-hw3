
def lcm(a, b):
    x = a
    y = b

    while y != 0:
        remainder = x % y
        x = y
        y = remainder

    gcd = x

    return (a * b) // gcd


print("LCM =", lcm(6, 8))
