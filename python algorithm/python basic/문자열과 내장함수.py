'''
문자열과 내장함수
'''

msg = "It is Time"
print(msg.upper()) # IT IS TIME, upper 대문자로 바꿈
print(msg.lower()) # it is time, lower 소문자로 바꿈

tmp = msg.upper() #IT IS TIME 
print(tmp.find('T')) # 1, find 인덱스 번호를 순차적으로 찾아 내줌
print(tmp.count('T')) # 2, count 문자열이 몇개있는지 알려줌

print(msg)
print(msg[:2]) # It, slicing 0번부터 1번까지 뽑아줌
print(msg[3:5]) # is, slicing 3번부터 4번까지 뽑아줌
print(len(msg)) # 10 , len 길이를 구해줌

for i in range(len(msg)):
    print(msg[i], end=' ') # I t  i s  T i m e
    
for x in msg:
    print(x, end=' ')# I t  i s  T i m e
    
for x in msg:
    if x.isupper(): #isupper, x가 대문자이면 True 
        print(x, end=' ') # I T

for x in msg:
    if x.islower(): # islower, x가 소문자이면 True
        print(x, end=' ') # t i s i m e
        
for x in msg:
    if x.isalpha(): #isalpha, 알파벳일 때 True
        print(x, end=' ')
        
tmp = 'AZ'
for x in tmp:
    print(ord(x)) #65 90, ord 아스키넘버를 출력해줌
    
tmp = 'az'
for x in tmp:
    print(ord(x)) # 97 122
    
tmp=65
print(chr(tmp)) #A, chr 아스키넘버에 맞는 문자열을 출력해줌