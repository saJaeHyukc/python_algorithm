'''
1. 나머지 구하기
'''
def solution(num1, num2):
    return num1 % num2

'''
2. 중앙값 구하기
'''
def solution(array):
    array.sort()
    return array[len(array) // 2]

'''
3. 최빈값 구하기
생각
#1. 최빈값을 담은 딕셔너리를 구함
#2. 딕셔너리의 벨류 값 중 최댓값과 같은 것만 따로 리스트를 만들어 담음
#3. 리스트 요소가 1개일 때 그 리스트 요소 반환, 아닐 때 -1 반환
'''
def solution(array):
    count = {}
    for i in array:
        try:
            count[i] += 1
        except:
            count[i] = 1     
    
    modes = []
    for k, v in count.items():
        if v == max(count.values()):
            modes.append(k)
    if len(modes) == 1:
        return modes[0]
    else:
        return -1
    
''''
4. 짝수는 싫어요
'''
def solution(n):
    array = []
    for i in range(1, n+1):
        if i % 2 == 1:
            array.append(i)
    return array