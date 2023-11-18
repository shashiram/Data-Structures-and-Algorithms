
# Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [widthi, lengthi, heighti] (0-indexed). Choose a subset of cuboids and place them on each other.

# You can place cuboid i on cuboid j if widthi <= widthj and lengthi <= lengthj and heighti <= heightj. You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.

# Return the maximum height of the stacked cuboids.

# Input: cuboids = [[50,45,20],[95,37,53],[45,23,12]]
# Output: 190
# Explanation:
# Cuboid 1 is placed on the bottom with the 53x37 side facing down with height 95.
# Cuboid 0 is placed next with the 45x20 side facing down with height 50.
# Cuboid 2 is placed next with the 23x12 side facing down with height 45.
# The total height is 95 + 50 + 45 = 190.

cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]

N=len(cuboids)

memo={}

def dp(i,w,l,h):

    key=str(i)+str(w)+str(l)+str(h)

    if key in memo:
        return memo.get(key)
    max_height=h

    print(key)

    for j in range(N):
        cuboids_j=cuboids[j]
        w_j=cuboids_j[0]
        l_j=cuboids_j[1]
        h_j=cuboids_j[2]

        ch1=0
        ch2=0
        ch3=0
        ch4=0
        ch5=0
        ch6=0

        if (w_j<w and l_j<l and h_j<h):
            ch1=h+dp(j,w_j,l_j,h_j)
        if (w_j<l and l_j<w and h_j<h):
            ch2=h +dp(j,l_j,w_j,h_j)
        if (w_j<w and h_j<h and l_j<h):
            ch3=h +dp(j,w_j,h_j,l_j)
        if (h_j<w and w_j<h and l_j<h):
            ch4=h +dp(j,w_j,h_j,l_j)
        if (l_j<w and h_j<h and w_j<h):
            ch5=h +dp(j,l_j,h_j,w_j)
        if (h_j<w and l_j<h and w_j<h):
            ch6=h +dp(j,w_j,h_j,l_j)

        tem=max(ch1,ch2,ch3,ch4,ch5,ch6)

        max_height=max(max_height,tem)

    memo[key]=max_height

    return max_height

       

max_len=0

for i in range(N):
    cuboids_i=cuboids[i]
    w=cuboids_i[0]
    l=cuboids_i[1]
    h=cuboids_i[2]
    ch1=dp(i,w,l,h)
    ch2=dp(i,w,h,l)
    ch3=dp(i,h,l,w)

    max_len=max(max_len,ch1,ch2,ch3)


print(max_len)
    

    



        