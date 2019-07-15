k = 13195
t = k
running = True
runs = True
prost = False

while runs:
    t = t - 1
    if t == 1:
        print("Число простое и не имееет делителей")
        runs = False
    elif k % t == 0:
        result = t
        running = True
        while running:
            result = result - 1
            if t % result == 0 and result > 1:
                prost = False
                running = False
            elif t % result == 0 and result == 1:
                prost = True
                running = False
        if prost == True:
            print(t)
            runs = False
        else:
            continue
