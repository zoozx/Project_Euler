b = 0
c = 0

for i in range(1, 101):
    k = i ** 2
    c = c + i
    b = b + k
result = (c ** 2) - b

print(result)
