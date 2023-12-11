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
     
    
