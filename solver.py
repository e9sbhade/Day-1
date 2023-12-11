#Write a function in python that returns the sum of all the multiples of a list of factors where the multiples are between the start and end, inclusive.
"""Edit the file solver.py to update the function solver which returns the answer when called as in the below example.

solver([3, 5, 12], 400, 1842)
"""

def solver(factors,start,end):
 
 numlist =  [] 

 for i in factors:
  for num in range(start, end):
    if num % i==0:
      if num not in numlist:
       numlist.append(num)

 addition = sum(numlist)
 return(addition)
    

print(solver([4,7,11],8912,40512 ))
     
    