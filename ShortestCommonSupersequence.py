
# Given two strings str1 and str2, the task is to find the length of the shortest string that has both str1 and str2 as subsequences.

# Input:   str1 = "geek",  str2 = "eke"
# Output: 5
# Explanation: 
# String "geeke" has both string "geek" 
# and "eke" as subsequences.

# Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
# Output:  9
# Explanation: 
# String "AGXGTXAYB" has both string 
# "AGGTAB" and "GXTXAYB" as subsequences.

str1='geek'
str2='eke'


final_str={}

def fun(i,j):
    if i< len(str1) and j< len(str2):
    
        if str1[i]==str2[j]:
            return str1[i]+fun(i+1,j+1)
        else:
            ch_1=fun(i,j+1)
            ch_2=fun(i+1,j)

            f_char=''

            if (len(ch_1)<len(ch_2)):
                f_char=str1[j]+ch_1
            else:
                f_char=str2[i]+ch_2


            return  f_char 
    else:
        if i<len(str1):
            return str1[i]+fun(i+1,j)
        elif j<len(str2):
            return str2[j]+fun(i,j+1)
        else:
            return ''
        
def setParent(node, parent):
    final_str[node]=parent
        
print(fun(0,0))







    











