s='Alok Mishra'
s=s.lower();
s1='abcdefghijklmnopqrstuvwxyz'
for char in s1:
    if char not in s:
        k=1
        break;
    k=0

if k ==0:
    print('pangram')
else:
 print('not pangram')
