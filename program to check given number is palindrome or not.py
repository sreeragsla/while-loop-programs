#w.a.p.t.p given number is palindrome or not

n=202
dummy=n
rev=0
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    rev=rev*10+rem
if n==rev:
    print(f'{n} is a palindrome')
else:
    print(f'{n} is not palindrome')

'''
iteration
1.controller will take 202 and checking whether it is greater than 0 or not.it is
  greater than 0 so condition satisfies and for extracting last digit we are performing
  202 modular division with 10 and 2 will be stored in rem.for eliminating the extracted
  element we are performing 202 floor division with 10 and eliminating 2 and 20 will
  be stored in dummy.to reverse the number we are using rev will be assign to rev*10+rem.
  here 0*10+2 and value will be stored in rev
2.it will take 20 and checking whether it is greater than 0 or not.it is greater than 0
  so condition satisfies and for extracting last digit we are performing 20 modular
  division with 10 and 0 will be stored in rem.for eliminating the extracted element
  we are performing 20 floor division with 10 and eliminating 0 and 2 will be stored
  in dummy.to reverse the number we are using rev will be assign to rev*10+rem.here
  2*10+0 and value will be stored in rev
3.it will take 2 and checking whether it is greater than 0 or not.it is greater than 0
  so condition satisfies and for extracting last digit we are performing 2 modular
  division with 10 and 2 will be stored in rem.for eliminating the extracted element
  we are performing 2 floor division with 10 and eliminating 2 and 0 will be stored
  in dummy.to reverse the number we are using rev will be assign to rev*10+rem.here
  20*10+2 and value will be stored in rev
4.it will take 0 and check whether it is greater than 0 or not.it is not greater
  than 0 so condition does not satisfies and controller will come out of the loop
  and checking if n is equals to rev or not.if it is equals then printing n is
  palindrome,else printing n is not palindrome

'''


