
def isPalindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return original == reverse


if isPalindrome(121):
    print("Palindrome")
else:
    print("Not Palindrome")
