N = int(input())
temp = []
for _ in range(N):
	temp.append(list(map(int, input().split())))

#도착/소요 시간 오름차순 정리
temp.sort(key=lambda x: x[0], reverse=False) #첫번째 인자 기준 오름차순
arrive_time = [x[0] for x in temp]
check_time = [x[1] for x in temp]

#각 소마다 현재까지 소요시간 실시간 집계
taken_time = 0
for i in range(N):
	if taken_time<arrive_time[i]: #만약 도착시간이 현재까지 소요시간보다 늦으면
		taken_time = arrive_time[i]+check_time[i]
	else: #현재 소요시간보다 도착시간이 빨랐다면
		taken_time += check_time[i]

print(taken_time)