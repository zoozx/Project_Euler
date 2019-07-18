def reverse (text):
    return str(text)[::-1]

def is_palindrome (text):
    return str(text) == reverse(text)

result = 0

for a in range(100, 999):
    b = a + 1
    cikl = True
    while cikl:
        b = b - 1
        c = a * b
        if (is_palindrome(c)):
            if result < c:
                result = c
            else:
                result = result
            cikl = False
        else:
            continue
print(result, 'Наибольший палиндром')
