'''
1. n의 리스트를 작성
2. 빈 리스트를 작성, tmp라는 인덱스 번호를 a - 1만큼 담는다
3. 범위를 입력받고 n의 범위만큼 빈 리스트에 담는다
4. 빈 리스트를 역순으로 바꾼다
5. for 돌려 n에 빈리스트에 들어 있는 요소를 삭제
6. for 돌려 n에 tmp에 해당하는 인덱스 번호에다 빈 리스트 요소를 하나씩 삽입
7. tmp를 1씩 증가시킴
8. 빈 리스트를 초기화
9. n의 리스트 출력
'''
n = list(range(21))
blank_list = []

for _ in range(10):
    a, b = map(int, input().split())
    tmp = a - 1
    blank_list = n[a-1:b]
    blank_list.reverse()
    
    #n 요소 제거 
    for j in range(len(blank_list)):
        n.remove(blank_list[j])
    
    #n에 blank_list 요소 삽입
    for j in range(len(blank_list)):
        n.insert(tmp, blank_list[j])
        tmp += 1
        
    blank_list.clear()

n = ' '.join(map(str, n))
print(n)

'''모범답안
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1) // 2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0)
for x in a
    print(x, end=' ')

'''