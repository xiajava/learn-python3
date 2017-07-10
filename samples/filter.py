def is_palindrome(n):
    s = str(n)
    i = 0
    j = int(len(s)) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


output = filter(is_palindrome, range(1, 1000))
print(list(output))
