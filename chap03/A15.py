N = int(input())
A = list(map(int, input().split()))
s1 = [(A[i], i) for i in range(N)]
s1.sort()
num = 1
B = [(num, s1[0][1])]
for i in range(1, N):
    if s1[i][0]>s1[i-1][0]:
        num += 1
        B.append((num, s1[i][1]))
    elif s1[i][0]==s1[i-1][0]:
        B.append((num, s1[i][1]))
ans = [None]*N
for i in range(N):
    ans[B[i][1]] = B[i][0]
print(*ans)


"""
import bisect
N = int(input())
A =  list(map(int, input().split()))
T = list(set(A))
T.sort()

B = [None]*N
for i in range(N):
    B[i] = bisect.bisect_left(T, A[i])
    B[i] += 1
print(*B, sep=' ')

"""