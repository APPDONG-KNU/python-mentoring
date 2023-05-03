total = int(input())
n = int(input())
res = 0

for i in range(n):
    price, num = map(int, input().split())
    res += price*num

if total == res:
    print("Yes")
else:
    print("No")
