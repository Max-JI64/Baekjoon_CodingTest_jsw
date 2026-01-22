N = int(input())
dasom = int(input())
temp=[]
for _ in range(N-1):
	temp.append(int(input())) #다른 후보 리스트


if N-1 == 0: #후보가 다솜이 혼자라면
	print(0)
else:
	count = 0 #총 매수자
	while True:
		max_candidate = max(temp) #제일 많은 득표수
		max_idx = temp.index(max_candidate) #제일 많은 득표자의 인덱스
		
		if dasom > max_candidate: #제일 높을 떄
			break
		
		temp[max_idx]-=1
		dasom+=1
		count+=1
	
	print(count)
		