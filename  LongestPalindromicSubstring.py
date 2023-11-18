
""" 
 Longest Palindromic Substring 

      Input: s = "baba"
      Output: "bab"
      Explanation: "aba" is also a valid answer.
    
"""
import math


class Solution:
      def longestPalindrome(self, s: str) -> str:
            
            def fun(i,j):

                

                if i==j:
                    return s[i]
    
                else:
                    if i+1==j and s[i]==s[j]:
                        return s[i]+s[j]
                         
                    mid =math.floor(i + (j-i)/2)
                    left=fun(i,mid)
                    right=fun(mid+1,j)

                    k_start= i+ math.floor((mid-i+2)/2)
                    k_end= mid +math.floor((j-mid + 1)/2)

                    k=k_start

                    cur_max_str=''

                    if len(left)>=len(right):
                        cur_max_str=left
                    else:
                        cur_max_str=right
                    
                    print(str(k_start)+"======" +str(k_end))
                    while k<= k_end:

                       

                        
                        
                        temp_str=pald(s[k],k-1,k+1,i,j)

                        if len(temp_str)>len(cur_max_str):
                            cur_max_str=temp_str
                        
                        temp_cnt=pald('',k,k+1,i,j)
                        if len(temp_cnt)>len(cur_max_str):
                                cur_max_str=temp_cnt

                        k+=1

                    return cur_max_str
                    
            def pald(sub_str,p,q,i,j):

                



                while p>= i and q<=j:

                  
                   
                    if s[p]==s[q]:
                        sub_str=s[p]+sub_str+s[q]
                        p-=1
                        q+=1
                    else:
                        break
                return sub_str
                    
            return fun(0,len(s)-1)


            
s="gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv"
sl = Solution()
print(sl.longestPalindrome(s))


            






        




    


    










                

            



       

      
    