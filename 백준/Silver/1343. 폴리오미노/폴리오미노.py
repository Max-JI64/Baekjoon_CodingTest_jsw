temp_list = list(input().split(".")) #나중에 ".".join으로 합치기

blocks=[] #AAAA와 BB의 조합을 저장, join으로 합칠것

is_can=True #가능하면
for bl in temp_list: #각 X블록들에 대하여 
	#홀수이면 안된다 -> 짝수이면 무조건 가능하다
	if len(bl) % 2 != 0:
		is_can=False
		break
	if len(bl)==0:
		blocks.append("") #빈공간이여도 join을 사용하기 위해 저장한다
		continue #continue가 없으면 아래 temp의 빈 문자열이 중복 추가된다
	
	num_AAAA = len(bl)//4 #AAAA의 최대 개수
	num_BB = (len(bl)%4)//2 #BB의 개수
	temp = "AAAA"*num_AAAA+"BB"*num_BB
	blocks.append(temp)
	
if is_can:
	result=".".join(blocks)
	print(result)
else:
	print(-1)
		
