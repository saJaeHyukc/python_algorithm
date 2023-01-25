'''
1. 해당 값이 소수이면 cnt를 1 증가시키고 제한된 숫자까지 1을 넣음
2. 제한된 숫자까지 for문을 돌려 cnt 값을 출력
'''

n = int(input())
ch = [0]*(n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)