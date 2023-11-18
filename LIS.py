
# find longest increasing sub(alphabatically) sequnce of a given string 

import sys

given_str="aviram"

n=len(given_str)

subSeq=''


def lis (i):
    print(i)
    sub_seq_temp=given_str[i]
    if i== (n-1):
        return sub_seq_temp
    else:
        j=i+1
        while  j< n:
            if given_str[i]<given_str[j]:
                retuned_str =given_str[i]+lis(j)

                if len(sub_seq_temp)<len(retuned_str):
                    sub_seq_temp=retuned_str
            j+=1
        return sub_seq_temp

i=n-1


while i>=0:
    sub_seq_temp=lis(i)
    
    if len(subSeq)<len(sub_seq_temp):
        subSeq=sub_seq_temp
    i=i-1

print(subSeq)

# def lis (i):

#     dic={0:1,1:given_str[i]}
#     if i== (n-1):
#         return dic
#     else:

#         j=i+1
#         while  j< n:
#             if given_str[i]<given_str[j]:

#                 temp_dic={}
#                 retuned=lis(j)

#                 temp_dic[0] =1+ retuned[0]
#                 temp_dic[1] =given_str[i]+retuned[1]

#                 if dic[0]<temp_dic[0]:
#                     dic=temp_dic
#             j+=1
#         return dic


# i=n-1
# final_dic={}
# final_dic[0]=-sys.maxsize-1
# final_dic[1]=''

# while i>=0:
#     returned_dic=lis(i)
    
#     if final_dic[0]<returned_dic[0]:
#         final_dic=returned_dic
#     i=i-1

















 

    