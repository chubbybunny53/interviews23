class Solution(object):

    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0 
        end = 1
        numsLen = len(nums)
        minLen = numsLen
        
        if (numsLen == 1):
            if nums[0] == target:
                return 1
            else:
                return 0
            
        while (start < end):
            curLen = end - start + 1
            tmpList = nums[start:end+1]
            tmpSum = sum(tmpList)
            print("start, end, curLen, tmpList, tmpSum: ", start, end, curLen, tmpList, tmpSum)
            if tmpSum == target:
                if curLen < minLen:
                    minLen = curLen
                start += 1
            if tmpSum > target:
                start += 1
                end = start + 1
            else: #tmpSum < target
                end += 1
            if end == minLen:
                start += 1
                end -= 1
        return minLen

s = Solution()
s.target = 4
s.nums = [1,4,4]

print("RETURN: ", s.minSubArrayLen(s.target, s.nums))