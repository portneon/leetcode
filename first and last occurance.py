nums = [5,7,7,8,8,10]
target = 8
left = 0
right = len(nums)-1
first_occ = 10000009
last_occ= 0
while left<=right:
    mid = (left+right)//2
    if nums[mid] == target:
        first_occ = min(mid,first_occ)
        right = mid-1
    elif nums[mid] < target:
        left = mid+1
    else:
        right = mid-1
left = 0
right = len(nums)-1
while left<=right:
    mid = (left+right)//2
    if nums[mid] == target:
        last_occ = max(mid,last_occ)
        left = mid+1

    elif nums[mid] < target:
        left = mid+1
    else:
        right = mid-1
print(first_occ, last_occ)