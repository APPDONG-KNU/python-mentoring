hashMap = {}
res = []

a = input()
keys = map(int, input().split())
for k in keys:
    hashMap[k] = 1

b = input()
resKeys = map(int, input().split())
for rk in resKeys:
    if rk in hashMap:
         res.append(hashMap[rk])
    else:
         res.append(0)

for r in res:
    print(r, end=" ")



''' 문제 설명 
    5 
    6 4 2 10 -10 
    8
10 9 -5 2 3 4 5 -10 

여기서 10이 윗 두번째 줄 값에 있다 -> 1로 표현 
4번째 줄 중 값이 2줄에 없다 -> 0 으로 표현'''
