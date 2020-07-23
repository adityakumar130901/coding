from sys import maxint 
def maxSubArraySum(a,size): 
    max_so_far = a[0]
    local_sum = a[0]

    for ele in a[1:]:
        local_sum = max(ele, local_sum+ele)
        max_so_far = max(max_so_far, local_sum)
   
    return max_so_far 
   
# Driver function to check the above function  
a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print "Maximum contiguous sum is", maxSubArraySum(a,len(a))
