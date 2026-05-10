arr = [12,34,56,78,32,121,3,4,5,9,90,4]

def max_element_value(arr):
    max_element = arr[0]
    for num in arr:
        if max_element < num:
            max_element = num
    
    return max_element

print(max_element_value(arr))