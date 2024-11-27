#w.a.p.t.p all the index positions where 'eE' is present in a given string

s='sreerag'
ip=0
while ip<len(s):
    if s[ip] in 'eE':
        print(ip)
    ip+=1

'''
iteration
1.controller will take 0 and check whether it is lesser than len(s).0 is lesser
  than 7 so condition satisfies.it will check whether s[0] is present in 'eE'.it
  is not present so condition does not satisfies and incremation will happen and
  ip will become 1
2.it will take 1 and check whether it is lesser than len(s).1 is lesser than
  7 so condition satisfies.it will check whether s[1] is present in 'eE'.it is
  not present so condition does not satisfies and incremation will happen and ip
  will become 2
3.it will take 2 and check whether it is lesser than len(s).2 is lesser than
  7 so condition satisfies.it will check whether s[2] is present in 'eE'.it is
  present so condition satisfies and printing 2 and incremation will happen and
  ip will become 3
4.it will take 3 and check whether it is lesser than len(s).3 is lesser than
  7 so condition satisfies.it will check whether s[3] is present in 'eE'.it is
  present so condition satisfies and printing 2 and incremation will happen and
  ip will become 4
5.it will take 4 and check whether it is lesser than len(s).4 is lesser than
  7 so condition satisfies.it will check whether s[4] is present in 'eE'.it is
  not present so condition does not satisfies and incremation will happen and ip
  will become 5
6.it will take 5 and check whether it is lesser than len(s).5 is lesser than
  7 so condition satisfies.it will check whether s[5] is present in 'eE'.it is
  not present so condition does not satisfies and incremation will happen and ip
  will become 6
7.it will take 6 and check whether it is lesser than len(s).6 is lesser than
  7 so condition satisfies.it will check whether s[6] is present in 'eE'.it is
  not present so condition does not satisfies and incremation will happen and ip
  will become 7
8.it will take 7 and check whether it is lesser than len(s).7 is not lesser than
  7 so condition does not satisfies and controller will come out of the loop

'''


