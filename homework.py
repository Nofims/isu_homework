"""Рыбаков Александр, УТС-41. Алгоритм А со звездой."""

from random import randrange as rd
import matplotlib.pyplot as plt

listOfPoints = []
setOfPoints = set()

x = 0
y = 0
quality = 0
# строим поле 4 на 4
while len(listOfPoints) < 16:
    listOfPoints.append([x, y, quality])
    x += 1
    if x == 4:
        x = 0
        y += 1
# координаты старта
startCoordinate = rd(0, 15)
while startCoordinate in setOfPoints:
    startCoordinate = rd(0, 15)
setOfPoints.add(startCoordinate)
listOfPoints[startCoordinate][2] = 1
# координаты препятствий
obstacleCoordinate = rd(0, 15)
i = 0
obstacleNumberList = []
while i < 3:
    while obstacleCoordinate in setOfPoints:
        obstacleCoordinate = rd(0, 15)
    setOfPoints.add(obstacleCoordinate)
    listOfPoints[obstacleCoordinate][2] = 2
    i += 1
    obstacleNumberList.append(obstacleCoordinate)
# координаты финиша
finishCoordinate = rd(0, 15)
while finishCoordinate in setOfPoints:
    finishCoordinate = rd(0, 15)
setOfPoints.add(finishCoordinate)
listOfPoints[finishCoordinate][2] = 3

# строим сетку - горизонтальные
plt.vlines(-0.5, -0.5, 3.5, color='b')
plt.vlines(0.5, -0.5, 3.5, color='b')
plt.vlines(1.5, -0.5, 3.5, color='b')
plt.vlines(2.5, -0.5, 3.5, color='b')
plt.vlines(3.5, -0.5, 3.5, color='b')
# и вертикальные линии
plt.hlines(-0.5, -0.5, 3.5, color='b')
plt.hlines(0.5, -0.5, 3.5, color='b')
plt.hlines(1.5, -0.5, 3.5, color='b')
plt.hlines(2.5, -0.5, 3.5, color='b')
plt.hlines(3.5, -0.5, 3.5, color='b')
# добавляем сетку
plt.grid()
# добавляем старт, препятствия и финиш
for i in range(16):
    if listOfPoints[i][2] == 1:
        plt.text(listOfPoints[i][0], listOfPoints[i][1], "S", size='large')
    if listOfPoints[i][2] == 2:
        plt.text(listOfPoints[i][0], listOfPoints[i][1], "x")
    if listOfPoints[i][2] == 3:
        plt.text(listOfPoints[i][0], listOfPoints[i][1], "F", size='large')
plt.grid()

f1 = f2 = f3 = f4 = 10
g = 0
x_s = listOfPoints[startCoordinate][0]
y_s = listOfPoints[startCoordinate][1]
x_f = listOfPoints[finishCoordinate][0]
y_f = listOfPoints[finishCoordinate][1]
x_1 = listOfPoints[obstacleNumberList[0]][0]
y_1 = listOfPoints[obstacleNumberList[0]][1]
x_2 = listOfPoints[obstacleNumberList[1]][0]
y_2 = listOfPoints[obstacleNumberList[1]][1]
x_3 = listOfPoints[obstacleNumberList[2]][0]
y_3 = listOfPoints[obstacleNumberList[2]][1]

print("Шаги, которые проделал агент:")
# алгоритм А со звездой
while x_s != x_f or y_s != y_f:
    if ((x_s - 1 != x_1) or (y_s != y_1)) and ((x_s - 1 != x_2)
                         or (y_s != y_2)) and ((x_s - 1 != x_3)
                         or (y_s != y_3)) and 3 >= x_s - 1 >= 0:
        f1 = g + abs(x_s - x_f - 1) + abs(y_s - y_f)
    if ((x_s != x_1) or (y_s - 1 != y_1)) and ((x_s != x_2)
                     or (y_s - 1 != y_2)) and ((x_s != x_3)
                     or (y_s - 1 != y_3)) and 3 >= y_s - 1 >= 0:
        f2 = g + abs(x_s - x_f) + abs(y_s - y_f - 1)
    if ((x_s + 1 != x_1) or (y_s != y_1)) and ((x_s + 1 != x_2)
                         or (y_s != y_2)) and ((x_s + 1 != x_3)
                         or (y_s != y_3)) and 3 >= x_s + 1 >= 0:
        f3 = g + abs(x_s - x_f + 1) + abs(y_s - y_f)
    if ((x_s != x_1) or (y_s + 1 != y_1)) and ((x_s != x_2)
                     or (y_s + 1 != y_2)) and ((x_s != x_3)
                     or (y_s + 1 != y_3)) and 3 >= y_s + 1 >= 0:
        f4 = g + abs(x_s - x_f) + abs(y_s - y_f + 1)
    f = min(f1, f2, f3, f4)
    if (f1 == f2 == f3 == f4) or (f1 > 50 or f2 > 50 or f3 > 50 or f4 > 50):
        print("Алгоритм не реализуем.")
        break
    if f == f1:
        x_a_l = x_s
        y_a_l = y_s
        x_s = x_s - 1
        y_s = y_s
    elif f == f2:
        x_a_l = x_s
        y_a_l = y_s
        x_s = x_s
        y_s = y_s - 1
    elif f == f3:
        x_a_l = x_s
        y_a_l = y_s
        x_s = x_s + 1
        y_s = y_s
    elif f == f4:
        x_a_l = x_s
        y_a_l = y_s
        x_s = x_s
        y_s = y_s + 1
    print('(x, y): ({}, {})'.format(x_s, y_s))
    plt.text(x_s, y_s, '.', color='m', size=35)
    g += 1
    f1 = f2 = f3 = f4 = 50

plt.show()
