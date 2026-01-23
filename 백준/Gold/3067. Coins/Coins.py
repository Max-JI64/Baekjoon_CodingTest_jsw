T = int(input())
for _ in range(T):
	N = int(input())
	coins = list(map(int, input().split()))
	M = int(input())
	
	#동적 테이블 - n번째는 n원을 만드는 가짓수가 들어있음
	dp = [0]*(M+1) #0부터 M까지
	dp[0]=1 #0원을 만드는 방법은 1가지
	
	for coin in coins:
		for i in range(coin, M+1): #현재 코인부터 M원까지
			dp[i] += dp[i-coin]
			
	print(dp[M])
	
	
	