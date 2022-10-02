'''
Merge sort is one of the most well-known sorting algorithms.
In this problem, mergesort takes an array of unique integers as a parameter and returns the sorted array.

 

An array has n elements. If the array has less than 2 elements, then the array is returned without any changes.
If the array has more than two elements, then it is divided into two arrays, left and right.
The left array contains the first half elements of the input array while the right array contains the second half of the elements.
If n is odd, the left array takes the middle element.
Next, the algorithm calls itself first with the left array and then with the right array.
After that, the algorithm produces the sorted array, by merging the left and the right arrays into a single sorted array.
In this challenge, keep a count for each of the elements in the input array.
Initially, all counts are 0. Whenever an integer k from the right array is merged before at least one element from the left array, add 1 to the count.
Find the maximum count value after the merge sort algorithm finishes.

 

Example

arr = [2, 3, 1]

 

All counters are initialized to 0. First, the mergesort divides the input array into left = [2,3] and right = [1].
Next, it runs itself again with the left array. It divides this array into [2] and [3].
Since both are sorted, it merges them, and during the merge 3 is merged after 2 into the sorted order, so nothing is added to the counter.
After the merge, the algorithm returns [2,3] to its caller.
Next, the initial mergesort call runs itself for the right array [1] but since it has only one element no merging is performed and [1] is returned immediately.
Next, the algorithm merges [2,3] with [1]. Since 1 from the right array comes before both elements from the left array during the merge, we add 1 to the counter.
After this merge, the algorithm finishes, and the maximum count after the process is 1.

 

Function Description 

 

Complete the function largestCountValue in the editor below.
The function must return an integer that denotes the maximum count value after the entire merge sort algorithm finishes for the input array arr.

 

The function has the following parameter(s):
arr: integer array of size n with all unique elements   
 

Constraints

1 ≤ n ≤ 105
1 ≤ arr[i] ≤ 109
all elements of arr are distinct

def merge(left, right) -> list:
        left, right = left[::-1], right[::-1]
        merged = []
        while left and right:
            if left[0] > right[0]:
                merged.append(left.pop(0))
            else:
                num = right.pop(0)
                count[num] += 1
                merged.append(num)
        return merged + left + right
'''

'''
We need to count the amount of times each num in the input arr is moved from the right to the left side.
We can accomplish this by wrapping a normal merge sort in a function and keeping our counter in the parent function.

Starting off we create a dict(or object for javascript) and use each number in the input arr as keys with their value set to 0.
Then we write out merge sort as we would normally, the only diffrence is when we write our merge we add to the counter for each
time we move a number from the right to the left.

we call merge_sort and then return max of the values from our counter.
'''

from math import ceil

def merge_counts(arr: list) -> int: # BigO(n log n) time | BigO(n) space
    count = {k: 0 for k in arr} # using dict comprehension we create our dict

    def merge(left, right) -> list: # we then create merge method for merge sort
        merged = [] # this will be our sorted merged, left and right sides.
        while left and right: # we keep looping until one of the sides is empty
            if left[0] < right[0]: # if our right side is bigger we pop the left side and append it to merged
                merged.append(left.pop(0))
            else: # else, which means when the left side is bigger
                num = right.pop(0) # we pop off from right
                count[num] += 1 # increment our counter for that number since we are now "moving" the number from right to left
                merged.append(num) # then we add the num to merged
        return merged + left + right # after the loop has ended we can then return merged + left + right, we do this so left or right has one left it is appened to the back

    def merge_sort(arr) -> list: # now we can create merge_sort itself
        if len(arr) <= 1: # our base case, if the input length of arr is 1 or less return it
            return arr

        mid = ceil(len(arr) / 2) # grab our mid point, normally it's fine to just use // to get it, but for this problem we have to ceil it.
        left = merge_sort(arr[:mid]) # grab all values to the left of the mid point (excluding the mid point) and call itself with the halfed arr.
        right = merge_sort(arr[mid:]) # grab all values to the right of the mid point (including the mid point) and call itself with the halfed arr.

        return merge(left, right) # we then call the merge method on the left and right. 

    merge_sort(arr) # call merge sort, we don't need the sorted arr at all we just need it to find what we are really looking for.
    # after merge_sort has ran, count will be filled with our answer

    return max(count.values()) # now we can just get the largest value from count's values

arr = [1, 2, 3, 4, 5, 10]
print(merge_counts(arr))


