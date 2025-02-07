def palindrome(a):
    a = a.replace(" ", "").lower()
    return a == a[::-1]