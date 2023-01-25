'''
1. 두 수의 나눗셈
'''
def solution(num1, num2):
    return int((num1 / num2) * 1000)

'''
2. 숫자 비교하기
'''
def solution(num1, num2):
    if num1 == num2:
        return 1
    else:
        return -1
    
'''
3. 분수의 덧셈
생각
1. 분수를 더한다.
2. 최대공약수를 구한다.
3. 최대공약수로 나눈다
4. 리스트로 출력한다.
'''

def solution(numer1, denom1, numer2, denom2):
    numer = (numer1 * denom2) + (numer2 * denom1) 
    denom = denom1 * denom2
    for i in range(1, numer + 1):
        if (numer % i == 0) & (denom % i ==0):
            gcd = i
    numer = int(numer // gcd)
    denom = int(denom // gcd) 
    return [numer, denom]

'''
4. 배열 두배 만들기
'''
def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(n * 2)
    return answer