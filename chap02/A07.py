D = int(input())
N = int(input())
L, R = [None]*N, [None]*N

for i in range(N):
    L[i], R[i] = map(int, input().split())
B = [0]*(D+2)
for i in range(N):
    B[L[i]] += 1
    B[R[i]+1] -= 1
ans = [None] * (D+2)
ans[0] = 0
for d in range(1, D+1):
    ans[d] = ans[d-1]+B[d]
for d in range(1, D+1):
    print(ans[d])


"""
review

D = int(input())
N = int(input())
L, R = [], []
for i in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
people = [0]*D
for i in range(N):
    people[L[i]-1] += 1
    if R[i]==D: continue
    people[R[i]] -= 1

ans = 0
for i in range(D):
    ans += people[i]
    print(ans)


"""