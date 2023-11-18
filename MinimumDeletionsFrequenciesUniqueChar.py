
""" 
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string.
For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Ex : 

        Input: s = "aaaaaaaaaa"
        Output: 0
        Explanation: s is already good.

        Input: s = "aaabbbcc" => [3,3,2]
        Output: 2
        Explanation: You can delete two 'b's resulting in the good string "aaabcc".
        Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

"""

import sys

s="aabb"

freqs={}
uniqueFreq={}

for char in s:
    if char in freqs:
        freqs[char]=freqs[char]+1
    else:
        freqs[char]=1
cn=0
for v in freqs.values():
 
    for i in range(v):

        if v in uniqueFreq:
            v=v-1
            cn=cn+1
        else:
            uniqueFreq[v]=1
            break

    







    






   




    



    






    

