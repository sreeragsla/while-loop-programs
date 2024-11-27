#w.a.p.t.check given number is perfect or not by using while loop

n=6
ds=0
i=1
while i<n//2+1:
    if n%i==0:
        ds+=i
    i+=1
if n==ds:
    print(f'{n} is perfect number')
else:
    print(f'{n} is not perfect number')


'''
iteration
1.controller will take 1 and check whether 1 is lesser than 4.it is lesser than 4 so
  6%1 will give 0 or not.6%1 will give 0 so condition satisfies and ds will
  be added with 1 and store the added value in ds.incemation will happen and
  ip will be 2
2.it will take 2 and check whether 2 is lesse than 4.it is lesser then 4 so
  6%2 will give 0 or not.6%2 will give 0 so condition satisfies and ds will be added
  with 2 and store the added value in ds.incemation will happen and ip will be 3
3.it will take 3 and check whether 6%3 will give 0 or not.6%3 will give 0 so condition
  satisfies and ds will be added with 3 and store the added value in ds.incemation will
  happen and ip will be 4
4.it will take 4 and check whether 4 is lesser than 4.it is not lesser than 4 so
  condition does not satisfies and controller will come out of the loop and checking
  if n is equals to ds or not.if it is equal printing n is perfect number,else
  printing n is not perfect number


'''


