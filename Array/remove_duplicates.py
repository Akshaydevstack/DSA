# arr = [1,1,2,2,3,4,4]

# def remove_dup(arr):

#     new_arr = []

#     for i in range(len(arr)):
#         if not new_arr or arr[i]!=new_arr[-1]:
#             new_arr.append(arr[i])

#     return new_arr

# print(remove_dup(arr))


arr = [1, 1, 2, 2, 2, 3, 4, 4]


def remove_dupli(arr):

    slow = 0

    for fast in range(1, len(arr)):

        if arr[slow] != arr[fast]:

            slow += 1

            arr[slow] = arr[fast]
    
    return slow+1

lenght =remove_dupli(arr)

print(arr[:lenght])