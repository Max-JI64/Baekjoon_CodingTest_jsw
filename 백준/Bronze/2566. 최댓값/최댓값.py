import sys

mat = []
while True:
	try:
		line = sys.stdin.readline() #값이 있는지 확인
		if not line:
			break #종료
		
		#값이 있으면
		row = map(int, line.split())
		mat.append(list(row))
		
	except Exception as e:
		break

N = len(mat) #row
M = len(mat[0]) #column

max_num = -1 #최대값
mi, mj = -1, -1 #최대값 좌표
for i in range(N):
	for j in range(M):
		if max_num<mat[i][j]:
			max_num = mat[i][j]
			mi, mj = i, j

#출력
print(max_num)
print(" ".join([str(mi+1), str(mj+1)]))