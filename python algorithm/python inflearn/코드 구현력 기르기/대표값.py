'''
1. n의 학생 수를 입력받는다
2. score_list라는 학생 점수들을 받는다
3. 평균을 구한다(소수점 첫째 자리)
4. 평균과 가까운 사람 한명을 구하여 차이를 구한다
5. 그 가까운 사람들 중 높은 숫자를 가진 사람들을 구하고 번호가 빠른 사람을 출력한다.
'''
n = int(input())
score_list = list(map(int, input().split()))
score_avg =  int((sum(score_list) / n) + 0.5)
a = float('inf')
for i, v in enumerate(score_list):
    tmp = abs(v - score_avg)
    if tmp < a:
        a = tmp
        score = v
        res = i+1
    elif tmp == a:
        if v > score:
            score = v
            res = i+1
            
print(score_avg, res)
'''새로 알게된 정보
1. 최솟값을 구하는 방법 (반드시 알고 있기!)
arr = [5, 3, 7, 9, 2]
arr_min = float('inf')
for i in range(len(arr)):
    if arr[i] < arr_min:
        arr_min = arr[i]
        
2. 최솟값을 구할 때 무한대 값 넣기
arr_min = float('inf') # 무한 대의 값을 넣을 수 있다

3. round는 round_half_even 방식을 택한다
a = 66.5
print(round(a)) # 67이 아닌 66이 나옴 왜냐하면 round_half_even 방식 때문에

그래서 round보다는 아래로 작성하는 것이 좋음 
a = 66.5
a = a + 0.5
a = int(a)
print(a) # 67
'''


