#w.a.p.t reverse a given string without using slicing

s=input()
rev=''
ip=0
while ip<len(s):
    rev=s[ip]+rev
    ip+=1
print(rev)

