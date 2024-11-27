#l=[11,22,33,44,-1,66,50] o/p-['odd','even','odd','even',-1,'even','even']

l=[11,22,33,44,-1,66,50]
ip=0
while ip<len(l):
    if l[ip]>0:
        if l[ip]%2==0:
            l[ip]='even'
        else:
            l[ip]='odd'
    ip+=1
print(l)

'''
iteration
1.controller will take 0 and check whether l[0] is greater than 0 or not.l[0] is
  greater than 0 so condition satisfies and it will check if it is even or not.l[0]
  is not even so controller will come to the else part and l[0] will assign to
  'odd'.after that incremation will happen and ip will become 1
2.it will take 1 and check whether l[1] is greater than 0 or not.l[1] is greater
  than 0 so condition satisfies and it will check if it is even or not.l[1] is even
  so condition satisfies and l[1] will be assign to 'even' and incremation will
  happen and ip will become 2
3.it will take 2 and check whether l[2] is greater than 0 or not.l[2] is greater
  than 0 so condition satisfies and it will check if it is even or not.l[2] is not
  even so controller will come to the else part and l[2] will assign 'odd' and
  incremation will happen and ip will become 3
4.it will take 3 and check whether l[3] is greater than 0 or not.l[3] is greater
  than 0 so condition satisfies and it will check if it is even or not.l[3] is even
  so condition satisfies and l[3] will be assign to 'even' and incremation will
  happen and ip will become 4
5.it will take 4 and check whether l[4] is greater than 0 or not.l[4] is not greater
  than 0 so condition does not satisfies.incremation will happen and ip will become
  5
6.it will take 5 and check whether l[5] is greater than 0 or not.l[5] is greater
  than 0 so condition satisfies and it will check if it is even or not.l[5] is even
  so condition satisfies and l[5] will be assign to 'even' and incremation will
  happen and ip will become 6
7.it will take 6 and check whether l[6] is greater than 0 or not.l[6] is greater
  than 0 so condition satisfies and it will check if it is even or not.l[6] is even
  so condition satisfies and l[6] will be assign to 'even' and incremation will
  happen and ip will become 7
8.it will take 7 and 7 is not greater than 7 so condition does not satisfies and
  controller will come out of the loop and printing l

'''



