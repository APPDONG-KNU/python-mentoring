H, M = map(int , input().split())
if M >= 45:
    M = M - 45
    print("%d %d" % (H, M))
else:
    if H >0:
        H = H - 1
    else:
        H = 23
    M = M + 60 - 45
    print("%d %d" % (H, M))
