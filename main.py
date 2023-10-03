import math


def delSecondElement(array:list):
    return array[::2]
print(delSecondElement([1, 2, 3, 4, 5, 6, 7, 8, 9]))

print('hi')


def fibonachi(n):
    if n == 0 or n == 1:
        return n
    return fibonachi(n - 1) + fibonachi(n - 2)
print(fibonachi(7))


def primer(m):
    if m == -2 or m == -3:
        return m
    return primer(m - 2) + primer(m - 1)
print(primer(2))


import math

num = int(input('Введите количество секторов: '))
radius = int(input('Введите радиус круга: '))

def ploshad(num, radius):
    pl = math.pi * radius ** 2
    res = pl / num
    return res

print(ploshad(num, radius))
