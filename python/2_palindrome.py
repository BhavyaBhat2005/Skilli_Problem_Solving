def isPalondrome(s: str) -> bool:
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

s = input("Enter a string: ")
print(isPalondrome(s))