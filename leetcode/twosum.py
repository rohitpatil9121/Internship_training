class Solution(object):
    def twoSum(self, nums, target):
        num = {}

        for index, value in enumerate(nums):

            find_another = target - value

            if find_another in num:
                return [num[find_another], index]

            num[value] = index

    list1 = [2,7,11,15]
    target = 9

    