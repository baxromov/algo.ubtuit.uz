# 15
a, b, c = map(int, input().split())
_a, _b, _c = 1 / a, 1 / b, 1 / c
sum = _a + _b + _c
print(f"{1 / sum:.2f}")

# 16
from math import e

a, b = map(float, input().split())
c = (a + b) / (b ** 2 + abs((b ** 2 + 2) / (a + a ** 3 / 5))) + e ** (b + 2)
print(f"{c:.2f}")

# 17
from math import tan, pi, cos, log2

x, y = map(float, input().split())
f = 2 * tan(x + pi / 6) / (1 / 3 + cos(y + x ** 2) ** 2) + log2(x ** 2 + 2)
print(f'{f:.2f}')

# 18
from math import e, pow, atan, cos

x, y = map(float, input().split())
a = 1 / (x + 2 / x ** 2 + 3 / x ** 3) + pow(e, x ** 2 + 3 * x)
b = atan(x + y) + abs(5 + x) ** 2
c = cos(y ** 2 + x ** 2 / 2) ** 2
res = a / b - c
print(f'{res:.2f}')

# 19
from math import log, sqrt, cos, pow

x, y = map(float, input().split())
a = log(abs(
    (x + y) ** 2) + sqrt(abs(y) + 2) - (x - x * y / (x ** 2 / 2 - 5))
        )
b = cos(x + y) ** 2 / pow(x + y, 1 / 3)
res = a + b
print(f'{res:.2f}')

# 20
from math import cos, sin

x, y = map(float, input().split())
_a = (x ** 2 + 1)
a = _a / (x ** 2 + (x * y + y ** 2) / ((y ** 2) + (y + x * y) / (abs(x * y) + 5)))
b = 1 / (1 + cos(x) + 1 / sin(abs(x)))
res = a + b
print(f'{res:.2f}')

# 21
a, b = map(float, input().split())
x = pow(a, 1 / 5)
y = pow(b * (a + b) / (2 * b + a * b), 1 / 4)
z = (a ** 2 + b ** 2 + 2)
res = x + y * z
print(f"{res:.2f}")

# 22
from math import sin, tan

x1, x2, c, d = map(float, input().split())
a = abs(sin(abs(c * x2 ** 3 + d * x1 ** 3 - c * d)) ** 2 / pow(c * x1 ** 2 + d * x2 ** 2 + 7, 1 / 2))
b = tan(x1 * x2 ** 2 + d ** 3)
res = a + b
print(f'{res:.2f}')

# 23
from math import cos

a, b, c, d, x = map(float, input().split())
a, b, c, d = int(a), int(b), int(c), int(d)
_a = a * x ** 2 + b * x + c
_b = cos(abs((a * x + b) / (c * x + d + 2 ** c)))
if a == 0 and b - c < 0:
    res = _b
else:
    _c = x * a ** 3 + a * a + a ** (b - c)
    res = _a / _c + _b
print(f'{res:.2f}')

# 24
from math import sqrt, cos

a, b, c, x = map(float, input().split())
a, b, c = int(a), int(b), int(c)
_a = 8.2 * x ** 2 + sqrt(abs(x ** 3 + 3 * x) + cos(x - 2))
_b = a / 4 + b / 3 + c / 2 + 1
res = 0.75 + _a / _b
print(f'{res:.2f}')

# 25
from math import sqrt, log10

a, x = map(float, input().split())
a = int(a)
_a = sqrt(x - 1) + sqrt(x + 2) + log10(sqrt(a * x ** 2) + 2)
_b = sqrt(sqrt(x + 2) + sqrt(x + 24) + x ** 5)
res = _a / _b
print(f'{res:.2f}')

# 26
from math import sqrt, e, sin, log

a, x, y = map(float, input().split())
a = int(a)
_a = sqrt(
    e ** (x * y) - x * sin(a * x) - (x ** 2 + 2) / (abs(x) + 5)
)
_b = sqrt(log(x ** 2 + 2) + 5)
res = _a + _b
print(f'{res:.2f}')

