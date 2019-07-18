run = True
running = True
a = 1
b = 1

while run:    #цикл который создает простые числа по очереди
    a = a + 2 #увеличиваем сило на 2 чтобы пропустить четные и сокрвтит время работы
    t = a
    running = True
    while running:  #цикл проверяет созданное число на делители
        t = t - 1
        if a % t == 0 and t > 1:
            running = False
        elif a % t == 0 and t == 1:  #это условие значит что число простое
            b = b + 1                #порядковый номер простого числа
            running = False
    if b == 10001:
        print(a)
        break
