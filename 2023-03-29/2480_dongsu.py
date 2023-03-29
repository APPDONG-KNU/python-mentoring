x, y, z = map(int, input().split())
if x == y == z:
    print(10000 + x * 1000)
elif x == y or x == z:
    print(1000 + x * 100)
elif z == y:
    print(1000 + z * 100)
else:
    a = [x, y, z]
    a.sort()
    b = int(a[2])
    print(b * 100)
