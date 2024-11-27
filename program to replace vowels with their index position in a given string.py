#w.a.p.t replace all the vowels with their index positions

s=input()
v='aeiouAEIOU'
ip=0
new=''
while ip<len(s):
    if s[ip] in v:
        new+=str(ip)
    else:
        new+=s[ip]
    ip+=1
print(new)

