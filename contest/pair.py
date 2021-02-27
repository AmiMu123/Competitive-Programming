def pairs(k, arr):
    count, s = 0, set(arr)
    for i in arr:
        if (k + i) in s:
            count += 1
    return count
