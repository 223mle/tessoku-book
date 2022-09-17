N, K = map(int, input().split())
A = list(map(int, input().split()))

#x秒後はK枚より多いかどうかを判定
def check(x, N, K, A):
    sum = 0
    for i in range(N):
        sum += x//A[i] 
    if sum>=K:
        return True
    else:
        return False

L = 1
R = 10**9
while L<R:
    M = (L+R)//2
    ans = check(M, N, K, A)
    if not ans:
        L = M+1
    if ans:
        R = M
#L==Rとなるためどちらでも良い
#Rの方が若干早かった
print(L)

