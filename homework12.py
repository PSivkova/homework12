#    Создайте новую функцию def test... с произвольным числом параметров разного типа,
#    функция должна распечатывать эти параметры внутри своего тела
#    Создайте рекурсивную функцию, которая будет считать факториал от числа n, n - передается в параметре

def test(txt, *args, a=None, **kwargs):
    if a is None:
        a = [8, 7, 6]
    print(txt, *args, a, kwargs)


test("Набор чисел", 5, 6, 8, name='Den', city='Moscow')


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(8))
