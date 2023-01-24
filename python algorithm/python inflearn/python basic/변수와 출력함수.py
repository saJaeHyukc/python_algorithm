"""
1) 영문과 숫자, _로 이루어진다
2) 대소문자를 구분한다
3) 문자나, _로 시작한다
4) 특수문자를 사용하면 안된다. (&, % 등)
5) 키워드를 사용하면 안된다.
"""
a=1
A=2
c=3
A1=3
# 2b=4 (error)
_b=5
print(a, A, c, A1, _b) #1, 2, 3, 3, 5

a, b, c = 3, 2, 1
print(a, b, c) #3, 2, 1

# 값 교환
a, b=10, 20
print(a, b) #10, 20
a, b = b, a
print(a, b) #20, 10

# 변수 타입(메모리가 허용하는 만큼 할당가능)
a = 12345
print(type(a)) #int 

a = 12.123456789123457
print(a) #8바이트 이상은 안나옴 
print(type(a)) #float

a="student"
print(a) #student 
print(type(a)) #string

# 출력방식
print("number") # number
a, b, c = 1, 2, 3
print(a, b, c) #1 2 3
print("number: ", a, b, c) # number : 1 2 3
print(a, b, c, sep=', ') #1, 2, 3
print(a, b, c, sep=',') #1,2,3
print(a, end=' ') # a \n
print(b, end=' ') # b \n

