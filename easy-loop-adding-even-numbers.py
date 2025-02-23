"""
Instructions
You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

Example Input 1
10
Example Output 1
30
Example Input 2
52
Example Output 2
702
Hint
There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.
"""

target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum_of_even = 0
# The target + 1 is used because the end number in range() is exclusive, meaning the loop will stop right before it reaches target + 1
# Note: range(start, end - 1)
# So, when you use range(0, len(var)), it will create an index range from 0 to len(var) - 1. Which is also correct.
for number in range(1, target + 1):
  if number % 2 == 0:
    sum_of_even += number

print(sum_of_even)
