#w.a.p.t.p given number is armstrong number or not

n=153
dummy=n
summ=0
p=len(str(n))
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    summ+=rem**p
if n==summ:
    print(f'{n} is armstrong number')
else:
    print(f'{n} is not armstrong number')

'''
iteration
1.controller will take 153 and will check whether it is greater than 0 or not.it
  is greater than 0 so condition satisfies and for extraction of the last digit
  we are performing modular division with 10 and storing the value 3 in rem.after
  that we have to eleminate the extracted digit from the number so we are performing
  floor division with 10 and storing the value 15 in dummy.after that summ will
  be added with 3**p.p is the number of digits present in given number which is
  3**3
2.it will take 15 and check whether it is greater than 0 or not.it is greater than
  0 so condition satisfies and performing modular division  and we took 5 and stored
  in rem.performing floor division with 15 and 10 and eliminating 5 and 1 will be
  stored in dummy.summ will be added with 5**3 and stored the value in summ
3.it will take 1 and check whether it is greater than 0 or not.it is greater than
  0 so condition satisfies and performing modular division  and we took 1 and stored
  in rem.performing floor division with 1 and 10 and eliminating 1 and 0 will be
  stored in dummy.summ will be added with 1**3 and stored the value in summ
4.it will take 0 and check whether it is greater than 0 or not.it is not greater
  than 0 so condition does not satisfies and controller will come out of the loop
  and checking if n is equals to summ or not.if it is equals then printing n is
  armstrong number,else printing n is not armstrong number

'''



  