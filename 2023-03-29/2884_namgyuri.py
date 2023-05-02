H, M = map(int , input().split())
if M>=45:
    print(H,M-45)
if H>=1 and M<45:
    print(H-1,M+15)
if H==0 and M<45:
    print(H+23,M+15)
