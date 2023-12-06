# Algorithms-and-Data-Structures-for-Beginners

## Content of the exercises
In technical interviews, you will be expected to code up an efficient algorithm, talk comfortably about the design, analysis and tradeoffs of a specific algorithm. Being able to succinctly perform these tasks in a timely fashion and communicate your ideas in a coherent manner is what can make the difference in thousands of dollars of compensation.

### Topics Covered
Arrays,
Linked Lists,
Recursion,
Sorting,
Binary Search,
Trees,
Backtracking,
Heap/Priority Queue,
Hashing,
Graphs,
Dynamic Programming,
Bit Manipulation

### Exercise 1
#### Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
<br>
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
<br>
<br>
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
<br>Return k.

### Exercise 2
#### Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
<br>
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
<br>
- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
- Return k.

##### Example 2
Input: nums = [0,0,1,1,1,2,2,3,3,4] <br>
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]<br>
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.<br>
It does not matter what you leave beyond the returned k (hence they are underscores).

### Exercise 3
#### Concatenation of Array
Welcome to the repository for the solution to the "Concatenation of Array" problem (LeetCode Problem #1929). In this problem, we are given an integer array nums of length n, and the task is to create a new array ans by concatenating two copies of the nums array.<br>

##### Problem Description<br>
Given an integer array nums of length n, you need to create an array ans of length 2n such that ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed). The resulting array ans is essentially the concatenation of two identical nums arrays.<br>

###### Example 1: <br>
Input: nums = [1,2,1] <br>
Output: [1,2,1,1,2,1] <br>

##### Constraints: <br>
n == nums.length <br>
1 <= n <= 1000<br>
1 <= nums[i] <= 1000<br>
##### Implementation
The solution to this problem can be found in the source code provided in this repository. You can use the provided code as a reference or directly incorporate it into your project.

### Exercise 4
#### Contains Duplicate
Welcome to the repository for the solution to the "Contains Duplicate" problem (LeetCode Problem #217). In this problem, we are given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.<br>

##### Problem Description<br>
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.<br>

###### Example 1: <br>
Input: nums = [1,2,3,1] <br>
Output: true <br>

##### Constraints: <br>
- 1 <= nums.length <= 105<br>
- 109 <= nums[i] <= 109<br>
##### Implementation
The solution to this problem can be found in the source code provided in this repository. You can use the provided code as a reference or directly incorporate it into your project.

### Exercise 5
#### Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target (LeetCode Problem #1)

You may assume that each input would have exactly one solution, and you may not use the same element twice. <br>

You can return the answer in any order. <br>

###### Example 1: <br>
Input: nums = [2,7,11,15], target = 9<br>
Output: [0,1]<br>
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

##### Implementation
The solution to this problem can be found in the source code provided in this repository. You can use the provided code as a reference or directly incorporate it into your project. I included two different answers for the same exercise being different in their time complexity.

### Exercise 6
#### Design HashSet
<b>Overview</b><br>
This repository contains a Python implementation of a simplified HashSet as described in the problem statement (705. Design HashSet). The goal is to design a HashSet without using any built-in hash table libraries. The provided MyHashSet class supports three main operations: adding a key, checking if a key exists, and removing a key.

##### Implementation
<b>Class Methods</b>
__init__(self)<br>

Initializes an empty HashSet.<br>
add(self, key)<br>
<br>

Inserts the value key into the HashSet. <br>
- contains(self, key)

Returns whether the value key exists in the HashSet or not. <br>
- remove(self, key) <br>

Removes the value key from the HashSet. If the key does not exist, no action is taken. <br>
<b> Example Usage <br></b>

##### Example usage
myHashSet = MyHashSet()<br>
myHashSet.add(1)          # set = [1] <br>
myHashSet.add(2)          # set = [1, 2]<br>
print(myHashSet.contains(1))  # True <br>
print(myHashSet.contains(3))  # False<br>
myHashSet.add(2)        # set = [1, 2] <br>
print(myHashSet.contains(2))  # True<br>
myHashSet.remove(2)      # set = [1]<br>
print(myHashSet.contains(2))  # False<br>

##### Constraints
0 <= key <= 10^6 <br>
At most 10^4 calls will be made to add, remove, and contains.
