N = int(input())
temp = []
for _ in range(N):
	temp.append(list(map(int, input().split())))

#도착/소요 시간 오름차순 정리
temp.sort(key=lambda x: x[0], reverse=False) #첫번째 인자 기준 오름차순
arrive_time = [x[0] for x in temp]
check_time = [x[1] for x in temp]

#첫번째 소의 검사가 끝난 시간
taken_time = arrive_time[0] + check_time[0]
for i in range(1, N):
	#각 소의 검사는 도착시간과 앞선 소의 검사가 끝난 시간 중 나중인 것부터 시작한다
	taken_time = max(taken_time,  arrive_time[i]) + check_time[i]
print(taken_time)