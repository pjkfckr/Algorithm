class Solution:
    def twosum(self, nums, target):
        dic = dict()
        for i, num in enumerate(nums):
            if target-num in dic:
                return [dic[target-num], i]
            else:
                dic[num] = i


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
sol = Solution().twosum(nums, target)
print(sol)