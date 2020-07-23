"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

def max_product(arr):
    local_max_product = arr[0]
    local_min_product = arr[0]
    global_max_product = arr[0]

    for ele in arr[1:]:
        if ele < 0:
            local_max_product, local_min_product = local_min_product, local_max_product

        local_min_product = min(ele, local_min_product*ele)
        local_max_product = max(ele, local_max_product*ele)

        global_max_product = max(global_max_product, local_max_product)

    print arr
    print global_max_product

for arr in [[2,3,-2,4], [-2,0,-1], [1, 0, -2, -3, -2, 1]]:
    max_product(arr)
