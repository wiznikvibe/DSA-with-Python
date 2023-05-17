##### Max Product Sub Array #####
# Given an input array []
# Output largetst product subarray return product

""" Time Complexity = O(n) -- Scan """
""" Space = O(1) """

def maxProd(nums):
    res = nums[0]
    curMax, curMin = 1, 1

    for _ in nums:
        vals = (_, _*curMax, _*curMin)
        curMax, curMin = max(vals), min(vals)

        res = max(res, curMax)
    return res