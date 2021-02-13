# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6  to 20 , print Weird
# If  is even and greater than 20 , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.



#!/bin/python
if __name__ == '__main__':
    n = int(input().strip())
    if(n%2 != 0):
        print("Weird")
    elif(n%2 == 0):
      if(n in range(1,6)):
        print("Not Weird")
      elif(n in range(6,21) ):              
        print("Weird")
      elif(n > 20):
        print("Not Weird")
        
                                                                                                                                                                                                                                                                                                                                               
    
