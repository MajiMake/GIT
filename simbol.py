def draw(massive, y, x, ):
    dam = 0
    for q in range(y):

        for g in massive[q]:
            dam += 1

            if dam == x:
               dam = 0
               print(g[0])
            else:
                print(g[0], end='')


def creator(x, y):
    massive = []
    for _ in range(y):
        massive.append([' ' for _ in range(x)])
    return massive


def coordination(symbol, x, y, x1, y1):
    massive = creator(x1, y1)
    massive[y][x] = symbol
    draw(massive, y1, x1)


coordination('s', 22, 17, 100, 100)
