'''
리스트와 내장함수(1)
'''
import random
a = []
print(a) # []
b = list()
print(b) # []

a = [1, 2, 3, 4, 5]
print(a) # [1, 2 ,3 ,4 ,5]
print(a[0]) # 1

b = list(range(1, 11))
print(b) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

c = a + b
print(c) # [1, 2 ,3 ,4 ,5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a.append(6)
print(a) # [1, 2 ,3 ,4 ,5, 6] append 뒤에 추가해줌

a.insert(3, 7)
print(a) # [1, 2 ,3 7, 4 ,5, 6] insert 3인덱스 지점에 7을 넣음

a.pop()
print(a) # [1, 2 ,3, 7, 4 ,5] pop 맨뒤에 인덱스를 뺌

a.pop(3)
print(a) # [1, 2 ,3, 4 ,5] pop 3번째 인덱스 지점에 있는 걸 뺌

a.remove(4)
print(a) # [1, 2, 3, 5] remove 특정 인덱스를 제거함

print(a.index(5)) # 3 index 해당 인덱스가 몇번 째에 있는지 알려줌

a = list(range(1, 11))
print(sum(a)) # 55 sum list에 있는 인자값을 전부 더해줌
print(max(a)) # 10 max list의 인자값 중 최댓값을 구해줌
print(min(a)) # 1 min list의 인자값 중 최솟값을 구해줌

random.shuffle(a)
print(a) # shuffle 랜덤으로 인자값을 섞음

a.sort()
print(a) # sort 오름차순으로 출력

a.sort(reverse=True)
print(a) # sort reverse 내림차순으로 출력

a.clear()
print(a) #빈리스트를 출력
