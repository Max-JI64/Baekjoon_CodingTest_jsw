X = int(input())

def solve(x):
	a = int(str(x)[:2])
	b = int(str(x)[2:])
	if (a+b)**2 == x:
		return x
	else:
		return -1

i = X+1
found = False
# 9999까지만 탐색
while i <= 9999:
    result = solve(i)
    if result != -1:
        print(result)
        found = True
        break # 첫 번째 일치하는 수를 찾으면 종료
    i += 1

if not found:
    print(-1)
