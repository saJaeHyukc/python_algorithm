'''
람다 함수
'''
def plus_one(x):
    return x + 1

print(plus_one(1))

plus_two = lambda x: x+2
print(plus_two(1)) # 3

a = [1, 2, 3]
print(list(map(plus_one, a))) #[2, 3, 4] map으로 함수명을 써서 적용시킬 수 있음 
print(list(map(lambda x: x+1, a))) #[2, 3, 4] map으로 람다함수를 써서 적용시킬 수 있음 