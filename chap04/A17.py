N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [None] * (N+1)
dp[1] = 0
dp[2] = A[0]

for i in range(3, N+1):
    dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])

ans = []
place = N
while True:
    ans.append(place)
    if place==1:
        break

    if dp[place-1]+A[place-2] == dp[place]:
        place-=1
    else:
        place -= 2
ans.reverse()
print(len(ans))
print(*ans, sep=' ')