import datetime
import turtle
print(datetime.datetime.today())
# Здесь можно передать временную зону для других городов.
print(datetime.datetime.now())
# Позволяет выставить разницу между датами (для пробного периода).
# Начальная дата регистрации.
d1 = datetime.datetime.today()
print(d1)
# Допустим дата, с которой начинается выводиться предупреждение о окончании периода.
d2 = d1 + datetime.timedelta(days=330)
print(d2)
# Допустим дата с которой мы закрываем доступ к пробному продукту.
d1 = d1 + datetime.timedelta(days=365)
print(d1)
# Для определения разницы во времени.
print(d1-d2)
# Для определения разницы во времени, по определённым аргументам (здесь в днях).
# Но, если разницы нет, то ничерта не покажет.
print((d1-d2).days)
# Можно менять формат вывода времени через strftime (для полного обзора кодов загляни в документацию,
# через F1 в IDLE Shell).
print(d1.strftime('%A %d %B %Y'))

# Рисуем с помощью черепахи
t = turtle
t.pen()

# RGB Красный, Синий, Зелёный, длина квадрата


def kvadrat(r, g, b, s):
    t.down()
    t.color(r, g, b)
    t.begin_fill()
    t.forward(s)
    t.left(90)
    t.forward(s)
    t.left(90)
    t.forward(s)
    t.left(90)
    t.forward(s)
    t.left(90)
    t.end_fill()
    t.up()
    

t.up()
t.forward(100)
kvadrat(0, 1, 1, 40)

t.forward(100)
kvadrat(1, 0, 0, 50)
t.left(90)
t.forward(100)
kvadrat(0, 1, 0, 30)
t.forward(50)
t.color('blue', 'red')
t.down()
for i in range(1, 20):
    t.begin_fill()
    t.forward(60)
    t.left(40)
    t.begin_fill()
t.up()
t.forward(100)
t.down()
# RGB Красный, Синий, Зелёный
t.color(1, 0, 1)
t.begin_fill()
t.pensize(3)
t.circle(100)
t.end_fill()
t.done()

print(dir(turtle))
input()
