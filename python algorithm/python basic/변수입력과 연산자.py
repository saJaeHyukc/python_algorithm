'''
변수입력과 연산자
'''

a = input("숫자를 입력하세요 : ")
print(a)

a, b=input("숫자를 입력하세요: ").split() #띄워쓰기로 연속 입력가능
a=int(a)
b=int(b)
print(a+b)

a, b=map(int, input("숫자를 입력하세요: " ).split())