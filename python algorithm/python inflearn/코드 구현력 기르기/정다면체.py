'''
1. n과 M을 입력받는다
2. 이중 for문으로 더한 값을 인덱스에 저장
3. cnt의 최댓값 찾기
4. 최댓값과 cnt의 합이 일치하면 그의 인덱스 값 출력
'''
n, m = map(int, input().split())
cnt = [0] * (n+m+1)
max =-21470000000

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

for i in range(n+m+1):
    if cnt[i] > max:
        max=cnt[i]

for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=' ')