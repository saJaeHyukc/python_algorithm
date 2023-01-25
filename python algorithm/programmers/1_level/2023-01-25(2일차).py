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
        
'''
두 정수 사이의 합
'''
def solution(a, b):
    total = 0
    if a < b:
        for i in range(a, b+1):
            total += i
    else: 
        for i in range(b, a+1):
            total += i
    return total

'''
콜라츠 추측
생각
#1. 입력된 수가 짝수면 2로 나눈다
#2. 입력된 수가 홀수면 3을 곱하고 1을 더한다
#3. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복
#4. 500번이 넘어가면 -1을 반환
'''
def solution(num):
    cnt = 0
    while num > 1:
        if num % 2 == 0:
            num = num // 2
            cnt += 1
        elif num % 2 == 1:
            num = (num * 3) + 1
            cnt += 1
        
        if  cnt > 500:
            return -1
    return cnt

print(solution(6))
print(solution(16))
print(solution(626331))
