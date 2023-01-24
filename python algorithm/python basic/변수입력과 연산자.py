'''
변수입력과 연산자
'''

a = input("숫자를 입력하세요 : ")
print(a)

a, b=input("숫자를 입력하세요: ").split() #띄워쓰기로 연속 입력가능
a=int(a)
b=int(b)
print(a+b)

a, b=map(int, input("숫자를 입력하세요: " ).split()) #map 함수로 int로 바꿔주고 띄워쓰기로 연속 입력가능
print(a+b) # 5 + 2 = 7
print(a-b) # 5 - 2 = 3
print(a*b) # 5 * 2 = 10
print(a/b) # 5 / 2 = 1.5
print(a//b) # 5 // 2 = 1.66666666667
print(a%b) # 5 % 2 = 2
print(a**b) # 5 ** 2 = 25

a=4.3
b=5
c=a+b
print(type(c)) # float 범위가 더 큰 것으로 나옴
print(c) # 9.3

