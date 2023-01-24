'''
리스트와 내장함수(2)
'''
'''요약
enumerate: 튜플로 해당 인덱스 번호와 값을 출력 
ex) for index, value in enumerate(a)으로 많이 씀
all: 조건이 모두 참이면 True
any: 조건이 하나라도 참이면 True
'''
a = [23, 12, 36, 53, 19]
print(a[:3]) # [23, 12, 36]
print(a[1:4]) # [12, 36, 53]
print(len(a)) # 5 len 리스트의 길이를 말해줌

for i in range(len(a)):
    print(a[i], end=' ') # 23 12 36 53 19

for x in a:
    print(x, end=' ') # 23 12 36 53 19
    
for x in enumerate(a): 
    print(x) # (0, 23) (1, 12) (2, 36) (3, 53) (4, 19) (인덱스번호, 인자값) 튜플로 반환
    
for x in enumerate(a):
    print(x[0], x[1]) # 0 23, 1 12, 2 36, 3 53, 4 19

# 이런 형식으로 가장 많이 사용함 enumerate
for index, value in enumerate(a):
    print(index, value) # 0 23, 1 12, 2 36, 3 53, 4 19

if all(60 > x for x in a): # all은 조건이 모두 참이어야 참
    print("YES")
else:
    print("NO")
    
if any(15 > x for x in a): # any은 조건이 하나라도 참이면 참
    print("YES")
else:
    print("NO")