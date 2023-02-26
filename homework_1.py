a = float(input())
b = float(input())
c = float(input())
if a == 0:
    print('Уравнение не является квадратичным')
else:
    d = b**2-4*a*c
    if d < 0:
        print('Нет корней')
    if d == 0:
        print('x1 =', (-b)/(2*a))
    if d > 0:
        print('x1 =',((-b + d**0.5)/(2*a)))
        print('x2 =',((-b - d**0.5)/(2*a)))
