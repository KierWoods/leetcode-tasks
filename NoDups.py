
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Count length of new array.
        count = 0
        
        # For loop to iterate through length of array.
        for i in range(len(nums)):
            # Skip matching numbers
            if i < len(nums) - 2 and nums[i] == nums[i + 1]:
                continue
             
            # update array and 
            nums[count] = nums[i]
            count += 1
        return count
r = Solution()
print(r.removeDuplicates([1,1,2]))  