#l=[11,2,44,66,77] o/p-['odd','even','even','even','odd']

l=[11,2,44,66,77]
ip=0
while ip<len(l):
    if l[ip]%2==0:
        l[ip]='even'
    else:
        l[ip]='odd'
    ip+=1
print(l)

'''
iteration
1.controller will take 0 and it will check l[0] is even or not.l[0] is not even
  so it will come to the else part and l[0] will be assign to 'odd'.incremation
  will happen and ip become 1
2.it will take 1 and it will check whether l[1] is even or not.l[1] is even so
  condition satisfies and l[1] will be assign to 'even'.incremation will happen and
  ip become 2
3.it will take 2 and it will check whether l[2] is even or not.l[2] is even so
  condition satisfies and l[2] will be assign to 'even'.incremation will happen and
  ip become 3
4.it will take 3 and it will check whether l[3] is even or not.l[3] is even so
  condition satisfies and l[3] will be assign to 'even'.incremation will happen and
  ip become 4
5.it will take 4 and it will check whether l[4] is even or not.l[4] is not even so
  it will come to the else part and l[4] will be assign to 'odd'.incremation will
  happen and ip become 5
6.it will take 5 but condition does not satisfies.so loop will break and controller
  will come out of the loop and printing l

'''


