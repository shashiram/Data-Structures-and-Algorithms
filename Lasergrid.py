
rows = 4
cols = 4
initR = 1
initC = 0
finalR = 2
finalC = 3
costRows = [1, 2, 3]
costCols = [4, 5, 6]

parents={}

def dp(i,j):

    key=str(i)+'_'+str(j)

    print(i,j)

    if i==finalR and j==finalC:
        return 0
    else:

        list=[]

        if ((str(i-1)+'_'+str(j)) not in parents ) and (i-1)>=0:

            ch1=(costRows[i-1] if i==rows-1 else costRows[i-1]) +dp(i-1,j)

            tem_dic=[(str(i-1)+'_'+str(j)),ch1]

            list.append(tem_dic)

        if ((str(i+1)+'_'+str(j)) not in parents ) and (i+1)<rows:

            ch2=costRows[i] +dp(i+1,j)

            tem_dic=[(str(i+1)+'_'+str(j)),ch2]

            list.append(tem_dic)

        if ((str(i)+'_'+str(j-1)) not in parents ) and (j-1)>=0:
            ch3=costRows[j-1] if j==cols-1 else costCols[j] +dp(i,j-1)

            tem_dic=[(str(i)+'_'+str(j-1)),ch3]

            list.append(tem_dic)

        if ((str(i)+'_'+str(j+1)) not in parents ) and (j+1)<cols:
            ch4=costRows[j]+dp(i,j+1)

            tem_dic=[(str(i)+'_'+str(j+1)),ch4]

            list.append(tem_dic)

        min_list=[]
        for i in range(len(list)):

            if i==0:
                min_list=list[i]
            else:

                if list[i][1]<min_list[1]:
                    min_list=list[i]
                 
        parents.setdefault(min_list[0])

        return min_list[1]

key=str(1)+'_'+str(0)
parents.setdefault(key)
print(dp(1,0))

print(parents)

        



    
 
    
 
