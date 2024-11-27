#w.a.p.t.p odd digits present in even index positions in a given string

s=input()
ip=0
while ip<len(s):
    if s[ip] in '13579':
        print(s[ip])
    ip+=2
