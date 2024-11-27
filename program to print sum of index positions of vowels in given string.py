#w.a.p.t.p sum of index positions of all the vowels present in given string using while loop

s=input()
summ=0
ip=0
v='aeiouAEIOU'
while ip<len(s):
    if s[ip] in v:
        summ+=ip
    ip+=1
print(summ)


    
