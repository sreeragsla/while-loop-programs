#w.ap.t.p the index positions of even digits present in even index positions

s=input()
ip=0
while ip<len(s):
    if s[ip] in '02468':
        print(ip)
    ip+=2
