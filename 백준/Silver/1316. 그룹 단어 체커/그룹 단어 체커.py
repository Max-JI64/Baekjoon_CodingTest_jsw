N = int(input())
word_list=[]
for _ in range(N):
	temp = list(input())
	word_list.append(temp)

count=0
for word in word_list:
	check_dict = {}
	is_group=True #그룹 단어인지 여부
	for i in range(len(word)):
		char=word[i] #현재 문자
		
		if char in check_dict: #기록되어있으면
			if i>0 and word[i-1]!=char: 
				#이미 딕셔너리에 기록이 되어있음에도 이전 글자가 지금 글자와 다르다
				#딕셔너리 기록 : 이미 전에 나왔다
				#계속 같은 글자였으면 이 조건문을 건너 뛰었을 것
				#따라서 지금 글자는 이미 기록된 것 중 다시 반복하여 나온 글자이다
				is_group=False
				break #즉시 해당 문자에 대해 분석 종료
		else: #기록이 되어있지 않다면
			check_dict[char]=True
	
	if is_group: #True가 계속 유지되었다면
		count+=1
print(count)