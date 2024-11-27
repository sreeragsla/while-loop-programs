#w.a.p.t check given number is harshad number or not

n=135
dummy=n
summ=0
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    summ+=rem
if n%summ==0:
    print(f'{n} is harshad number')
else:
    print(f'{n} is not harshad number')

'''
iteration
1.controller will take 135 and will check whether it is greater than 0 or not.it
  is greater than 0 so condition satisfies and for extraction of the last digit
  we are performing modular division with 10 and storing the value 5 in rem.after
  that we have to eleminate the extracted digit from the number so we are performing
  floor division with 10 and storing the value 13 in dummy.after that summ will
  be added with 5 and stored the value in summ
2.it will take 13 and check whether it is greater than 0 or not.it is greater than
  0 so condition satisfies and performing modular division  and we took 3 and stored
  in rem.performing floor division with 13 and 10 and eliminating 3 and 1 will be
  stored in dummy.summ will be added with 3 and stored the value in summ
3.it will take 1 and check whether it is greater than 0 or not.it is greater than
  0 so condition satisfies and performing modular division  and we took 1 and stored
  in rem.performing floor division with 1 and 10 and eliminating 1 and 0 will be
  stored in dummy.summ will be added with 1 and stored in summ
4.it will take 0 and check whether it is greater than 0 or not.it is not greater
  than 0 so condition does not satisfies and controller will come out of the loop
  and checking if n%summ is equals to 0 or not.if it is equal printing n is harshad
  number,else printing n is not harshad number

'''



