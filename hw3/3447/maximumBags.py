def maximumBags(list1, list2, int):
    l = list(zip(list1, list2))
    l.sort(key=lambda x: x[0] - x[1])

    count = 0
    for pair in l:
        left = pair[0] - pair[1]
        if (left <= int):
            int -= left
        else:
            break
        count += 1

    return count
