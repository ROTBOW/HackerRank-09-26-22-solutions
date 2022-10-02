'''
Given a collection of time intervals, [start, end], merge and return the overlapping intervals sorted in ascending order of their start times.

 

Example
intervals = [[7, 7], [2, 3], [6, 11], [1, 2]]

 

The interval [1, 2] merges with [2, 3] while [7, 7] merges with [6, 11].
There are no more overlapping intervals. The answer is [[1, 3], [6, 11]].

 

Function Description
Complete the function getMergedIntervals in the editor below.

 

getMergedIntervals has the following parameter(s):
    int intervals[[n][2]]:  the time intervals

 

Returns
    int[][2]: the merged intervals in sorted order
'''

'''
We will need to sort the intervals before we do anything else.
I want to use a stack to solve this, so we can take advantage of the fact we're sorting to 
reverse the intervals.

After they've been sorted and reversed, we will make a while loop, it will go as long as there is at least two intervals in our stack
for each loop we check if the current top of the stack can merge with the interval one element below it.
if so, we change the element one below to take the smallest start of the two, and the largest end of the two.
Else, meaning the interval at the top of our stack can't merge down, we pop it off and add it to our res list.
The loop will keep doing this until there is only one interval left in the stack, at which point we return res + intervals
'''

def merge_intervals(intervals) -> list: # BigO(n log n) time | BigO(n) space
    intervals.sort(reverse=True) # we sort and reverse the intervals
    res = [] # this will store our answer

    while len(intervals) > 1: # our while loop will loop until intervals only has one interval left in it.
        if intervals[-1][1] >= intervals[-2][0]: # if top interval can merge with the interval right below it.
            intervals[-2][0] = min(intervals[-2][0], intervals[-1][0]) # takes the smallest of the two intervals
            intervals[-2][1] = max(intervals[-2][1], intervals[-1][1]) # takes the largest of the two intervals
            intervals.pop() # remove the top interval, since we used the interval below for the merge we can throw this one away
        else:
            res.append(intervals.pop()) # if no merge can be made we pop off the top and append it to our res list.

    return res + intervals # finally we return res along with the last interval that is left in the stack

intervals = [[4, 8], [2, 6], [5, 7]]
print(merge_intervals(intervals))