#w.a.p.t.find the sum of individual digits of a given number

n=135
summ=0
while n>0:
    rem=n%10
    n=n//10
    summ+=rem
print(summ)


'''
iteration
1.controller will take 135 and will check whether it is greater than 0 or not.it
  is greater than 0 so condition satisfies and for extraction of the last digit
  we are performing modular division with 10 and storing the value 5 in rem.after
  that we have to eleminate the extracted digit from the number so we are performing
  floor division with 10 and storing the value 13 in n.summ will be added with rem
  and added value will be stored in summ
2.it will take 13 and check whether it is greater than 0 or not.it is greater than
  0 so condition satisfies and performing modular division  and we took 3 and stored
  in rem.performing floor division with 13 and 10 and eliminating 3 and 1 will be
  stored in n.summ will be added with rem and added value will be stored in summ
3.it will take 1 and check whether it is greater than 0 or not.it is greater than
  0 so condition satisfies and performing modular division  and we took 1 and stored
  in rem.performing floor division with 1 and 10 and eliminating 1 and 0 will be
  stored in n.summ will be added with rem and added value will be stored in summ
4.it will take 0 and check whether it is greater than 0 or not.it is not greater
  than 0 so condition does not satisfies and controller will come out of the loop
  and printing summ

'''

