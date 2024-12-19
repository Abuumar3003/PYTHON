def closest_sum_to_zero(arr):

    arr.sort()
    min_sum = float('inf')
    closest_pair = (None, None)
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            closest_pair = (arr[left], arr[right])
        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return closest_pair
arr = [1, 5, 3, 2, 4]
result = closest_sum_to_zero(arr)
print(f"The two elements whose sum is closest to zero are: {result}")
