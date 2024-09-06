def minmumSubSum(target:int,nums:list[int]) -> int:
    ans = float('inf')

    left = 0
    cur = 0
    for right in range(len(nums)):
        cur += nums[right]
        while cur >= target and left < right:
            ans = min(ans, right - left +1)
            cur -= nums[left]
            left += 1
    ans = ans if ans != float('inf') else 0
    print(ans)
    return ans 

# target = 7
# nums = [2,3,1,2,4,3]
# minmumSubSum(target,nums)

target1 = 4
nums1 = [1,4,4]
minmumSubSum(target1,nums1)

target = 11
nums = [1,1,1,1,1,1,1,1]
minmumSubSum(target,nums)