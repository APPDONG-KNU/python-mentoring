a=int(input())
b=int(input())
one = (b%10)*a
ten = (((b%100)//10)*a)
hundred = ((b//100)*a)
print(one)
print(ten)
print(hundred)
print(one+ten*10+hundred*100)
