class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # self.solution_01(nums1, m, nums2, n)
        # self.solution_02(nums1, m, nums2, n)
        self.solution_03(nums1, m, nums2, n)
    
    def solution_01(self, nums1: list[int], m: int, nums2: list[int], n: int):
        # Write the elements of num2 into the end of nums1.
        for i in range(n):
            nums1[i + m] = nums2[i]
        
        # Sort nums1 list in-place.
        nums1.sort()

    def solution_02(self, nums1: list[int], m: int, nums2: list[int], n: int):
        # Make a copy of the first m elements of nums1.
        nums1_copy = nums1[:m] 
        
        # Read pointers for nums1Copy and nums2 respectively.
        p1 = 0
        p2 = 0
        
        # Compare elements from nums1Copy and nums2 and write the smallest to nums1.
        for p in range(n + m):
            # We also need to ensure that p1 and p2 aren't over the boundaries
            # of their respective arrays.
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1] 
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
    
    def solution_03(self, nums1: list[int], m: int, nums2: list[int], n: int):
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1
    
        # And move p backward through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            # print('p, n+m',p, n+m)
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # print('p, p2', p, p2)
                nums1[p] = nums2[p2]
                p2 -= 1
        print(nums1)        
            
    # does not work as expected - solution_03 above is the most optimum
    def solution_04(self, nums1: list[int], nums2: list[int]):
        # Set p1 and p2 to point to the end of their respective arrays.
        # m = 0
        # for i in nums1[::-1]:
        #   if i == 0:
        #     m += 1
        #   else:
        #       break

        m = sum(p >= 1 for p in nums1)
        n = sum(p >= 1 for p in nums2)
        p1 = m - 1
        p2 = n - 1
        p3 = m + n
    
        # And move p backward through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(p3 - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
        print(nums1)        


# Solution().merge([1,2,3,0,0,0],3,[2,5,6],3)
Solution().solution_04([1,2,3,0,0,0],[2,5,6])
Solution().solution_04([1],[])
Solution().solution_04([],[])
# incorrect test case
# Solution().solution_04([],[1])
Solution().solution_03([0,0],1,[2],1)
Solution().solution_03([0,0,0],1,[2],1)
# Solution().solution_04([0],[1])
# incorerct output - expected is [-1,0,0,1,2,2,3,3,3]
# Solution().solution_04([-1,0,0,3,3,3,0,0,0],[1,2,2])