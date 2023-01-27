'''
피자 나눠 먹기 (1)
'''
def solution(n):
    answer = n // 7
    if n % 7 != 0:
        return answer + 1
    return answer

'''
피자 나눠 먹기 (2)
'''
def solution(n):
    for i in range(6, 606, 6):
        if i % n == 0:
            answer = i / 6
            break
    return answer

'''
피자 나눠 먹기 (3)
'''
def solution(slice, n):
    pizza = 1
    while (slice * pizza) < n:
        pizza += 1
    return pizza

'''
배열의 평균값
'''
def solution(numbers):
    avg = sum(numbers) / len(numbers)
    return avg