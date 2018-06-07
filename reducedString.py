'''Given a string consisting of letters, 'a', 'b' and 'c', we can perform the following operation:

Take any two adjacent distinct characters and replace them with the third character.
For example, if 'a' and 'b' are adjacent, they can replaced by 'c'.

Find the smallest string which we can obtain by applying this operation repeatedly'''

def dp(s):
    aCount,bCount,cCount=0,0,0
    l=len(s)
    if len(set(s))==1:
        print(l)
    else:
        for j in range(l):
            if s[j]=='a':
                aCount+=1
            elif s[j]=='b':
                bCount+=1
            else:
                cCount+=1
        if aCount%2==0 and bCount%2==0 and cCount%2==0:
            print('2')
        elif aCount&1 and bCount&1 and cCount&1:
            print('2')
        else:
            print('1')