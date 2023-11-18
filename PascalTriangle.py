
num_rows=25

result_list=[[1]]


def fun (row):

        if(row>num_rows):
             return

        row_list=result_list[row-2]
        list=[]
        for i in range(row):
            if i==0:
                list.append(1)
            elif i==len(row_list):
                list.append(1)
            else:
                sum=row_list[i-1]+row_list[i]
                list.append(sum)

        result_list.append(list)
    
        fun(row+1)

if num_rows==1:
    print(result_list)
else:
    fun(2)
    print(result_list)


for item in result_list:
    print(item)






