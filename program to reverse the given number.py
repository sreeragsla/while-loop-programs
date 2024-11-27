#w.a.p.t reverse the given number

n=int(input())
dummy=n
rev=0
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    rev=rev*10+rem
print(rev)


