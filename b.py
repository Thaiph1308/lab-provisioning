nums1=[1,2,3,0,0,0]
m = 3
nums2=[2,5,6]
n = 3
tmp = 0

# nums1= [1,2,4,5,6,0]
# nums2 = [3]
def merge(nums1, m, nums2, n):
    # for i in range(len(nums1)-n):
    #     for j in range(len(nums2)):
    #         if nums2[j] < nums1[i]:
    #             tmp = nums1[i]
    #             nums1[i] = nums2[j]
    #             nums2[j] = tmp
    #             nums2.sort()
    #             print(f'{len(nums1)-m}, {len(nums2)}, {i}, {j}, {nums1[i]}, {nums2[j]}, {tmp}, nums1: {nums1}, nums2: {nums2}')
    # nums1[m:] = nums2[:]
    # print(nums1)
    i = m - 1
    j = n - 1
    k = m + n - 1
        
    while j >= 0:
        print(f'{i}, {j}, {k}, {nums1[i]}, {nums2[j]}, {nums1[k]}, nums1: {nums1}, nums2: {nums2}')
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
        print(f'{i}, {j}, {k}, {nums1[i]}, {nums2[j]}, {nums1[k]}, nums1: {nums1}, nums2: {nums2}')
        print('-----')
        


merge(nums1,m,nums2,n)