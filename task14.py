
def transformDigits(n):
    result = 0
    place = 1

    while n > 0:
        digit = n % 10

        if digit % 2 == 0:
            digit = digit + 1
        else:
            digit = digit - 1

        result = result + digit * place
        place = place * 10
        n = n // 10

    return result


print(transformDigits(983210))
