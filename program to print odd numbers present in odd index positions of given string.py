#w.a.p.t.p odd numbers present in odd index positions

s=input()
ip=1
while ip<len(s):
    if s[ip] in '13579':
        print(s[ip])
    ip+=2

    
