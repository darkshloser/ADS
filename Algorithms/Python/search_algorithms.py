
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

Complexity: Time complexity is O(log n).
            Space complexity O(1) for iterative, O(log n) for recursive.
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




'''
Title: Jump Search

Info:  It's similar to Binary Search t works on sorted array and uses
       similar 'Divide and Conquer' approach.
       We search in jumps and when 'key' is between jumps like 
       source[i] < key < source[i+jump] it will perform Linear search.


Output:  Return the index of the first occurrence (if there is no 
         such element it will return '-1')

Complexity: Time complexity is O(sqrt(n))
'''

import math

def JumpSearch(source, key):
    length = len(source)
    jump = int(math.sqrt(length))
    i = 0

    while i != length - 1 and source[i] < key:
        if source[i+jump-1] == key:
            return i+jump-1
        elif source[i+jump-1] > key:
            block = source[i: i+jump-1]
            return i + LinearSearch(block, key)
        i += jump
    
    block = source[i: i+jump]
    return i + LinearSearch(block, key)




'''
Title: Fibonacci Search

Info:  It's similar to binary and jump search.
       It's using Fibonacci numbers to calculate the block size or
       search range in each step.
       Algorithm works with three fibonacci numbers at a time.
       fib = fib_minus_1 + fib_minus_2. The advantage is that it 
       handle arrays that are too large, because it searches in 
       increasing step size.


Output:  Return the index of the first occurrence (if there is no 
         such element it will return '-1')

Complexity: Time complexity is O(log n). The algorithm is faster than
            Linear search and jump search in most cases.
'''

def FibonacciSearch(source, key):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(source)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(source)-1))
        if (source[i] < key):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (source[i] > key):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(source)-1) and source[index+1] == key):
        return index+1
    return -1





'''
Title: Exponential Search

Info:  It's also known by the names galloping search, doubling search
       and Struzik search. It depends on the binary search to perform 
       final comparison.

Output:  Return the index of the first occurrence (if there is no 
         such element it will return '-1')

Complexity: Time complexity Best case O(log i) 'i' is the index of
            the item we are searching for. Worst case O(log n)
'''

def ExponentialSearch(source, key):
    if source[0] == key:
        return 0
    index = 1
    while index < len(source) and source[index] <= key:
        index = index * 2
    return BinarySearch(source[:min(index, len(source))], key)







