
'''
Title: Membership Operators

Info:  These operators can be used with any iterable data structure in 
Python, including Strings, Lists and Tuples.

Output:  Returns True if given element is a part of the structure or
         False if it is NOT.

Complexity: It uses different methods of search depending on the type 
            of the structure:
            - For List, String, Tuple it uses Linear Search -> O(n)
            - For Set, Dictionaries will use (hash-table lookup) -> O(1)
'''

def MembershipOperators(source, key):
    return key in source



'''
Title: Linear Search

Info:  It is one of the simplest searching algorithms and the easiest 
       to understand. It doesn't require the collection to me sorted 
       before execution og that algorithm.

Output:  Return the index of the first occurrence (if there is no 
         such element it will return '-1')

Complexity: Time complexity is O(n), space complexity is O(1)
'''

def LinearSearch(source, key):
    for i in range(len(source)):
        if source[i] == key:
            return i
    return -1




'''
Title: Binary Search

Info:  It was implemented by 'Divide and Conquer' methodology. It is 
       much faster than Linear Search but it requires the array to be 
       sorted before that.
       Binary search algorithm can be written either recursively or
       iteratively. (recursion is generally slower in Python because it
       requires the allocation of new stack frames)

Output:  Return the index of the first occurrence (if there is no 
         such element it will return '-1')

Complexity: Time complexity is O(log n)
'''

def BinarySearch(source, key):
    f_pos = 0
    l_pos = len(source) - 1
    index = -1
    while (f_pos <= l_pos) and (index == -1):
        mid = (f_pos+l_pos)//2
        if source[mid] == key:
            index = mid
        else:
            if key < source[mid]:
                l_pos = mid - 1
            else:
                f_pos = mid + 1
    return index








