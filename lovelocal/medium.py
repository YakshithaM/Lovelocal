from collections import Counter

def majority_elements(nums):
    counter = Counter(nums)
    n = len(nums) // 3
    return [num for num, count in counter.items() if count > n]

# Test cases
nums1 = [3, 2, 3]
output1 = majority_elements(nums1)
print(output1)

nums2 = [1]
output2 = majority_elements(nums2)
print(output2)

nums3 = [1, 2]
output3 = majority_elements(nums3)
print(output3)
