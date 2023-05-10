total = int(input())
n = int(input())
mytotal = 0

for i in range(n):
    price, num = map(int,input().split())
    mytotal += (price * num)

if total == mytotal:
    print('Yes')
else:
    print('No')
