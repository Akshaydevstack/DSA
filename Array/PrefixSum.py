# Normal way 

Arr = [2,4,6,8,10] 


# bute force
def Sum(arr,rang):
    res = 0
    for i in range(0,rang+1):
        res+= arr[i] 
    return res

print(Sum(Arr,4))


