'''
조건문 if(분기, 중첩)
'''
#분기
x = 7
if x == 7: #같다 
    print("Lucky") 
    print("ㅋㅋ") 


x = 5
if x != 7: #같지 않다
    print("Lucky") 
    print("ㅋㅋ")
    
#중첩
x = 15
if x >= 10: #x가 10보다 같거나 크다
    if x % 2 == 1: #x가 2로 나눴을 때 몫이 1
        print("10이상의 홀수")

x = 7
if x > 0 and x < 10: #and로 교집합 가능
    print("10보다 작은 자연수")

x = 7
if 0 < x < 10: #C나 C++은 이게 불가능 파이썬의 장점
    print("10보다 작은 자연수")
    
#분기문
x = 10
if x > 0:
    print("양수")
else:
    print("음수")

x = 93
if x >= 90:
    print("A")
elif x >= 80:
    print("B")
elif x >= 70:
    print("C")
elif x >= 60:
    print("D")
else:
    print("F")