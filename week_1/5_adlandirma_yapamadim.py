nums = [1,2,3,3,3,2]
delrpt = list(set(nums))
result = 0
for num in delrpt :
    rptcount = nums.count(num)
    if rptcount > 1 :
        result += rptcount*num
print(result)
