class Solution:

    '''
    def nextPermutation(self, nums):
        perm, l = False, len(nums) - 2
        while 0 <= l:
            r = len(nums) - 1  
            while l < r and nums[r] <= nums[l]: 
                r -= 1
            if r <= l: 
                l -= 1
            else:
                nums[l], nums[l + 1:], perm = nums[r], sorted(nums[l + 1:r] + [nums[l]] + nums[r + 1:]), True
                break
        if not perm: nums.sort()
    '''

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        flag = 0
        while i > 0:
            if nums[i] > nums[i - 1]:
                # 往后找大于nums[i-1]且小于nums[i]的数与nums[i-1]交换
                j = len(nums) - 1
                while j > i:
                    if nums[i - 1] < nums[j] < nums[i]:
                        nums[j], nums[i - 1] = nums[i - 1], nums[j]
                        flag = 1
                        break
                    j -= 1

                # 找不到这样的数
                if flag == 0:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]

                # 交换后对i后面的元素进行排序
                nums[i:] = sorted(nums[i:])
                return
            else:
                i -= 1
        nums.sort()  # 重新从小到大排序





arr = [3,9,5,7,4]
a = Solution()
res = a.nextPermutation(arr)
print(res)