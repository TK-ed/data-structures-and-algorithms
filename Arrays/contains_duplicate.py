nums = [1,1,1,3,3,4,3,2,4,2]
size = len(nums)-1
l = nums[0]
r = nums[size-1]
print(r)
while l<r:
    if nums[l] == nums[r]:
       print("True")
    l+=1
    r-=1
print("False")
