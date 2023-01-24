'''
반복문(for, while)
'''

# for문
a = range(1, 11)
print(list(a)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(10):
    print("hello") #hello 10번 반복
    
for i in range(1, 11):
    print(i) #1,2,3,4,5,6,7,8,9,10

for i in range(10, 0, -1):
    print(i) # 10,9,8,7,6,5,4,3,2,1
    
# while문
i = 1
while i <= 10:
    print(i) # 1,2,3,4,5,6,7,8,9,10
    i = i+1

# break
i = 1
while True:
    print(i) #무한 반복
    if i == 10:
        break # i가 10일 때 반복문 멈춤
    i += 1 # 축약 연산자

# continue
for i in range(1, 11):
    if i % 2 == 0:
        continue # continue 하면 해당 아래의 for 문 다음으로 넘어가버림
    print(i) # 1 3 5 7 9
    

for i in range(1, 11):
    print(i)
    if i > 15:
        break
else:
    print(11)

    
