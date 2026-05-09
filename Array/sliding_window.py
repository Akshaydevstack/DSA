# arr = [2,3,4,9,5,1,6,7]

# k = 3

# window_sum = sum(arr[:k])

# max_sum = window_sum

# for i in range(k,len(arr)):
#     window_sum = window_sum - arr[i-k] + arr[i]
#     if max_sum < window_sum:
#         max_sum = window_sum
        
#         subarry = [i-k+1,k]
    

# print(max_sum)
# print(subarry)


arr = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k,len(arr)):
    window_sum = window_sum - arr[i-k] + arr[i]
    max_sum = max(window_sum,max_sum)


print(max_sum)