# Normal way 

Arr = [2,4,6,8,10] 


# # bute force
# def Sum(arr,rang):
#     res = 0
#     for i in range(0,rang+1):
#         res+= arr[i] 
#     return res

# print(Sum(Arr,4))


# arr = [12,232,323,43,45,67,9]

# prefix = [0]* len(arr)

# prefix[0] = arr[0]

# for i in range(1,len(arr)):
#     prefix[i] = prefix[i-1] + arr[i]


# def sumOfRange(prefix,L,R):

#     if L == 0:
#         return prefix[R]
#     return prefix[R] - prefix[L-1]

# print(prefix)
# print(sumOfRange(prefix,2,5))


# arr = [2,4,6,8,10]

# def Prefix_sum(nums):

#     prefix = [0]* len(nums)
#     prefix[0] = nums[0]

#     for i in range(1,len(nums)):
#         prefix[i] = prefix[i-1]+nums[i]

#     return prefix

# print(Prefix_sum(arr)) 

# arr = Prefix_sum(arr)


# def sum_of_range(prefix,l,r):

#     if l == 0:
#         return prefix[r]
    
#     return prefix[r] - prefix[l-1]


# print(sum_of_range(arr,0,1))



# arr= [1,23,34,64]

# newk =arr[-1:-2]

# print(newk)

