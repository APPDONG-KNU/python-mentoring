total = int(input())
n = int(input())
myTotal = 0

for i in range(n):
    price, num = map(int, input().split())
    myTotal += (price * num)

if total == myTotal:
    print('Yes')
else:
    print('No')
