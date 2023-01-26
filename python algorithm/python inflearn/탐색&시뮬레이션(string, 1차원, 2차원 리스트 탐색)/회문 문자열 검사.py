'''
1. 입력받은 문자를 전부 소문자로 바꾼다.
2. for문 해당 길이의 반만 돌려 앞의 문자열과 뒤의 문자열이 같은지 비교
3. 같지 않다면 no 같으면 yes
'''
def palindrome(i, a):
    # 소문자로 바꿈
    a = list(a.lower()) 
    
    # for문을 돌려 앞뒤 문자 비교하여 값 return
    for j in range(len(a)//2):
        if a[j] != a[-1-j]:
            return print(f'#{i} NO')
    return print(f'#{i} YES')
    
n = int(input())
for i in range(1, n+1):
    a = input()
    palindrome(i, a)
    
''' 모범답안
#1
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size // 2):
        if s[j] != s[-1-j]:
            print(f'#{i+1} NO')
            break
    else:
        print(f'#{i+1} YES')

#2 array[::-1] -> reverse된 결과값을 반환함
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print(f'#{i+1} YES')
    else:
        print(f'#{i+1} NO')
'''