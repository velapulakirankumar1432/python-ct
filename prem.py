def perm(nums, i):
    if i == len(nums) - 1:
        print(nums)
        return
    for j in range(i, len(nums)):
        nums[i], nums[j] = nums[j], nums[i]
        perm(nums, i + 1)
        nums[i], nums[j] = nums[j], nums[i]  # backtrack
perm([1, 2, 3], 0)
