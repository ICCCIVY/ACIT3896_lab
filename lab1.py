#Part 1
#Ivy Chen
#Jovica Kuzmanovic

def linear_search(needle, haystack):
    for n in range(len(haystack)):
        if haystack[n] == needle:
            return n
    
#How you can actually do it

# def linear_search(needle, haystack):
#     try:
#         return haystack.index(needle)
#     except:
#         return None

# print(linear_search(3,[1,45,5,6,7,9,4,5,3,1]))

#Part 2

def binary_search(needle, haystack):
    bootom = 0
    middle = 0
    top = len(haystack) - 1

    while bootom <= top:
        middle = (bootom+top) // 2

        # Checking if the needle is in the middle
        if haystack[middle] < needle:
            bootom = middle +1

        # If the number is greater ignore the half
        elif haystack[middle] > needle:
            top = middle + 1

        # if the number is smaller ignore the right
        else:
            return middle
    return -1
