arr = [1,2,3,4,5,6,7]

k = 3


def reverse(arr, left, right):

    while left < right:

        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1


def rotate_array(arr, k):

    n = len(arr)

    # Important optimization
    k = k % n

    # Step 1
    reverse(arr, 0, n-1)

    # Step 2
    reverse(arr, 0, k-1)

    # Step 3
    reverse(arr, k, n-1)

    return arr


print(rotate_array(arr, k))