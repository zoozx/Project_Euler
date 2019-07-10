k=0
for i in range(1, 1000):
    if i % 3 == 0:
        k=k+i
        #print(k)
    elif i % 5 == 0:
        k=k+i
        #print(k)
    else:
        k=k
print(k)
