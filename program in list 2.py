#L=[11,22,33,44,55,66] o/p-[22,11,44,33,66,55]

L=[11,22,33,44,55,66]
ip=0
while ip<len(L):
    L[ip],L[ip+1]=L[ip+1],L[ip]
    ip+=2
print(L)

'''
iteration
1.controller will take 0 and l[0] will assign to l[1] and l[1] will assign to l[0]
  after that incremation will happen and ip become 2
2.it will take 2 and l[2] will assign to l[3] and l[3] will assign to l[2] after
  that incremation will happen and ip become 4
3.it will take 4 and l[4] will assign to l[5] and l[5] will assign to l[4] after
  that incremation will happen and ip become 6
4.it will take 6 and condition will not satisfy 6 is not greater than 6.so controller
  will come out of the loop and printing l

'''





