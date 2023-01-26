'''
나누어 떨어지는 숫자 배열
'''
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    else:
        answer.sort()
        return answer
    
'''
휴대폰 번호 가리기
'''
def solution(phone_number):
    phone_number_len = len(phone_number)
    return ((phone_number_len - 4) * '*')+ phone_number[-4:]

'''
제일 작은 수 제거하기
'''
def solution(arr):
    if len(arr) == 1:
        return [-1]
    arr.remove(min(arr))
    return arr

'''
음양 더하기
'''
def solution(absolutes, signs):
    answer = []
    for i in range(len(absolutes)):
        if  signs[i]== True:
            answer.append(absolutes[i])
        else:
            answer.append(-absolutes[i])
    return sum(answer)

'''
없는 숫자 더하기
#1. 1 ~ 9까지의 리스트를 만든다
#2. 리스트와 number의 리스트를 비교하여 remove하여 없으면 제거
#3. number를 sum한다
'''
def solution(numbers):
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for n in numbers:
        number.remove(n)
    return sum(number)

'''
가운데 글자 가져오기
#1. 홀수이면 가운데 있는 거 가져옴  
#2. 짝수이면 가운데 있는거 두개 가져옴 
'''
def solution(s):
    if len(s) % 2 == 1:
        return s[len(s)//2]
    else:
        return s[len(s)//2 -1:len(s)//2 + 1]

'''
수박수박수박수박수박수?
'''
def solution(n):
    if n % 2 == 0:
        return '수박' * (n//2)
    else:
        return '수박' * (n//2) + '수'

'''
내적
'''
def solution(a, b):
    array = []
    for i in range(len(a)):
        array.append(a[i]*b[i])
    return sum(array)

'''
문자열 내림차순으로 배치하기
'''
def solution(s):
    s = list(s)
    s.sort(reverse=True)
    return ''.join(s)

'''
약수의 개수와 덧셈
#1. 약수의 개수 판단으로 그 개수가 짝수면 양수로 배출 홀수면 음수로 배출
#2. for돌려서 숫자를 더함
'''
def cal_divisor(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    if cnt % 2 == 0:
        return n 
    else:
        return -n

def solution(left, right):
    total = 0
    for i in range(left, right+1):
        total += cal_divisor(i)
    return total

'''
문자열 다루기 기본
#1. 문제를 잘 읽자 
-> 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성 
'''
def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            try: 
                if type(i) == str:
                    i = int(i)
            except:
                return False
        return True
    return False

'''
부족한 금액 계산하기
#1. price와 count를 순차적으로 곱하여 놀이기구의 이용금액구함
#2. money와 놀이기구의 이용금액을 뺀다
#3. 금액이 부족하지 않으면 0을 return
#4. 부족하다면 뺀 금액을 return
'''
def solution(price, money, count):
    total = 0
    for i in range(1, count+1):
        total += (price * i)
    if total < money:
        return 0
    return total - money
