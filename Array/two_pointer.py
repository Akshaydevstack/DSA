arr = [1,2,3,4,5,6]
target = 10

def two_sum(arr,target):

    lp,rp = 0,len(arr)-1

    while lp<rp:
        cr_sum = arr[lp] + arr[rp]

        if cr_sum == target:
            return [lp,rp]
        elif  cr_sum < target:
            lp+= 1
        else:
            rp-=1
        

print(two_sum(arr,target))
