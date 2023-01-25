n = int(input())
n_list = list(map(int, input().split()))
total = 0
cnt = 0
for i in n_list:
    if i == 1:
        cnt += 1
        total += cnt
    else:
        cnt = 0
print(total)
