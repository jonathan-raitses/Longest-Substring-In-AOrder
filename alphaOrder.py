__author__ = 'Jonathan Raitses'
school = 'Massachusetts Institute of Technology'
s = 'abcdefghijklmnopqrstuvwxyz'
tempAns = ''
ans = ''
for letter in range(len(s)):
    if s[letter-1] <= s[letter]:
        tempAns += s[letter]
        if len(ans) < len(tempAns):
            ans = tempAns
    else:
        tempAns = s[letter]
print('Longest substring in alphabetical order is: ' + ans)
