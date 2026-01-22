Q = int(input()) #문제의 개수
M = [] #앞에 있는 인원
for _ in range(Q):
	M.append(int(input()))
	
for i in range(Q):
	bus_num = M[i]//50 #앞에서 지나간 버스 수
	total_m = 0 #6시부터 지금까지 총 소요시간(분)

	#먼저 첫차는 국제선에서 국내선으로 이동해야 함으로 오는거 4분 정차시간 2분을 더한다
	total_m+=6

	#앞에서 지나간 버스 수만큼 4+2+4+2 분을 더한다
	##국내선 정류장에서 "출발"하는 시간이니 정차시간도 더해야 한다
	while bus_num>0:
		total_m+=12
		bus_num-=1 #버스 하나가 지나감
	
	#오늘 안에 못타면 -1 출력
	##06:00부터 00:06(막차 국내선 도착)까지는 총 18*60+6분이다
	###막차도 오늘 안에 타는건가?
	if total_m>18*60+6:
		print(-1)
	else:
		HH = 6 + total_m//60
		if HH>=24: #24시간 형식
			HH=0
		MM = total_m%60
		print(f"{HH:02d}:{MM:02d}")