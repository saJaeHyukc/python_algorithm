'''
1. 약수를 구하는 함수를 구한다
2. 정렬하여 특정 인덱스를 뽑아준다.
3. 특정 인덱스가 넘어가면 -1을 출력하고 아니면 특정 인덱스 값을 출력
'''

a, b = map(int, input().split())
a_list = []

#약수 판단하고 추가
for i in range(1, a+1):
    if a % i == 0:
        a_list.append(i)
        
#정렬
a_list.sort()

# -1출력할지, 인덱스값 출력할지
if len(a_list) < b:
    print(-1)
else:
    print(a_list[b-1])

'''모범 답안
n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:`
        print(i)
        break
else: 
    print(-1)
'''
'''새로 알게된 정보
for else
'''