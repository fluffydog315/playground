class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        # Initialize variables to keep track of the length of the longest 
        # wiggle subsequence and the last wiggle direction
        max_len = 1
        last_wiggle = None
        l = 0
        res = 0
        for i in range(1, n):
            # Calculate the difference between the current and previous element
            diff = nums[i] - nums[i-1]
            # If the difference is positive and the last wiggle direction was negative
            # or the difference is negative and the last wiggle direction was positive,
            # then we've found a new wiggle direction and can update the length of the 
            # longest wiggle subsequence
            if (diff > 0 and last_wiggle != 1) or (diff < 0 and last_wiggle != -1):
                max_len += 1              
                res += i - l
            elif diff != 0 and last_wiggle is None:
                res += 1 
            elif diff == 0 :
                l = i 
            else:
                #keep descreasing 
                #print(i)
                res += 1 
                l = i - 1
                # Update the last wiggle direction
   
            last_wiggle = 1 if diff > 0 else -1    
        #return max_len
        return res 

arr1 = [9,8,7,6,5]
q = Solution()
print(q.wiggleMaxLength(arr1))
arr2 = [1,2,1,3,4,-2]
print(q.wiggleMaxLength(arr2))
arr3 = [1,2,1,2,1]
print(q.wiggleMaxLength(arr3))
arr4 = [10,10,10]
print(q.wiggleMaxLength(arr4))

# 4
#9
#10
#0 
