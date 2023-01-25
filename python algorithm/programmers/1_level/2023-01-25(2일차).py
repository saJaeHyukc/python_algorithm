'''
평균 구하기
'''
def solution(arr):
    answer = sum(arr)/ len(arr)
    return answer

'''
짝수와 홀수
'''
def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
'''
자릿수 더하기
'''
def solution(n):
    n_list = list(map(int, str(n)))
    return sum(n_list)

'''
자연수 뒤집어 배열로 만들기
'''
def solution(n):
    n_list = list(map(int, str(n)))
    n_list.reverse()
    return n_list

'''
정수 제곱근 판별
생각
#1. 제곱근을 구한다. 0.5를 곱하면 된다 루트를 생각하면 편하다
#2. 맞으면 제곱근에서 1을 더해 제곱하여 리턴 아니면 -1
'''
def solution(n):
    num = int(n ** 0.5)
    if n == num ** 2:
        return int((num + 1) ** 2)
    else:
        return -1

'''
문자열 내 p와 y의 개수
'''
def solution(s):
    s = list(s.lower())
    if s.count("p") == s.count("y"):
        return True
    else:
        return False

'''
x만큼 간격이 있는 n개의 숫자
'''
def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer

'''
문자열을 정수로 바꾸기
'''
def solution(s):
    return int(s)

'''
정수 내림차순으로 배치하기
'''
def solution(n):
    n_list = list(map(int, str(n)))
    n_list.sort(reverse=True)
    n_list = list(map(str, n_list))
    return int("".join(n_list))

'''
하사드 수
'''
def solution(x):
    x_list = list(map(int, str(x)))
    if  x % sum(x_list) == 0:
        return True
    else:
        return False

'''
나머지가 1이 되는 수 찾기
'''
def solution(n):
    for i in range(1, n):
        if n % i == 1:    
            return i