# 27
from math import sqrt, cos, sin, tan

x = float(input())
a = sqrt((2 * tan(x + 2) - cos(x + 2 ** x)) / (1 + cos(x + 2) ** 2))
b = sin(x ** 2) / (x ** 2 + 3)
res = a + b
print(f'{res:.2f}')

# 28
from math import sin, cos, log10

a, x = map(float, input().split())
a = int(a)
_a = x * sin(x / 2 + x / 3 + x / 4)
_b = (log10(x ** 2 - 2) + 3 ** a) / (cos(x + 3) * sin(x + 3) + 8)
res = _a + _b
print(f'{res:.2f}')

# 29
from math import sqrt, e, cos, sin

a, x, y = map(float, input().split())
a = int(a)
res = sqrt(y ** 2 + e ** x + sqrt(e ** x + a / (x ** 2 + 2)) + cos(x) ** 2 / sin(x ** 2)) + cos(x) ** 3
print(f'{res:.2f}')

# 30
from math import sin, e, sqrt

x, y, z = map(float, input().split())
x = int(x)
res = 2 ** (-x) * sqrt(x + pow(abs(y) + 2, 1 / 4)) * pow((pow(e, x - 1)) / sin(z + 2) + 2, 1 / 3)
print(f'{res:.2f}')

# 31
x, y = map(float, input().split())
print(max(x, y), min(x, y))

# 32
x, y, z = map(float, input().split())
print(max(x, y, z), min(x, y, z))

# 33
x, y, z = map(float, input().split())
print(f'{max(x + y + z, x, y, z):.2f}', f'{min(x + y / 2, x, y, z) ** 2:.2f}')

# 34
a, b, c = map(int, input().split())
if a < b < c:
    print("YES")
else:
    print("NO")

# 35
a, b, c = map(int, input().split())
if c <= b <= a:
    print(a * 2, b * 2, c * 2)
else:
    print(abs(a), abs(b), abs(c))

# 36
a, b = map(int, input().split())
if a > b:
    print(a)
else:
    print(a, b)

# 37
a, b = map(int, input().split())
if a <= b:
    print(0, b)
else:
    print(a, b)

# 38
x, y, z = map(float, input().split())
s = x if 1 <= x <= 3 else None, y if 1 <= y <= 3 else None, z if 1 <= z <= 3 else None
a = list(filter(lambda x: x is not None, s))
print(' '.join(map(str, a)).strip())

# 39
x, y = map(int, input().split())
if x > y:
    print(f"{4 * x * y:.1f}", f"{(x + y) / 2:.1f}")
else:
    print(f"{(x + y) / 2:.1f}", f"{4 * x * y:.1f}")

# 40
x, y, z = map(int, input().split())
_x = x if x < 0 else x ** 2
_y = y if y < 0 else y ** 2
_z = z if z < 0 else z ** 2
print(_x, _y, _z)

# 41
x, y, z = map(float, input().split())
if x < 1 and y < 1 and z < 1:
    d = min(x, y, z)
    if x == d:
        print((y + z) / 2, y, z)
    elif y == d:
        print(x, (x + z) / 2, z)
    else:
        print(x, y, (x + y) / 2)
else:
    print(x, y, z)

# 42
a, b, c, d = map(float, input().split())
if a <= b <= c <= d:
    _max = max(a, b, c, d)
    print(_max, _max, _max, _max)
else:
    _min = min(a, b, c, d)
    print(_min, _min, _min, _min)

# 43
x, y = map(float, input().split())
if x < 0 and y < 0:
    print(abs(x), abs(y))
elif x > 0 and y > 0:
    print(x, y)
else:
    print(x + .5, y + .5)

# 44
x, y, z = map(int, input().split())
if x + y > z and x + z > y and y + z > x:
    print("YES")
else:
    print("NO")

# 45
from math import sqrt

a, b, c = map(int, input().split())
D = b ** 2 - 4 * a * c
if D < 0:
    print("NO")
else:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print(f"{x1:.2f}", f"{x2:.2f}")
