
def draw(massive,y):
     for q in range(y):

          for g in massive[q]:
               print(g[0], end='')



def creator(x,y):
     massive = []
     for _ in range(y):
          massive.append([' ' for _ in range(x)])
     return massive


def coordination(symbol, x,y,x1,y1):
     massive = creator(x1,y1)
     massive[y][x] = symbol
     draw(massive,y1)

coordination('s',10,45,100,100)


