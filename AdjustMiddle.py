# -*- coding: utf-8 -*-
#给你一个数组，比如[6,2,3,4]，如果一个数比左右的都小，就变大一个，比左右的都大就变小一个。直到不变为止。收尾两个数不能动。
#[6,2,3,4]就变成[6,3,3,4] [1,6,3,4,3,5] 就变成[1,4,4,4,4,5]
# [1,6,3,4,3,5] -> [1,5,4,4,4,5] -> [1,4,4,4,4,5]
#一群学生考很多次试 给一个int[] 表示第一次的分数 然后规则是如果一个学生两边的学生分数都比他高 下次他就多考一分； 如果都不如他就少考一分; 不然不变； 
#求最后的稳定状态 -- 其实就是找到最后的monotone sequence

def AdjustMiddle(nums):
    lenNums = len(nums)
    if lenNums<=2: return nums
    else:
        marks = [0 for num in nums]
        i=0
        while True:
            if i==lenNums: i=0
            if i==0:
                i += 1 
                continue            
            if i==(lenNums-1): 
                nums = [sum(x) for x in zip(nums, marks)]
                marks = [0 for num in nums]
                i += 1
                continue
                           
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]: marks[i] = -1
            if nums[i]<nums[i-1] and nums[i]<nums[i+1]: marks[i] = 1 
            if all([mark == 0 for mark in marks[1:-1]]): break
            i += 1
            
    return nums
            
            
        #i = 1
        #while i>=1 and i<=(lenNums-2):
        #    if nums[i]>nums[i-1] and nums[i]>nums[i+1]: nums[i] -= 1
        #    if nums[i]<nums[i-1] and nums[i]<nums[i+1]: nums[i] += 1
        #    i += 1
        #    if i==(lenNums-1): i = 1
            