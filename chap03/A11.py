N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

def binary_search(x, A):
    L = 0
    R = N-1
    while L<=R:
        M = (L+R)//2
        if x<A[M]:
            R = M-1
        elif x==A[M]:
            return M
        else:
            L = M+1
    return -1
ans = binary_search(X, A)
print(ans+1)

"""
こっちの方が遅かった
import bisect
N, X = map(int, input().split())
A = list(map(int, input().split()))
print(bisect.bisect_left(A, X) + 1)
"""