N, Q = map(int, input().split())
A = list(map(int, input().split()))
L, R = [], []
for _ in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
sum_A = [A[0]]
for i in range(1, N):
    sum_A.append(sum_A[i-1]+A[i])

for i in range(Q):
    if L[i]==1:
        print(sum_A[R[i]-1])
        continue
    print(sum_A[R[i]-1]-sum_A[L[i]-2])