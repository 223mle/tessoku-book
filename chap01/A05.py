N, K = map(int, input().split())
count = 0
for red in range(1, N+1):
    for blue in range(1, N+1):
        if 1<=K-red-blue<=N:
            count += 1
print(count)