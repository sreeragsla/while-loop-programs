#w.a.p.t.p the elements which are in even index positions of a given string

s='sreerag'
ip=0
while ip<len(s):
    print(s[ip])
    ip+=2

'''
iteration
1.controller will take 0 and check whether it is lesser than len(s).it is lesser
  than len(s) so condition satisfies and printing s[0] and incremation will happen
  and ip will become 2
2.it will take 2 and and check whether it is lesser than len(s).it is lesser than
  len(s) so condition satisfies and printing s[2] and incremation will happen and
  ip will become 4
3.it will take 4 and and check whether it is lesser than len(s).it is lesser than
  len(s) so condition satisfies and printing s[4] and incremation will happen and
  ip will become 6
4.it will take 6 and and check whether it is lesser than len(s).it is lesser than
  len(s) so condition satisfies and printing s[6] and incremation will happen and
  ip will become 8
5.it will take 8 and check whether it is lesser than len(s).it is not lesser than
  len(s) so condition does not satisfies and controller will come out of the loop

'''

