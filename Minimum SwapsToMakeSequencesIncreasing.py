

nums1 = [1,3,5,4]
nums2 = [1,2,3,7]
cnt=0
def dp(i,j):
    if j>=len(nums1):
        return
    if (nums1[i]<nums1[j]) and (nums2[i]<nums2[j]):
        dp(i+1,j+1)
    else:
        tem=nums1[i]
        nums1=nums2[i]
        nums2=tem
        cnt=cnt+1
        dp(i,j)


print(dp(0,1))