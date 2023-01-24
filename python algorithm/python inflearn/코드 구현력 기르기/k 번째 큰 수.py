'''
1. N장의 수의 카드와, K 번쨰로 큰 수를 입력받는다
2. N장의 수들을 입력받는다
3. 3장을 뽑아 더할 수 있는 경우의 수를 모두 구한다
4. 중복제거 후 내림차순으로 정렬한다
5. K번째로 큰수를 출력한다.
'''
N, K = map(int, input().split())
N_list = list(map(int, input().split()))
res = set()
for i in range(N):
    for j in range(i+1, N):
        for m in range(j+1, N):
            res.add(N_list[i] + N_list[j] + N_list[m])
res = list(res)
res.sort(reverse=True)
print(res[K-1])

'''새로 알게된 정보
미리 set을 지정하여 추가하면 중복 방지를 할 수 있다.
<집합 관련 함수들>
add 값 1개 추가하기
update 값 여러 개 추가하기
remove 특정 값 제거하기
'''