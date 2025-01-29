# nums = [3, 2, 3]
majority_count = len(nums) // 2

count_dict = {}
for num in nums:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

result = None
for k, v in count_dict.items():
    if v > majority_count:
        result = k
        break

return result
