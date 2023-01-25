'''
1. 자연수 각자릿수의 합을 더하는 함수를 만든다
2. n을 입력받는다
3. n의 갯수의 자연수를 입력받는다
3. for문을 돌려 각자릿수의 합을 더한 값보다 크면 변수에 할당한다
4. x를 출력한다.
'''

def digit_sum(x):
    x = list(map(int, str(x)))
    return sum(x)

n = int(input())
n_list = list(map(int, input().split()))
x = 0
for i in n_list:
    if digit_sum(i) > digit_sum(x):
        x = i
print(x)

'''모범 답안 1
n = int(input())
n_list = list(map(int, input().split()))

def digit_num(x):
    sum = 0
    while x>0:
        sum += x % 10
        x = x // 10
    return sum

max = -2147000000

for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)
'''

'''모범 답안 2
n = int(input())
n_list = list(map(int, input().split()))

def digit_num(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

max = -2147000000

for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)
'''