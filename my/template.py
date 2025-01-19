import math

def template(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print(None)
        return
    perim = a + b + c
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    ravn = (a == b or a == c or b == c)
    ravns = (a == b == c)

    print('периметр:', perim)
    print('площадь:', area)
    print(f"Равнобедренный: {'да' if ravn else 'нет'}")
    print(f"Равносторонний: {'да' if ravns else 'нет'}")