# Lovelocal
Solution for interview assignment questions of Lovelocal company.
##Easy
#### Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal 
substring consisting of non-space characters only.
Explanation:-
The function length_of_last_word takes a string s as input.
It uses the split method to break the string into a list of words, using spaces as separators.
It then checks if there are any words in the list.If there are words, it returns the length of the last word in the list.
If there are no words, it returns 0.

##Medium
#### Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Explanation:-
Counter(nums) creates a dictionary-like object where keys are elements in nums, and values are their respective counts.
n = len(nums) // 3 calculates the threshold for majority elements based on the given condition.
The list comprehension [num for num, count in counter.items() if count > n] iterates through the items in the Counter and selects elements whose counts are greater than the threshold.
The function returns a list of elements that appear more than ⌊ n/3 ⌋ times in the input array.

##Hard
####Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
Explanation:-
Initialize count to 0, factor to 1, and i to 1.
Start a while loop that continues as long as i is less than or equal to n.
Inside the loop:
Calculate divisor as i * 10.
Update the count using the formula:
count += (n // divisor) * i + min(max(n % divisor - i + 1, 0), i)
This formula accounts for the occurrences of digit '1' in the current place (i.e., ones, tens, hundreds).
Multiply i by 10 to move to the next place value.
After the loop, return the final count.
The algorithm efficiently calculates the total count of digit '1' by considering each place value in the numbers from 1 to n.
