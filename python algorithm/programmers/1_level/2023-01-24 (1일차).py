'''
약수의 합
'''
def solution(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += i
    return cnt
