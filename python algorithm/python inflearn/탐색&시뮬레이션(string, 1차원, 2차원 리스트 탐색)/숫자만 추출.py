'''
1. 문자와 숫자가 섞여있어 숫자만 골라내고 정수로 바꾼다.
2. 그 정수로 바꾼 것을 약수의 개수를 구한다.
3. 정수와 약수의 개수를 return 한다.
'''
def set_number(n):
    number = []
    for i in n:
        try: 
            if i == str(i):
                number.append(str(int(i)))
        except:
            pass
    return int(''.join(number))

def count_divisor(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return cnt

n = input()
number = set_number(n)
print(number)
print(count_divisor(number))

'''모범답안
s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x) #중요중요중요중요중요
print(res)

cnt = 0
for i in range(1, res+1):
    if rest % i == 0:
        cnt += 1
print(cnt)
        
'''