time=int(input())

def factorial(n):
    temp=1
    for i in range(1, n+1):
        temp *= i # 1, 2, ..., n
    return temp

for _ in range(time):
    n, m = map(int, input().split())
    result=factorial(m)//(factorial(n)*factorial(m-n))
    print(result)