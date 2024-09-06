def moveZeros(nums:list[int]) -> None:
    non_zero_idx = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_idx] , nums[i] = nums[i], nums[non_zero_idx]
            non_zero_idx += 1
    print(nums)

nums = [0,1,0,3,12]
nums2 = [0]
moveZeros(nums)
moveZeros(nums2)

