N = int(input())
fruits = list(map(int, input().split()))
fruits_list=[0]*(9+1) #현재 윈도우의 과일 종류별 개수
types=0 #과일 개수
count=0

#윈도우를 움직여서 과일 수를 카운팅할것임
left=0
for right in range(N):
	if fruits_list[fruits[right]]==0:
		types+=1
	fruits_list[fruits[right]]+=1

	#과일 종류가 3개 이상이라면
	while types>=3:
		fruits_list[fruits[left]]-=1 #개수를 줄인다
		if fruits_list[fruits[left]]==0: #해당 창에서 해당 과일의 종류가 사라질때까지
			types-=1
		left+=1 #창 왼쪽을 한칸 앞으로 이동시킨다

	count = max(count, right-left+1)

print(count)		
	
