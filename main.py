def median(nums):
    nums = sorted(nums)
    n = len(nums)
    if n % 2 != 0:
        return nums[n // 2]
    else:
        return int(round((nums[n // 2] + nums[n // 2 - 1]) / 2, 0))
# длина списка делится пополам, затем этот элемент складывается с предыдущим элементом и делится на 2, в конце округляется
nums = [int(x) for x in input().split()]
print(median(nums))