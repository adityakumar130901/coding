def get_min_jump(arr):
    if not arr:
        return "Empty Array !!"

    steps_left = arr[0]
    max_reachable_index = arr[0]
    jump_count = 1
    _len = len(arr)

    path = arr[0]

    path_element = arr[0]

    for cur_index, element in enumerate(arr[1:]):
        if cur_index == (_len-1):
            break

        max_reachable_index = max(max_reachable_index, cur_index+element)
        steps_left = steps_left - 1

        if steps_left == 0:
            # we can not reach end
            if cur_index >= max_reachable_index:
                jump_count = -1
                break

            jump_count = jump_count + 1
            steps_left = max_reachable_index - cur_index
            path = "%s-%s"%(path, path_element)

    print "Min Jump: %s"%jump_count

for arr in [[1,2,3,0,0,0,1], [1,2,3,0,0,1], [1,3,5,8,9,2,6,7,6,8,9]]:
#for arr in [[1,2,3,0,0,1]]:
    print arr
    get_min_jump(arr)
