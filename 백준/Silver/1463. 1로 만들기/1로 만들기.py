N = int(input())

# 최소 연산 횟수
dp = [0]*(N+1)

for i in range(2, N+1):
    #1. 1을 빼기
    dp[i] = dp[i-1]+1 #횟수니깐 1을 더한다
    
    #2. 2로 나누기
    if i%2==0:
        dp[i]=min(dp[i], dp[i//2]+1) #1을 뺀것과 비교
    
    #3. 3으로 나누기
    if i%3==0:
        dp[i]=min(dp[i], dp[i//3]+1) #1을 뺀것과 2로 나눈것을 비교

print(dp[N])