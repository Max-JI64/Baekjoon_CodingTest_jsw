T = int(input())
	
dp=[0]*12
#가능한 경우의 수 미리 지정
dp[1]=1
dp[2]=2
dp[3]=4
	
#경우의 수를 모두 더한다
##경우의 수는 순열이다
###각각의 순열 마지막에 1,2,3 중 하나를 더하면 각각 서로 다른 경우의 가짓수이다
for i in range(4, 12):
	dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
	
for _ in range(T):
	N = int(input())
	print(dp[N])