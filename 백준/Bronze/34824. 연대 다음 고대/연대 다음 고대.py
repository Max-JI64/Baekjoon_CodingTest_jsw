N = int(input())
temp = []
for _ in range(N):
	temp.append(input())

for i in range(N):
	if temp[i]=="yonsei":
		print("Yonsei Won!")
		break
	elif temp[i]=="korea":
		print("Yonsei Lost...")
		break






