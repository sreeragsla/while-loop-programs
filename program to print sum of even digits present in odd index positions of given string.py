#find the sum of even digits present in odd index position

s=input()
summ=0
ip=1
while ip<len(s):
    if s[ip] in '02468':
        summ+=int(s[ip])
    ip+=2
print(summ)


        
