'''
1. 뒤집는 함수 만들기 -> 리스트로 만들어 reverse로 뒤집고 정수로 만든다
2. 소수 판별 함수 만들기 -> for 문을 돌려 0으로 나누어 질 때 cnt가 1증가하고 cnt가 2일 때 True 아니면 False
3. for문을 돌려 그 함수가 뒤집었을 때 소수이면 출력함
'''

def reverse(x):
    x = list(str(x))
    x.reverse()
    return int(''.join(x))

def isPrime(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False

n = int(input())
n_list = list(map(int, input().split()))
for i in n_list:
    if isPrime(reverse(i)):
        print(reverse(i), end=' ')



'''모범 답안
def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res
    
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    else:
        return True

n = int(input())
n_list = list(map(int, input().split()))
for x in n_list:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
'''

