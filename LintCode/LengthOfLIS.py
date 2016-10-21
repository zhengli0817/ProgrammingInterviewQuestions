# https://leetcode.com/problems/longest-increasing-subsequence/
# http://www.lintcode.com/en/problem/longest-increasing-subsequence/
# https://www.hackerrank.com/challenges/longest-increasing-subsequent
#Given an unsorted array of integers, find the length of longest increasing subsequence.
#
#For example,
#Given [10, 9, 2, 5, 3, 7, 101, 18],
#The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.
#
#Your algorithm should run in O(n2) complexity.
#
#Follow up: Could you improve it to O(n log n) time complexity?

# ref: http://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming
# ref: http://bookshadow.com/weblog/2015/11/03/leetcode-longest-increasing-subsequence/

# DP O(n^2) solution
def LengthOfLIS(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = [1] * size
        for x in range(size):
            for y in range(x):
                if nums[x] > nums[y]:
                    dp[x] = max(dp[x], dp[y] + 1)
        return max(dp) if dp else 0
        
# A more efficient O(nlogn) solution
# ref: https://en.wikipedia.org/wiki/Longest_increasing_subsequence#Efficient_algorithms
def LengthOfLIS2(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high) / 2
                if dp[mid] >= nums[x]:
                    high = mid - 1
                else:
                    low = mid + 1
            if low >= len(dp):
                dp.append(nums[x])
            else:
                dp[low] = nums[x]
        return len(dp)
        
# Another faster and more elegant solution using bisect_left
from bisect import bisect_left        
def LengthOfLIS3(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = []
        for x in range(size):
            low = bisect_left(dp, nums[x])
            if low >= len(dp):
                dp.append(nums[x])
            else:
                dp[low] = nums[x]
        return len(dp)

# IO code for HackerRank         
#n = int(raw_input())
#a = list()
#for i in range(n):
#    temp = int(raw_input())
#    a.append(temp)
#print LengthOfLIS3(a)