#--------------------------Linear Search Algorithm----------
#sequential algorithm that searches through each item in the list until the target is found. We need to go through the indexes of the list using the range function. Create a range of items starting at 0 and goes through the length of the list

# def linear_search(list, target):
#     """
#     Returns the index poistion of the target if found, else returns None
#     """
#     for i in range(0, len(list)):    #len(list)constant time
#         if list[i] == target:
#             return i
#     return None

# my_list = [1,2,3,4,5,6,7,8,9]

# def linear_search_algo(list, target):
#     for index in range(0, len(list)):
#         if list[index] == target:
#             return f"This is your target index position: {index}"
#     return "The target does not exist in the list"

# print(linear_search_algo(my_list, 12))

# list_items = ["Jack", "Jill", "Bob", "Scott"]

# def linear_search(list, target):
#     for i in range(0, len(list)):
#         if list[i] == target:
#             print(f"your target was found at index {i}")
#     return None


# linear_search(list_items, "Bob")

# liste = [1, 2, 56, 98, 58, 200, 3000, 78, 45, 32]
# def linear_search(list, target):
#     for index in range(0, len(list)):
#         if list[index] == target:
#             print(f"Your target is located at index: {index} and it contains the value: {list[index]}")
#     return "Target no located!"


# linear_search(liste, 58)

#----------------------------Binary Search---------------------
#non-sequential algorithm that separates the list in half or smaller sections and then searches for the target.
#first the list should be sorted.If it is not already sorted we must sort it.

#indexes:  0  1  2  3  4  5  6
# liste = [1, 2, 3, 4, 5, 6, 7]
# print(len(liste)) #this will return 7
                     #*
liste = [1, 2, 3, 4, 5, 6, 7]

def binary_search(list, target):
    first = 0 #point to the first element in the list(the index of the first item)
    last = len(list) - 1 #to get the last item in a list we use the leng function and subtract 1 because the index position will be one less than the length

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None #if first, last , midpoint never become equal then the target does not exist, return None

result = binary_search(liste, 5)
print(f"your target is found at index: {result}")

