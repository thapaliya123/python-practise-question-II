"""
9. Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found.
"""

def binarySearch (arr, l, r, x): 
  
    if r >= l: 
  
        mid = l + (r - l) // 2
  
        if arr[mid] == x: 
            return mid 
          
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
   
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        return -1
  
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print (f"Element is present at index {result}") 
else: 
    print ("Element is not present in array") 



# def binary_search_function(arr, x):
#     arr.sort()
#     print(arr) 
#     arr_length = len(arr)

#     # mid_item_index, lower_half, upper_half = get_mid_lower_upper(arr, arr_length)
#     if arr_length%2 == 0:
#         mid_item_index = (arr_length/2)-1
#         lower_half = arr[0:mid_item_index]
#         upper_half = arr[mid_item_index+1:]
#     else:
#         mid_item_index = (arr_length)//2
#         lower_half = arr[0:mid_item_index]
#         upper_half = arr[mid_item_index+1:]

    
#     if x==arr[mid_item_index]:
#         return mid_item_index
#     elif x<arr[mid_item_index]:
#         arr = lower_half
#         if (len(arr)!=0):
#             binary_search_function(arr, x)
#         else:
#             return -1
#     else:
#         arr = upper_half
#         if(len(arr)!=0):
#             binary_search_function(arr, x)
#         else:
#             return -1

# arr = [ 2, 3, 4, 10, 40 ] 
# x = 10
# print(binary_search_function(arr, x))

