from random import randint


def mazes(m, n):
    m += 2
    n += 2
    print(m,n)
    maze = [[1 for i in range(n)] for j in range(m)]
    for x in range(1, m-1):
        for y in range(1, n-1):
            if(x == 1 and y == 1) or (x == m-2 and y == n-2):
                maze[x][y] = 0
            else:
                maze[x][y] = randint(0, 1)
    return maze

if __name__ == '__main__':
    m, n = int(input()), int(input())
    mazes(m, n)


