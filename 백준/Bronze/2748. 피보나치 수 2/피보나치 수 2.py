num = int(input())

a = 0 #F_{n-2}
b = 1 #F_{n-1}
c = 0 #F_{n}

if num>=2: #아래의 식은 두번째 피보나치부터
	for _ in range(num-1):
		c = a+b
		a=b #n-2번은 과거의 n-1번
		b=c #n-1번은 과거의 n번
else:
	c=1 #첫번째 피보나치는 1이다

print(c)