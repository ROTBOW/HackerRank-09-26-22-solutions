'''
A single roll operation on a string is a circular increment of each character by one. Looking at the English alphabet,
characters in the range ascii[a-z], a becomes b, b becomes c, and z becomes a.

 
Given an array of integers named roll, perform a roll operation on the first roll[i] characters of s for each element i in the array.
Given a zero indexed string, an operation roll[i] affects characters at positions 0 through (roll[i]-1).

Example 
s = 'abz'
roll = [3, 2, 1]


Perform the following sequence of operations:

roll[0] = 3: Roll all three characters so 'abz' becomes 'bca.'
roll[1] = 2: Roll the first two characters so 'bca' becomes 'cda'.
roll[2] = 1: Roll the first character so 'cda' becomes 'dda'.
After performing the operations, the final value of s is 'dda'.

 
Function Description 

Complete the function rollTheString in the editor below.

 

rollTheString has the following parameter(s):
    string s:  the string to operate on
    int roll[n]:  an array of integers indicating the number of items in s to roll
Returns:
     string :  the resulting string after all roll operations have been performed

 

Constraints

Each character in s is a character in the range ascii[a-z].
1 ≤ length of s ≤ 105
1 ≤ n ≤ 105
1 ≤ roll[i] ≤ length of s, where 0 ≤ i < n.
'''

'''
First we need to turn our string into a list, we need to do this since python doesn't allow us to reassign char in strings at indexes without reseting the entire str.
Then we will need a lowercase string of the alphabet, in python we can easily get that by importing ascii_lowercase from the string module.
We're going to make a nested loop, the outer loop will inter our roll, then we loop through str for each roll. 
We can use the str.index method to find the idx of our current char, and then add one to it (rolling our letter one forward).
If the idx we get is 26 or over we set our idx to 0 (restarting the loop through letters).
After all loops have ended, we can join the list and return.
'''

from string import ascii_lowercase as letters 
def roll_the_string(s: str, roll: list) -> str: # BigO(n * m) time | BigO(1) space
    s = list(s) # we turn our string into a list, so we can reassign letters at indexes

    for depth in roll: # loop through our roll
        for i in range(depth): # loop through our str for each roll
            idx = letters.index(s[i]) + 1 # get the index of the letter and add 1 to it
            if idx >= 26: # if our new idx is 26 or higher, we need to move our idx to the beginning of letters
                idx = 0 # we set idx to 0 to move it to the beginning.
            s[i] = letters[idx] # after we get the new idx, we reassign our current letter to the new letter at idx
            
    return ''.join(s) # after all loops have finished, we can join the list back into a string and return

s = 'abz'
roll = [3, 2, 1]
print(roll_the_string(s, roll))