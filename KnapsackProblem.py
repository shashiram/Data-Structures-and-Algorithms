

profit=[1,2,3]
weight=[4,5,6]

bag_capasity=3

def fun(i,bag_capasity):

    if i==3:
        return 0
    else:
       ch_1= fun(i+1,bag_capasity)
       if bag_capasity-weight[i]>0:
           ch_2=fun(i+1,bag_capasity-weight[i])+profit[i]
           return max(ch_1,ch_2)
       else:
           return ch_1

print(fun(0,bag_capasity))
