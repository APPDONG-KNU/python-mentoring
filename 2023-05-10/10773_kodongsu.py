k = int(input())
hop = []
Plus = 0
for i in range(k):
    a = int(input())
    if a == 0:
        hop.pop()
    else:
        hop.append(a)
for z in range(len(hop)):
    Plus = Plus + hop[z]
print(Plus)
