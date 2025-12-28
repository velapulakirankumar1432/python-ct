def combine(nums, k, start, current):
    if len(current) == k:
        print(current)
        return
    for i in range(start, len(nums)):
        combine(nums, k, i + 1, current + [nums[i]])
nums = [1, 2, 3, 4]
combine(nums, 2, 0, [])
