def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

array = [10, 23, 31, 55, 40]
print(reverse_list(array))  
