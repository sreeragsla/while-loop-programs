#w.a.p.t.p the index positions of vowels in a given string

s=input()
v='aeiouAEIOU'
ip=0
while ip<len(s):
    if s[ip] in v:
        print(ip)
    ip+=1
