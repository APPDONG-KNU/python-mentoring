X = int(input())
N = int(input())
add = 0
for _ in range(N):
    a, b = map(int,input().split())
    add = add + (a*b)
if add == X:
    print('Yes')
else:
    print('No')
