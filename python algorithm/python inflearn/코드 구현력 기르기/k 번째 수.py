'''
1. 테스트 케이스 입력받는다
2. n, s, e, k 를 순서대로 받는다
3. N개의 숫자를 차레대로 받는다
4. s에서 e까지를 슬라이싱 해서 리스트 저장 후 오름차순으로 정렬
5. k번째를 뽑는다
'''
T = int(input())
for i in range(1, T+1):
    N, s, e, k = map(int, input().split())
    n_list = list(map(int, input().split()))
    n_list = n_list[s-1:e]
    n_list.sort()
    print(f"#{i} {n_list[k-1]}")