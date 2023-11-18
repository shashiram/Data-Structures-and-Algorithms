
""" 


"""

metals=[[5,3],[10,5]]


sorted_metals=[[10,5],[6,3]]

T=100

list=[]


for i in range(len(sorted_metals)):

    value=sorted_metals[i][1]
    weight_required=T/value
    weight_given=sorted_metals[i][0]
    if weight_given>= weight_required:
        list.append(weight_required)
        break
    else:
        list.append(weight_given)
        T=T-value*weight_given

if T>0:
    print("Not possible")
    print(T)

print(sum(list))


            

    

    

    

    


