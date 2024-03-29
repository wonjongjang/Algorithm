import sys
sys.stdin = open('input.txt')


N, K = map(int, input().split())
dp = [0]*(K+1)
for _ in range(N):
    w, k = map(int, input().split())
    for i in range(K, w-1, -1):
        dp[i] = max(dp[i], dp[i-w]+k)

print(dp[K])