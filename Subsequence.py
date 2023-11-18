
str1="rjufvjafbxnbgriwgokdgqdqewn"
str2="mjmqqjrmzkvhxlyruonekhhofpzzrjujaxekbcydldcq"


def fun(sub_seq,index1,index2):

    print(sub_seq)

    if index1==len(str1) and sub_seq!=str1:
        return False

    if sub_seq==str1:
        return True
    if sub_seq==str1:
        return False
    char=str1[index1]
    isSub=False
    while index2 <(len(str2) ):
        if char==str2[index2]:
            sub_seq=sub_seq+char

            if fun(sub_seq,index1+1,index2+1):
                isSub=True
                break
        index2+=1
    if isSub:
        return True
    else:
        return False
    
print(fun('',0,0))




    


