'''
함수 만들기
'''

def add(a, b):
    c = a + b
    print(c)

add(3, 2)
add(5, 7)

def add(a, b):
    c = a + b
    return c

print(add(3, 2))

x = add(3, 2)
print(x)

def add(a, b):
    c = a + b
    d = a - b
    return c, d # 두개를 리턴 가능

print(add(3, 2)) # (5, 1)

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

a = [12, 13, 7, 9, 19]
for y in a:
    if is_prime(y):
        print(y, end=' ')