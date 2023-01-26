'''
1. 리스트를 입력받아 for문을 돌려 빈 리스트에 추가한다
2. 오름차순으로 정렬한다
3. 출력한다.
'''
array = []
for _ in range(2):
    n = input()
    n_list = list(map(int, input().split()))
    for i in n_list:
        array.append(i)

array.sort()
print(' '.join(map(str, array)))

'''모범 답안
# 이문제를 낸 의도는 sort를 사용하지 않고 정렬하는 것이 목적이다.
# sort는 nlogn의 시간복잡도가 되는데 n번의 시간복잡도가 되는 정렬을 아래에 작성
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
c = []
while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p1 < n:
    c = c + a[p1:]
if p2 < m:
    c = c + b[p2:]
for x in c:
    print(x, end=' ')

'''