H, W, N = map(int, input().split())
A, B, C, D = [None]*N, [None]*N, [None]*N, [None]*N
for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())
X = [[0]*(W+2) for i in range(H+2)]
Z = [[0]*(W+2) for i in range(H+2)]

for t in range(N):
    X[A[t]][B[t]] += 1
    X[A[t]][D[t]+1] -= 1
    X[C[t]+1][B[t]] -= 1
    X[C[t]+1][D[t]+1] += 1

for h in range(1, H+1):
    for w in range(1, W+1):
        Z[h][w] = Z[h][w-1] + X[h][w]
for w in range(1, W+1):
    for h in range(1, H+1):
        Z[h][w] = Z[h-1][w] + Z[h][w]

for h in range(1, H+1):
    for w in range(1, W+1):
        if w>=2:
            print(' ', end='')
        print(Z[h][w], end='')
    print('')

