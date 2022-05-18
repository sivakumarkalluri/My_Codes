

def minMoves2(nums):
    nums.sort()
    ans, median = 0, nums[len(nums) // 2]
    for num in nums: ans += abs(median - num)
    return ans
print(minMoves2([2849,1620,705,1,30]))