def merge_sorted_array(nums1,nums2):
    n1 = len(nums1)
    for i in range(n1):
        if nums1[i] == 0:
            # print(nums1,nums2)
            nums1[i] = nums2.pop(0)
    nums1.sort()
    return nums1

print(merge_sorted_array([1,2,3,0,0,0],[2,5,6]))