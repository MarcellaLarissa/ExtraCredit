def target(list_nums, target_num):
    li = []
    

    for x in range(0, len(list_nums)):
        if list_nums[x] < target_num:
            candidate = list_nums[x]

            for y in range(0, len(list_nums)):
                if (list_nums[y] + candidate == target_num):
                    li.append(candidate)
                    li.append(list_nums[y])
                    return li

list_nums = [1,5,7,4,3]
target_num = 8

target_li = target(list_nums, target_num)
print(target_li)