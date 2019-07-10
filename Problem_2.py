k = 1
t = 2
result = 0
while True:
    k = k + t
    #print(k)
    if k >= 4000000:
        break
    elif k % 2 == 0:
        result = result + k
    t = t + k
    #print(t)
    if t >= 4000000:
        break
    elif t % 2 == 0:
        result = result + t

#print(k)
#print(t)
print(result)
