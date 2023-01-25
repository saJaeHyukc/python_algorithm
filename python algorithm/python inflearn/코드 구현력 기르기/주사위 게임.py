'''
1. 상금을 받는 함수를 만든다 -> 
- 같은 눈 3개면 10000원 + (같은 눈) * 1000원
- 같은 눈 2개면 1000원 + (같은 눈) * 100원
- 전부 다른 눈 (가장 큰 수) * 100원
2. 가장 큰 수를 for문을 돌려 max값과 비교하여 출력
'''
def cal_reward(x):
    reward = 0
    if x[0] == x[1] == x[2]:
        reward = 10000 + (x[0] * 1000)
    elif x[0] == x[1] or x[0] == x[2]:
        reward = 1000 + (x[0] * 100)
    elif x[1] == x[2]:
        reward = 1000 + (x[1] * 100)
    else:
        reward = max(x) * 100
    return reward

n = int(input())
max_reward = 0
for i in range(1, n+1):
    n_list = list(map(int, input().split()))
    reward = cal_reward(n_list)
    if  reward > max_reward:
        max_reward = reward
print(max_reward)