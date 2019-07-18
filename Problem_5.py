r = 0
cikl = True
while cikl:
    r = r + 10
    if r % 2 == 0:
        if r % 3 == 0:
            if r % 4 == 0:
                if r % 5 == 0:
                    if r % 6 == 0:
                        if r % 7 == 0:
                            if r % 8 == 0:
                                if r % 9 == 0:
                                    if r % 10 == 0:
                                        if r % 11 == 0:
                                            if r % 12 == 0:
                                                if r % 13 == 0:
                                                    if r % 14 == 0:
                                                        if r % 15 == 0:
                                                            if r % 16 == 0:
                                                                if r % 17 == 0:
                                                                    if r % 18 == 0:
                                                                        if r % 19 == 0:
                                                                            if r % 20 == 0:
                                                                                print(r)
                                                                                cikl = False


# Вторая реализация

d = 0
c = False
p = (3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

while c is False:
    d = d + 10
    for j in p:
        if d % j == 0:
            c = True
        else:
            c = False
            break
print(d)
