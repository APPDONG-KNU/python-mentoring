baskets = []
num, changes = map(int, input().split())
for n in range(num+1):
    baskets.append(n)
for i in range(changes):
    b1, b2 = map(int, input().split())
    baskets[b1], baskets[b2] = baskets[b2], baskets[b1]
    # temp = baskets[b2]
    # baskets[b2] = baskets[b1]
    #baskets[b1] = temp
baskets.pop(0)
for b in baskets:
     print(b, end=" ")
