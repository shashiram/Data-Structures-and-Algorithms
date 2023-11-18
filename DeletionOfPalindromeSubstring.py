

# Given a string containing characters as integers only. We need to delete all characters of this string in a minimum number of steps wherein in one step we can delete the substring which is a palindrome. After deleting a substring remaining parts are concatenated. 

# Examples:

# Input : s = “2553432”
# Output : 2
# We can delete all character of above string in
# 2 steps, first deleting the substring s[3, 5] “343”  
# and then remaining string completely  s[0, 3] “2552”

# Input : s = “1234”
# Output : 4
# We can delete all character of above string in 4 
# steps only because each character need to be deleted 
# separately. No substring of length 2 is a palindrome 
# in above string.


given_str='character'

'carac'

sub_dic={}



def fun(i,j,p):
    node=str(i)+'_'+str(j)
    sub_dic[node]=p
    sub_str=given_str[i:j]
    sub_dic[sub_str]=node
    if isPalendrome(sub_str):
        return sub_str
    else:
        ch_1=fun(0,i+1,node)
        ch_2=fun(i+1,j,node)
        if(len(ch_1)<len(ch_2)):
            return ch_2
        else:
            return ch_1
    
def isPalendrome(sub_str):

    if len(sub_str)==1:
        return True
    else:
       if sub_str==sub_str[::-1]:
           return True
       else:
           False

final_str=fun(0,len(given_str),None)
print(final_str)












# def delete_fun():

#     count=0
#     temp_str=given_str
#     while len(temp_str)>0:
#             max_len_str=fun(0,len(temp_str),temp_str)
#             temp_str=temp_str.replace(max_len_str,'')
#             count+=1

#     return count




        



# print('delete required :'+ str(delete_fun()))





        






