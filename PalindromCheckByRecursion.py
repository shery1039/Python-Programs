def PalindromRecursive(str, start, end):
    if start >= end:
        return True
    if str[start] != str[end]:
        return False
    return PalindromRecursive(str, start + 1, end - 1)

str = "radar"
n = len(str) - 1

is_palindrome = PalindromRecursive(str, 0, n)