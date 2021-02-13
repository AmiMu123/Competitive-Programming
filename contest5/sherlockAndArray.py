def balancedSums(arr):
    right_sum = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        if left_sum == right_sum-arr[i]-left_sum:
            return "YES"
        left_sum += arr[i]
    return "NO"
