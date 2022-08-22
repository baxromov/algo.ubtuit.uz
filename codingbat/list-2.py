nums = [2, 1, 2, 3, 4]

# def count_evens(nums):
#     count = 0
#     for num in nums:
#         if num % 2 == 0:
#             count += 1
#     return count
#
# print(count_evens(nums))


# def big_diff(nums):
#     return max(nums) - min(nums)

# def centered_average(nums):
#     small = min(nums)
#     large = max(nums)
#     return (sum(nums) - small - large) / (len(nums) - 2)

# def sum13(nums):
#     for i in range(len(nums)):
#         if nums[i] == 13:
#             nums[i] = 0
#             if i + 1 < len(nums):
#                 nums[i + 1] = 0
#     return sum(nums)
# a = [1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]
#
#
# def sum67(nums):
#     n = len(nums)
#     count = True
#     summa = 0
#     for i in range(0, n, 1):
#         if nums[i] == 6:
#             count = False
#         elif count == False and nums[i] == 7:
#             count = True
#         elif count:
#             summa += nums[i]
#     return summa
# print(sum67(a))

# b = [1, 2, 1, 2]
#
# def has22(nums: list):
#     n = len(nums)
#     for i in range(n - 1):
#         if nums[i] == 2 and nums[i + 1] == 2:
#             return True
#     return False
# print(has22(b))