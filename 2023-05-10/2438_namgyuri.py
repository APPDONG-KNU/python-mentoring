n = int(input())
'''
for i in range(n):
    print('*'*(i+1))
'''
for i in range(n):
    for j in range(i+1):
        print('*', end="")
    print()
