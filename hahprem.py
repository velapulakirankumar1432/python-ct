def perm(nums, i):
    if i == len(nums) - 1:
        print(nums)
        return
    hash={}
    for j in range(i, len(nums)):
        if nums[j]not in hash:
            hash[nums[j]]=True
            nums[i], nums[j] = nums[j], nums[i]
            perm(nums, i + 1)
            nums[i], nums[j] = nums[j], nums[i]  
perm ([1, 1, 3], 0)
