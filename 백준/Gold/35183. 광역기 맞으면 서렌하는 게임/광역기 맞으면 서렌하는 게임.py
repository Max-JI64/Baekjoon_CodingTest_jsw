N = int(input())
patterns = []
for _ in range(N):
	patterns.append(list(map(int, input().split())))

def check(n, patterns, skip_idx):
	"""
	n = 총 시간, N
	patterns = N초간의 패턴, L_i, R_i
	skip_idx = 광역기를 한번 스킵하는 초

	a, b = 현재 i초에 존재할 수 있는 범위
	매 초마다 범위를 1씩 늘릴 것임
	그리고 현재 패턴의 L_i, R_i와의 교집합을 새로운 존재 범위로 삼을것임
	이떄 한번 보호막을 사용한다면(skip_idx), 그때는 범위를 1씩 늘리기만 할 뿐 교집합 계산은 안할것임
	"""
	#만약 한개의 패턴만 있을 경우
	#모조건 통과한다
	if n == 1: 
		return True

	#초기 시작지점
	#만약 첫번째 패턴에 보호막을 사용한다면 초기 시작지점은 두번째 패턴의 위치가 되어야함
	if skip_idx==0:
		a, b = patterns[1][0], patterns[1][1]
	#초기 시작지점은 첫번째 패턴의 범위인게 가장 좋다
	else:
		a, b = patterns[0][0], patterns[0][1]
	
	for i in range(N):
		#범위 늘리기
		a-=1
		b+=1

		#교집합 구하기
		#skip_idx인 경우는 제외하고
		if i != skip_idx:
			a = max(a, patterns[i][0])
			b = min(b, patterns[i][1])
		
		#교집합이 없다면 실패
		if a>b:
			return False
	#한번도 교집합이 없었던 적이 없다면 성공
	return True

champion = False #통과가 되었나 플래그
for skip_idx in range(-1, N):
	if check(N, patterns, skip_idx):
		champion = True

if champion == True:
	print("World Champion")
else:
	print("Surrender")