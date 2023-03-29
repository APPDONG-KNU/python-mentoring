a= int(input())
b= int(input())
one = b%10*a
ten = b%100//10*a
hun = b//100*a
print(one)
print(ten)
print(hun)
print(one+ten*10+hun*100)
